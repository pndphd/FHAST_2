################################################################################
# This script takes two FHAST runs an makes a report of the differences for the 
# adult parts
################################################################################

##### Make Plots ###############################################################

# Migration Map
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

ggsave(filename =here(output_folder, "migration_map.png"),
       plot = ml$plot$migration_map,
       dpi = 300,
       device = "png",
       width = ml$var$plot_width*1.5,
       height = (ml$var$migration_map_length) * ml$var$plot_width*1.5)

# Migration energy use
ml$plot$migration_energy_hist = ggplot(data = ml$df$adult_migration_energy_data) +
  theme_classic(base_size = 20) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1)) +
  labs(x = "Species", y = "Energy Used (kJ)") +
  geom_bar(aes(x = species, y = energy_cost),
           stat = "identity", position = position_dodge()) 


ggsave(filename =here(output_folder, "migration_energy_hist.png"),
       plot = ml$plot$migration_energy_hist,
       dpi = 300,
       device = "png")

################################################################################
# End
################################################################################