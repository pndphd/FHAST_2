################################################################################
# This is the main script to plot habitat over the time window
################################################################################

##### Line Plots ###############################################################

# 1D wetted plot area
ml$plot$cover_scatter_plot = make_scatter_plot(
  data_frame = ml$sum[[1]]$day,
  x_axis = flow_cms,
  y_axis = total_cover,
  x_lab = "Flow (cms)",
  y_lab = expression(Cover ~ Area ~ (m^2)))
display_plot(ml$plot$cover_scatter_plot)

##### Heat maps ################################################################

# 2D area cover heat map
ml$plot$depth_velocity_heatmap = make_heat_map(
  data_frame = ml$sum[[1]]$map,
  x_axis = depth,
  y_axis = velocity,
  z_axis = wetted_area,
  x_lab = "Depth (m)",
  y_lab = "Velcoity (m/s)",
  z_lab = expression(Area ~ (m^2)),
  resolution = 100)
display_plot(ml$plot$depth_velocity_heatmap)

##### Maps #####################################################################

# Set the plot widths
ml$var$plot_width = 5

# Wetted cover map
ml$plot$cover_map = make_map(data_frame = ml$sum[[1]]$map,
                             fill = cover_fra,
                             scale_name = "Cover\nFraction")
display_plot(ml$plot$cover_map)

# Cutoff map
ml$plot$cutoff_map = make_map(
  data_frame = ml$sum[[1]]$map %>%
    filter(depth < ml$df$habitat_parms$dep_cutoff,
           velocity < ml$df$habitat_parms$vel_cutoff),
  fill = (cover_fra),
  scale_name = "Cover\nFraction")
display_plot(ml$plot$cutoff_map)

# Predator maps
if (ml$var$juvenile_run == TRUE){
  ml$plot$pred_map = make_map(
    data_frame = ml$sum[[1]]$map,
    fill = hab_rating,
    scale_name = "Predator\nHabitat Rating")
  display_plot(ml$plot$pred_map)
  
  # Predation risk map
  ml$plot$mort_map = deep_pluck(ml$sum, "map") %>% 
    .[grep("juvenile", names(.))] %>%
    map2(.x = ., .y = names(.), .f = ~make_map(
      data_frame = .x,
      fill = pred_mort_risk,
      scale_name = "Mortality\nRisk",
      title = str_replace_all(.y, c("-" = " ", "_" = " ")))) %T>% 
    assign(x = "temp_predation_map_length", value = length(.), envir = .GlobalEnv) %>% 
    wrap_plots(ncol = 1, widths = ml$var$plot_width,
               heights = temp_predation_map_length * ml$var$plot_width)
  display_plot(ml$plot$mort_map, 15, 15)
  ml$var$predation_map_length = temp_predation_map_length
  rm(temp_predation_map_length)
}

# Cover facte map
ml$plot$cover_cutoff_map = ggplot(data = ml$sum[[1]]$map) +
  theme_classic(base_size = ml$var$selected_base_size) +
  theme(axis.text.x = element_text(angle = 90)) +
  labs(alpha = "Cover", fill = "Group") +
  geom_sf(aes(fill = factor(below_group), 
              alpha = cover_fra), lwd = 0) +
  scale_fill_manual(values = c(ml$df$palette[3],
                               ml$df$palette[1],
                               ml$df$palette[2],
                               ml$df$palette[8]),
                    labels = c("1" = "Below D",
                               "0" = "Below None",
                               "11" = "Below Both",
                               "10" = "Below V"))
display_plot(ml$plot$cover_cutoff_map, 10, 20)

# Adult migration map
if (ml$var$adult_run == 1){
  ml$plot$migration_map = ml$df$adult_migration_map_data %>% 
    map(~make_map(
      data_frame = .x,
      fill = num_paths,
      scale_name = "Frequency of Use",
      title = str_replace_all(paste0(.x$species[1]),
                              c("-" = " ", "_" = " ")))) %T>% 
    assign(x = "temp_migration_map_length", value = length(.), envir = .GlobalEnv)%>% 
    wrap_plots(ncol = 1, widths = ml$var$plot_width,
               heights = temp_migration_map_length * ml$var$plot_width)
  display_plot(ml$plot$migration_map, 15, 15)
  ml$var$migration_map_length = temp_migration_map_length
  rm(temp_migration_map_length)
}

# Metabolic map
ml$plot$metabolic_map = deep_pluck(ml$sum, "map") %>% 
  map2(.x = ., .y = names(.), .f = ~make_map(
    data_frame = .x,
    fill = fish_met_j_per_day,
    scale_name = "Metabolic Rate\n(j/day)",
    title = str_replace_all(.y, c("-" = " ", "_" = " ")))) %T>% 
  assign(x = "temp_metabolic_map_length", value = length(.), envir = .GlobalEnv) %>% 
  wrap_plots(ncol = 1, widths = ml$var$plot_width,
             heights = temp_metabolic_map_length * ml$var$plot_width)
display_plot(ml$plot$metabolic_map, 15, 15)
ml$var$metabolic_map_length = temp_metabolic_map_length
rm(temp_metabolic_map_length)

# Net energy map
ml$plot$net_energy_map = deep_pluck(ml$sum, "map") %>%
  map2(.x = ., .y = names(.), .f = ~make_map(
    data_frame = .x %>% mutate(net_energy = ifelse(net_energy>=0, net_energy, 0)),
    fill = net_energy,
    scale_name = "Net Positive\nEnergy Areas\n(j/day)",
    title = str_replace_all(.y, c("-" = " ", "_" = " ")))) %T>% 
  assign(x = "temp_net_energy_map_length", value = length(.), envir = .GlobalEnv)%>% 
  wrap_plots(ncol = 1, widths = ml$var$plot_width,
             heights = temp_net_energy_map_length * ml$var$plot_width)
display_plot(ml$plot$net_energy_map, 15, 15)
ml$var$net_energy_map_length = temp_net_energy_map_length
rm(temp_net_energy_map_length)

##### Histograms and bar plots #################################################

# Cover facet histogram
ml$plot$cover_facet_hist  <- make_hist(
  data_frame = ml$sum[[1]]$map,
  bins = cover_fra,
  x_label = "Percent Cover",
  weights = wetted_area) +
  facet_grid(below_d_cutoff ~ below_v_cutoff,
             labeller = labeller(below_d_cutoff = c("1" = "Below D", "0" = "Above D"),
                                 below_v_cutoff = c("1" = "Below V", "0" = "Above V")))
display_plot(ml$plot$cover_facet_hist, 10, 20)

if (ml$var$adult_run == 1){
  ml$plot$migration_energy_hist <- ggplot(ml$df$adult_migration_energy_data) +
    theme_classic(base_size = 20) +
    theme(axis.title.y=element_blank(),
          axis.text.y=element_blank(),
          axis.ticks.y=element_blank()) +
    geom_density(aes(x = energy_cost/1000,
                     y=after_stat(scaled)),
                 fill = ml$df$palette[1]) +
    labs(x = "Energy Cost (kJ)") +
    facet_wrap(species~., scales = "free", ncol = 1)
  display_plot(ml$plot$migration_energy_hist)
} 


################################################################################
# End
################################################################################
