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

suppressMessages(ggsave(filename =here(ml$path$output_folder, "migration_map.png"),
                        plot = ml$plot$migration_map,
                        dpi = 300,
                        device = "png",
                        width = ml$var$plot_width*1.5,
                        height = (ml$var$migration_map_length) * ml$var$plot_width*1.5))

# Migration energy use
ml$plot$migration_energy_hist = ggplot(data = ml$df$adult_migration_energy_data) +
  theme_classic(base_size = 20) +
  theme(axis.title.y=element_blank(),
        axis.text.y=element_blank(),
        axis.ticks.y=element_blank()) +
  geom_density(aes(x = energy_cost/1000,
                   y=after_stat(scaled),
                   color = species)) +
  labs(x = "Energy Cost (kJ)") +
  scale_color_manual(values = ml$df$palette)



suppressMessages(ggsave(filename =here(ml$path$output_folder, "migration_energy_hist.png"),
                        plot = ml$plot$migration_energy_hist,
                        dpi = 300,
                        device = "png"))

################################################################################
# End
################################################################################