################################################################################
# This is the main script to summarize habitat over the time window
################################################################################

##### Save Data ################################################################

# Save spatial average data
write.csv(x = here(ml$path$output_folder, st_drop_geometry(ml$sum[[1]]$map)),
          file = "habitat_map_data.csv",
          row.names = FALSE)

# Save time average data
write.csv(x = here(ml$path$output_folder, ml$sum[[1]]$day),
          file = "habitat_daily_data.csv",
          row.names = FALSE)

# Write all the fish daily data sets
deep_pluck(ml, "day") %>% 
walk2(.y = names(.),
      .f = ~write.csv(x = .x,
                      file = here(ml$path$output_folder, paste0(.y,"_daily.csv")),
                      row.names = FALSE))

# Write all the fish spatial data sets
deep_pluck(ml, "map") %>% 
  walk2(.y = names(.),
      .f = ~write.csv(x = .x,
                      file = here(ml$path$output_folder, paste0(.y,"_map.csv")),
                      row.names = FALSE))

# Write adult data
if (ml$var$adult_run == TRUE){
  # Write the adult migration map to csv
  walk(ml$df$adult_migration_map_data, ~write.csv(x = .x,
                                   file = here(ml$path$output_folder,
                                               paste0("adult_migration_path_",
                                                      .x$species[1],
                                                      ".csv")),
                                   row.names = FALSE))
  
  # Write the adult energy used data
  write.csv(x = here(ml$path$output_folder, ml$df$adult_migration_energy_data),
            file = "adult_migration_energy_data.csv",
            row.names = FALSE)
}

##### Save GIS Maps ############################################################

# Write the habitat map
write_sf(ml$sum[[1]]$map, here(ml$path$output_shape_folder, "habitat_map.shp"),
         driver ="ESRI Shapefile")

# Write the mean fish maps
deep_pluck(ml$sum, "map") %>% 
  walk2(.y = names(.),
      ~write_sf(obj = .x, 
                dsn = here(ml$path$output_shape_folder, paste0("fish_map_", .y, ".shp"))))

# Write the adult migration maps
if (ml$var$adult_run == TRUE){
  walk(ml$df$adult_migration_map_data,
       ~write_sf(obj = .x,
                 dsn = here(ml$path$output_shape_folder,
                            paste0("adult_migration_path_",
                                   .x$species[1],
                                   ".shp"))))
}

##### Save Plots and Tables ####################################################

# List of objects and names for the save files 
data_list = list(summary_stats = ml$table$summary_stats,
                 summary_stats_cutoff = ml$table$summary_stats_cutoff,
                 fish_energy_area_stats = ml$table$fish_energy_area_stats,
                 predator_rating_area_stats = ml$table$predator_rating_area_stats,
                 mort_risk_area_stats = ml$table$mort_risk_area_stats,
                 fish_summary_stats = ml$table$mort_risk_area_stats)

plot_list = list(cover_scatter_plot = ml$plot$cover_scatter_plot,
                 depth_velocity_heatmap = ml$plot$depth_velocity_heatmap,
                 cover_map = ml$plot$cover_map,
                 cover_cutoff_map = ml$plot$cover_cutoff_map,
                 cover_facet_hist = ml$plot$cover_facet_hist,
                 cutoff_map = ml$plot$cutoff_map,
                 metabolic_map = ml$plot$metabolic_map,
                 net_energy_map = ml$plot$net_energy_map)

plot_dimeshions = list(1.2, 1.2, 1.2, 1.2, 1.2, 1.2,
                       ml$var$metabolic_map_length + 1,
                       ml$var$net_energy_map_length + 1)

if (ml$var$juvenile_run == TRUE){
  plot_list = append(plot_list, list(pred_map = ml$plot$pred_map,
                                     mort_map = ml$plot$mort_map))
  plot_dimeshions = append(plot_dimeshions, list(1.2, ml$var$predation_map_length + 1))
}

if (ml$var$adult_run == TRUE){
  data_list = append(data_list,
                     list(migration_summary_stats = ml$table$migration_summary_stats))
  plot_list = append(plot_list, list(migration_map = ml$plot$migration_map,
                                     migration_energy_hist = ml$plot$migration_energy_hist))
  
  plot_dimeshions = append(plot_dimeshions, list((ml$var$migration_map_length + 1)/2,
                                                 (ml$var$migration_map_length + 1)/2))
}

object_list = c(data_list, plot_list, summary_data = ml$sum)

# Save all the outputs 
# walk2(object_list, names(object_list), ~saveRDS(object = .x,
#   file = here(ml$path$output_temp_folder, paste0(.y, ".rds"))))

# Save the summary tables as CSV
walk(data_list, names(data_list), ~write.csv(
  # Replace the fancy squared character for CSV
  x = mutate_all(.x, .funs = ~str_replace_all(.,"(m\u00B2)", " m^2")),
  file = here(ml$path$output_folder, paste0(.y, ".csv")),
   row.names = FALSE))

# Save for output
pwalk(list(plot_list, plot_dimeshions, names(plot_list)),
      ~suppressMessages(ggsave(height = ..2*5,
                               plot = ..1,
                               filename = here(ml$path$output_folder,
                                               paste0(..3, ".png")),
                               limitsize = FALSE,
                               device = "png")))

# Clean UP
rm(data_list, plot_dimeshions, plot_list, object_list)
gc()

################################################################################
# End
################################################################################