################################################################################
# This script takes two FHAST runs an makes a report of the differences for the 
# juvenile parts
################################################################################

##### Make Plots ###############################################################

# Predator Rating
ml$plot$pred_map = make_map(
  data_frame = ml$sum[[1]]$map,
  fill = hab_rating,
  scale_name = "Predator\nHabitat Rating")

ggsave(filename =here(output_folder, "pred_map.png"),
       plot =ml$plot$pred_map,
       dpi = 300,
       device = "png")

# Mortality risk
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

ggsave(filename =here(output_folder, "mort_map.png"),
       plot = ml$plot$mort_map,
       dpi = 300,
       device = "png",
       height = (length(ml$sum[grep("juvenile", names(ml$sum))]) + 1) * 3)

# Rearing time plot
ml$plot$rearing_plot = map(ml$df$detailed_data_list,
                           ~make_line_plot(data_frame = .x,
                                           x_axis = date,
                                           y_axis = rearers,
                                           x_lab =  "Date",
                                           y_lab = "Rearing Fish",
                                           title = .x$Species[1])) %>% 
  wrap_plots(ncol = 1, widths = ml$var$plot_width,
             heights = length(ml$df$detailed_data_list) * ml$var$plot_width)

ggsave(filename =here(output_folder, "abm_rearing_plot.png"),
       plot = ml$plot$rearing_plot,
       dpi = 300,
       device = "png",
       width = ml$var$plot_width,
       height = (length(ml$df$detailed_data_list)) * ml$var$plot_width)

# Growth time plot
ml$plot$growth_plot = map(ml$df$detailed_data_list,
                          ~make_line_plot(data_frame = .x,
                                          x_axis = date,
                                          y_axis = mean_rearing_growth_length,
                                          x_lab =  "Date",
                                          y_lab = "Growth (cm)",
                                          title = .x$Species[1])) %>% 
  wrap_plots(ncol = 1, widths = ml$var$plot_width,
             heights = length(ml$df$detailed_data_list) * ml$var$plot_width)

ggsave(filename =here(output_folder, "abm_growth_plot.png"),
       plot = ml$plot$growth_plot,
       dpi = 300,
       device = "png",
       width = ml$var$plot_width,
       height = (length(ml$df$detailed_data_list)) * ml$var$plot_width)

# Count vs. growth plot
ml$plot$count_v_growth_plot = map(ml$df$detailed_data_list,
                                  ~make_color_scatter_plot(data_frame = .x,
                                                           x_axis = rearers,
                                                           y_axis = mean_rearing_mass_growth_fra,
                                                           x_lab =  "Count",
                                                           y_lab = "Fraction Mass Increase",
                                                           color = run_day,
                                                           color_lab = "Run Day",
                                                           title = .x$Species[1])) %>% 
  wrap_plots(ncol = 1, widths = ml$var$plot_width,
             heights = length(ml$df$detailed_data_list) * ml$var$plot_width)

ggsave(filename =here(output_folder, "abm_count_v_growth_plot.png"),
       plot = ml$plot$count_v_growth_plot,
       dpi = 300,
       device = "png",
       width = ml$var$plot_width,
       height = (length(ml$df$detailed_data_list)) * ml$var$plot_width)

# Count vs. length plot
ml$plot$count_v_length_plot = map(ml$df$detailed_data_list,
                                  ~make_color_scatter_plot(data_frame = .x,
                                                           x_axis = rearers,
                                                           y_axis = mean_rearing_growth_length,
                                                           x_lab =  "Count",
                                                           y_lab = "Growth (cm)",
                                                           color = run_day,
                                                           color_lab = "Run Day",
                                                           title = .x$Species[1])) %>% 
  wrap_plots(ncol = 1, widths = ml$var$plot_width,
             heights = length(ml$df$detailed_data_list) * ml$var$plot_width)

ggsave(filename =here(output_folder, "abm_count_v_length_plot.png"),
       plot = ml$plot$count_v_length_plot,
       dpi = 300,
       device = "png",
       width = ml$var$plot_width,
       height = (length(ml$df$detailed_data_list)) * ml$var$plot_width)

# ABM mortality plot
ml$plot$mortality_plot = ggplot(data = ml$df$mortality_breakdown) +
  theme_classic(base_size = 20) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  labs(x = "Cause", y = "Mortality Counts") +
  geom_bar(aes(x = Cause, y = Count, fill = Species),
           stat="identity", position=position_dodge()) +
  scale_fill_manual(values = ml$df$palette)

ggsave(filename =here(output_folder, "abm_mortality_plot.png"),
       plot = ml$plot$mortality_plot,
       dpi = 300,
       device = "png")

################################################################################
# End
################################################################################