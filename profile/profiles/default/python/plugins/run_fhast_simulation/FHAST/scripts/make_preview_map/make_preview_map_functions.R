################################################################################
# These functions are used to make the preview map
################################################################################

# This function changes a raster to an object that can be plotted with ggplot
raster_to_df <- function(raster = NULL) {
  test_spdf <- as(raster, "SpatialPixelsDataFrame")
  test_df <- as.data.frame(test_spdf)
  colnames(test_df) <- c("value", "x", "y")
  return(test_df)
}

# constructs the plot
make_map_plot <- function() {
  ##### Process things for map #####
  # Get the grid oputline
  river_appx = ml$df$center_line %>% 
    smooth(method = "ksmooth",
           max_distance = ml$df$habitat_parms$resolution,
           bandwidth = ml$df$habitat_parms$resolution*10) %>% 
    st_buffer(dist = ml$df$habitat_parms$buffer, endCapStyle = "FLAT")
  
  # Get a sample raster file to get the extent
  # find all the depth and velocity rasters
  d_files <- list.files(ml$path$raster_folder, "D\\d+.tif", full.names = TRUE)

  # remove just the values from the file lists.
  flow_values <- str_remove(d_files, coll(ml$path$raster_folder)) %>%
    str_sub(start = 3) %>%
    str_extract(".*(?=\\.)") %>%
    as.numeric() %>%
    sort()
  example_flow <- flow_values[ceiling(length(flow_values) / 2)]
  example_raster <- raster(paste0(ml$path$raster_folder,"/D",example_flow,".tif"))
  
  raster_extent <- extent(example_raster) %>%
    as("SpatialPolygons") %>%
    st_as_sf() %>%
    st_set_crs(crs(river_appx))
  
  ##### Make the plot #####
  top_label = data.frame(x = st_coordinates(ml$df$top_marker)[1],
                         y = st_coordinates(ml$df$top_marker)[2],
                         name = "TOP")
  
  grid_extent <- extent(river_appx)
  map_plot <- ggplot() +
    theme_classic(base_size = 25) +
    geom_sf(data = raster_extent, fill = "#E8F5E9") +
    geom_sf(data = river_appx, aes(color = "Grid"), fill = NA) +
    geom_sf(data = ml$df$cover, aes(color = "Cover"), fill = NA) +
    geom_sf(data = ml$df$canopy, aes(color = "Canopy"), fill = NA) +
    geom_label(data = top_label, aes(x,y,label = name),
              size = 5, label.size = 1, color = "black")
  
  # If there is an AOI add it in
  if (!is.na(ml$path$aoi)) {
    map_plot <- map_plot +
      geom_sf(data = ml$df$aoi, aes(color = "AOI"), fill = NA, size = 2)
  }
  
  # mare map process that must be done after APO addation 
  map_plot <- map_plot +
    coord_sf(xlim = c(grid_extent[1], grid_extent[2]),
             ylim = c(grid_extent[3], grid_extent[4]), expand = FALSE) +
    scale_color_manual(name = NULL,
                       values = c(Grid = ml$df$palette[1],
                                  Cover = ml$df$palette[2],
                                  Canopy = ml$df$palette[3],
                                  AOI = ml$df$palette[8],
                                  Top = ml$df$palette[5])) +
    labs(caption = paste0(
      "The layout of the spatial input files. A green background means\n",
      "these shapes are within the bounds of the raster extent.")) +
    theme(plot.caption = element_text(hjust = 0, size = 15),
          panel.border = element_rect(colour = "black", fill = NA),
          axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))

  ##### Save the data #####
  write_sf(river_appx, here(ml$path$output_shape_folder, "preview_river_grid_outline.shp"),
           driver ="ESRI Shapefile")
  ggsave(filename =here(ml$path$output_folder, "preview_plot.png"),
         plot = map_plot,
         dpi = 300,
         device = "png",
         height = 10,
         width = 10,
         units = "in")
  
  return(map_plot)
}

################################################################################
# End
################################################################################