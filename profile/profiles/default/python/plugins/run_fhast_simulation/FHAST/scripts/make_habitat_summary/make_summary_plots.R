##### Description #####
# This contains the functions used in make_habitat_summary

# set the base size once
selected_base_size = 20

##### Plotting Functions #####
# Line plot
make_line_plot <- function(data_frame_in, x_axis, y_axis, x_lab, y_lab, title = NULL) {
  output_plot <- ggplot(data_frame_in, aes(x = {{ x_axis }}, y = {{ y_axis }})) +
    theme_classic(base_size = selected_base_size) +
    theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1)) +
    ggtitle(title) +
    geom_path(
      color = cbPalette[1],
      linewidth = 1,
      linetype = "solid"
    ) +
    scale_y_continuous(y_lab) +
    labs(x = x_lab)
  
  return(output_plot)
}

# make a scatter plot
make_scatter_plot <- function(data_frame_in, x_axis, y_axis, x_lab, y_lab, title = NULL) {
  output_plot <- ggplot(data_frame_in, aes(x = {{ x_axis }}, y = {{ y_axis }})) +
    theme_classic(base_size = selected_base_size) +
    theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1)) +
    ggtitle(title) +
    geom_point(
      color = cbPalette[1],
      size = 2,
      shape = 1,
      stroke = 2
    ) +
    scale_y_continuous(y_lab) +
    labs(x = x_lab)
  
  return(output_plot)
}

# make a color coated sctter plot
make_color_scatter_plot <- function(data_frame_in,
                                    x_axis, y_axis,
                                    color, color_lab,
                                    x_lab, y_lab,
                                    title = NULL) {
  output_plot <- ggplot(data_frame_in, aes(x = {{ x_axis }},
                                        y = {{ y_axis }},
                                        color = {{color}})) +
    theme_classic(base_size = selected_base_size) +
    theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1)) +
    ggtitle(title) +
    geom_point(size = 2,
               shape = 1,
               stroke = 2) +
    scale_y_continuous(y_lab) +
    scale_color_viridis(name = color_lab) +
    labs(x = x_lab)
  
  return(output_plot)
}

# Function to make a map
# Depth map
make_map <- function(data_frame_in = NULL,
                     fill = NULL,
                     scale_name = NULL,
                     title = NULL) {
  output_map <- ggplot(data = data_frame_in) +
    theme_classic(base_size = selected_base_size) +
    theme(axis.text.x = element_text(angle = 90)) +
    geom_sf(aes(fill = {{ fill }}, color = {{ fill }})) +
    scale_fill_viridis(name = scale_name) +
    scale_color_viridis(name = scale_name, guide = "none")+
    ggtitle(title)

  return(output_map)
}

# Function to process an make the heat map
# the z value is the sum
make_heat_map = function(data_frame_in,
                         x_axis, y_axis, z_axis,
                         x_lab, y_lab, z_lab,
                         resolution){

  # Make a list for the x and y axis
  x_axis_select = deparse(substitute(x_axis))
  x_bins_list = seq(min(data_frame_in[[x_axis_select]]),
                    max(data_frame_in[[x_axis_select]]),
                    length.out = resolution)
  y_axis_select = deparse(substitute(y_axis))
  y_bins_list = seq(min(data_frame_in[[y_axis_select]]),
                    max(data_frame_in[[y_axis_select]]),
                    length.out = resolution)

  # Make a blank data frame and assign bins which will be used in the join
  blank_data_frame = data.frame(expand.grid(x_value = x_bins_list,
                                            y_value = y_bins_list,
                                            base_value = NA)) %>%
    mutate(y_bin = cut(y_value, breaks = seq(min(y_value),
                                             max(y_value),
                                             length.out = resolution),
                       include.lowest = TRUE),
           x_bin = cut(x_value, breaks = seq(min(x_value),
                                             max(x_value),
                                             length.out = resolution),
                       include.lowest = TRUE))

  # Now bin all the data in the data frame
  plot_df = data_frame_in  %>%
    st_drop_geometry() %>% 
    mutate(x_bin = cut({{x_axis}}, breaks = seq(min({{x_axis}}),
                                                max({{x_axis}}),
                                                length.out = resolution),
                       include.lowest = TRUE),
           y_bin = cut({{y_axis}}, breaks = seq(min({{y_axis}}),
                                                max({{y_axis}}),
                                                length.out = resolution),
                       include.lowest = TRUE)) %>%
    group_by(x_bin, y_bin) %>%
    summarise(total_z = sum({{z_axis}}, na.rm = TRUE)) %>%
    ungroup() %>%
    mutate(z_fraction = total_z/sum(total_z)) %>%
    full_join(blank_data_frame, by = c("x_bin", "y_bin")) %>%
    mutate(z_fraction_final = ifelse(is.na(z_fraction), 0 , z_fraction))

  # Make the plot
  heat_map_plot = ggplot(plot_df, aes(x = x_value,
                                      y = y_value,
                                      fill = z_fraction_final)) +
    theme_classic(base_size = selected_base_size) +
    geom_raster(interpolate = FALSE) +
    scale_x_continuous(expand = c(0, 0)) +
    scale_y_continuous(expand = c(0, 0)) +
    scale_fill_viridis(name = z_lab) +
    labs(x = x_lab, y = y_lab)

}

# Function to process an make the histogram
# the z value is the sum
make_hist <- function(data_frame_in = NULL,
                      bins = NULL,
                      weights = NULL,
                      x_label = NULL,
                      title = NULL) {
  output_hist <- ggplot(data = data_frame_in) +
    theme_classic(base_size = selected_base_size) +
    theme(axis.title.y=element_blank(),
          axis.text.y=element_blank(),
          axis.ticks.y=element_blank()) +
    geom_histogram(aes(x = {{ bins }},
                  y = after_stat(density),
                  weight = {{ weights }}),
                  bins = 20,
                  color = "black",
                  fill = "white") +
    labs(x = x_label)
  
  return(output_hist)
}