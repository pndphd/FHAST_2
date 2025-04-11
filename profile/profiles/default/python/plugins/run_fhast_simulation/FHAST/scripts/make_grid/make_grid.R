########################################
# This script runs the necessary functions to make and save a rive grid
########################################

##### Load functions used in the script #####
source(here("scripts","make_grid","make_grid_functions.R"))

# inputs
# ml$path$center_line, ml$path$hab, ml$path$top_marker
# outputs
# temp_river_grid_path, temp_river_grid_shape_path

temp_river_grid_path <- here(ml$path$output_temp_folder, "river_grid.rds")

temp_river_grid_shape_path <- here(ml$path$output_temp_folder, "river_grid.shp")

input_output_file_paths <- c(ml$path$center_line, ml$path$hab,
                             ml$path$top_marker, temp_river_grid_path,
                             temp_river_grid_shape_path)

hash_storage <-here(ml$path$output_temp_folder, "make_grid_run_hashes.txt")

if (!compare_last_run_hashes(hash_storage, input_output_file_paths)) {

  ##### Pre Processing #####
  # get a list of distances for buffers
  distances_list = make_distances_list(resolution = ml$df$habitat_parms$resolution,
                                       buffer = ml$df$habitat_parms$buffer)
  
  ##### Main Work #####
  # Load the center line and smooth it
  smooth_line = ml$df$center_line %>%
    # bandwidth = resolution*10 was a good value in testing
    smooth(method = "ksmooth",
           max_distance = ml$df$habitat_parms$resolution,
           bandwidth = ml$df$habitat_parms$resolution*10)
  
  # Make the buffers which are the lateral grid dividers
  # This next commented line will filter for only polygons
  buffers = make_buffers(distances = distances_list,
                         line = smooth_line,
                         resolution = ml$df$habitat_parms$resolution)
  
  # Make a file to tell left from right bank
  large_buffer = make_large_buffer(distances = distances_list,
                                   line = smooth_line)
  
  # Place sample points along the line
  sample_points = make_sample_points(resolution = ml$df$habitat_parms$resolution,
                                     line = smooth_line)
  
  # Make the Voronoi cells
  vor_cells = make_vor_cells(points = sample_points,
                             top = ml$df$top_marker,
                             resolution = ml$df$habitat_parms$resolution)
  
  # Combine the buffers and vornoi cells to make the grid
  grid = make_grid(resolution = ml$df$habitat_parms$resolution,
                   cells = vor_cells,
                   buffers = buffers,
                   large_buffer = large_buffer) %>% 
    # set left and right bank correctly
    mutate(lat_dist = ifelse(lat_dist>0, 
                             ifelse(left_or_right<0,
                                    lat_dist,
                                    -lat_dist),
                             0))
  
  ##### Trim Grid #####
  #get the rasters
  d_files = list.files(ml$path$raster_folder, "D\\d+.tif", full.names=TRUE)
  # remove just the values from the file lists.
  d_values = str_remove(d_files, coll(ml$path$raster_folder)) %>%
    str_sub(start = 3) %>%
    str_extract(".*(?=\\.)") %>%
    as.numeric() %>%
    sort()
  # find the value larger then the max flow
  max_raster_value = d_values[min(which(d_values > max(ml$df$daily_input$flow_cms)))]
  max_raster = rast(here(ml$path$raster_folder, paste0("D", max_raster_value, ".tif")))

# Filter the grid so only use potentially wetted cells
  # grid = exact_extract(max_raster, grid, fun = 'max', progress = FALSE) %>%
  #   data.frame() %>%
  #   # bind it back to the polygons
  #   cbind(data.frame(grid)) %>%
  #   na.omit() %>%
  #   select(-1) %>%
  #   st_as_sf()


  rm(max_raster)

  ##### Save Outputs #####
  saveRDS(grid, temp_river_grid_path)
  
  # rename some things to avoid a warning
  grid_save = grid %>% 
    rename(dist = distance,
           l_or_r = left_or_right)
  
  write_sf(grid_save, temp_river_grid_shape_path,
           driver ="ESRI Shapefile")

  store_last_run_hashes(hash_storage, input_output_file_paths) 
}

##### Load and save the outputs #####
result = read_sf(temp_river_grid_shape_path)
write_sf(result, here(ml$path$output_shape_folder, "river_grid.shp"),
         driver ="ESRI Shapefile")
