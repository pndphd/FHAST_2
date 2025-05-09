################################################################################
# This script takes two FHAST runs an makes a report of the differences for the 
# general habitat
################################################################################

##### Make Plots ###############################################################

# Cover vs flow scatter plot
ml$plot$cover_scatter_plot = make_scatter_plot(
  data_frame = ml$sum[[1]]$day,
  x_axis = ml_a$sum[[1]]$day$flow_cms,
  y_axis = total_cover,
  x_lab = "Flow (cms)",
  y_lab = expression(Cover ~ Area ~ (m^2)))

ggsave(filename =here(output_folder, "cover_scatter_plot.png"),
       plot = ml$plot$cover_scatter_plot,
       dpi = 300,
       device = "png",
       height = 5,
       width = 5,
       units = "in")

# Cover vs cutoff criteria map 
ml$plot$cover_cutoff_map_1 = ggplot(data = ml_a$sum[[1]]$map) +
  theme_classic(base_size = ml_a$var$selected_base_size) +
  theme(axis.text.x = element_text(angle = 90)) +
  labs(alpha = "Cover", fill = "Group") +
  geom_sf(aes(fill = factor(below_group), 
              alpha = ml$sum[[1]]$map$cover_fra), lwd = 0) +
  scale_fill_manual(values = c(ml$df$palette[3],
                               ml$df$palette[1],
                               ml$df$palette[2],
                               ml$df$palette[8]),
                    labels = c("1" = "Below D",
                               "0" = "Below None",
                               "11" = "Below Both",
                               "10" = "Below V"))
ml$plot$cover_cutoff_map_2 = ggplot(data = ml_b$sum[[1]]$map) +
  theme_classic(base_size = ml_a$var$selected_base_size) +
  theme(axis.text.x = element_text(angle = 90)) +
  labs(alpha = "Cover", fill = "Group") +
  geom_sf(aes(fill = factor(below_group), 
              alpha = ml$sum[[1]]$map$cover_fra), lwd = 0) +
  scale_fill_manual(values = c(ml$df$palette[3],
                               ml$df$palette[1],
                               ml$df$palette[2],
                               ml$df$palette[8]),
                    labels = c("1" = "Below D",
                               "0" = "Below None",
                               "11" = "Below Both",
                               "10" = "Below V"))

ml$plot$cover_cutoff_map = ml$plot$cover_cutoff_map_1 +
  ml$plot$cover_cutoff_map_2 +
  plot_layout(guides = "collect") +
  plot_layout(ncol = 1)

ggsave(filename =here(output_folder, "cover_cutoff_map.png"),
       plot = ml$plot$cover_cutoff_map,
       dpi = 300,
       device = "png",
       height = 10,
       width = 10,
       units = "in")

# Cover facet histogram
ml$plot$cover_facet_hist = ggplot(data = ml_a$sum[[1]]$map) +
  theme_classic(base_size = ml$var$selected_base_size) +
  theme(axis.title.y=element_blank(),
        axis.text.y=element_blank(),
        axis.ticks.y=element_blank()) +
  geom_histogram(aes(x = cover_fra,
                     y = after_stat(density),
                     weight = wetted_area),
                 bins = 20,
                 alpha = 0.5,
                 color = "black",
                 fill = ml$df$palette[2]) +
  geom_histogram(data = ml_b$sum[[1]]$map,
                 aes(x = cover_fra,
                     y = after_stat(density),
                     weight = wetted_area),
                 bins = 20,
                 alpha = 0.5,
                 color = "black",
                 fill = ml$df$palette[3]) +
  labs(x = "Percent Cover") +
  facet_grid(below_d_cutoff ~ below_v_cutoff,
             labeller = labeller(below_d_cutoff = c("1" = "Below D",
                                                    "0" = "Above D"),
                                 below_v_cutoff = c("1" = "Below V",
                                                    "0" = "Above V")))

ggsave(filename =here(output_folder, "cover_facet_hist.png"),
       plot =ml$plot$cover_facet_hist,
       dpi = 300,
       device = "png")

# D and V heat map plot
ml$plot$depth_velocity_heatmap_1 = make_heat_map(
  data_frame = ml_a$sum[[1]]$map,
  x_axis = depth,
  y_axis = velocity,
  z_axis = wetted_area,
  x_lab = "Depth (m)",
  y_lab = "Velcoity (m/s)",
  z_lab = expression(Area ~ (m^2)),
  resolution = 100) %>% 
  layer_data()

ml$plot$depth_velocity_heatmap_2 = make_heat_map(
  data_frame = ml_b$sum[[1]]$map,
  x_axis = depth,
  y_axis = velocity,
  z_axis = wetted_area,
  x_lab = "Depth (m)",
  y_lab = "Velcoity (m/s)",
  z_lab = expression(Area ~ (m^2)),
  resolution = 100) %>% 
  layer_data()

heatmap_data = ml$plot$depth_velocity_heatmap_1 %>% 
  mutate(z = z - ml$plot$depth_velocity_heatmap_2$z)

ml$plot$depth_velocity_heatmap = ggplot(heatmap_data,
                                        aes(x = x,
                                            y = y,
                                            fill = z)) +
  theme_classic(base_size = ml$var$selected_base_size) +
  geom_raster(interpolate = FALSE) +
  scale_x_continuous(expand = c(0, 0)) +
  scale_y_continuous(expand = c(0, 0)) +
  scale_fill_viridis(name = expression(Area ~ (m^2))) +
  labs(x = "Depth (m)", y = "Velcoity (m/s)",)

ggsave(filename =here(output_folder, "depth_velocity_heatmap.png"),
       plot = ml$plot$depth_velocity_heatmap,
       dpi = 300,
       device = "png",
       units = "in")

# Metabolic maps 
ml$plot$metabolic_map = deep_pluck(ml$sum, "map") %>% 
  map2(.x = ., .y = names(.), .f = ~make_map(
    data_frame = .x,
    fill = fish_met_j_per_day,
    scale_name = "Metabolic Rate\n(j/day)",
    title = str_replace_all(.y, c("-" = " ", "_" = " ")))) %T>% 
  assign(x = "temp_metabolic_map_length", value = length(.), envir = .GlobalEnv)%>% 
  wrap_plots(ncol = 1, widths = ml$var$plot_width,
             heights = temp_metabolic_map_length * ml$var$plot_width)

ggsave(filename =here(output_folder, "metabolic_map.png"),
       plot = ml$plot$metabolic_map,
       dpi = 300,
       device = "png",
       height = (length(ml$sum) + 1) * 3)

# Energy budget maps 
ml$plot$net_energy_map = deep_pluck(ml$sum, "map") %>%
  map2(.x = ., .y = names(.), .f = ~make_map(
    data_frame = .x %>% mutate(net_energy = ifelse(net_energy>=0, net_energy, 0)),
    fill = net_energy,
    scale_name = "Net Positive\nEnergy Areas\n(j/day)",
    title = str_replace_all(.y, c("-" = " ", "_" = " ")))) %T>% 
  assign(x = "temp_net_energy_map_length", value = length(.), envir = .GlobalEnv)%>% 
  wrap_plots(ncol = 1, widths = ml$var$plot_width,
             heights = temp_net_energy_map_length * ml$var$plot_width)

ggsave(filename =here(output_folder, "net_energy_map.png"),
       plot = ml$plot$net_energy_map,
       dpi = 300,
       device = "png",
       width = ml$var$plot_width,
       height = (length(ml$sum) + 1) * ml$var$plot_width)

##### Save the ml data #########################################################

saveRDS(ml, here(output_folder, "master_data_list.rds"))

################################################################################
# End
################################################################################