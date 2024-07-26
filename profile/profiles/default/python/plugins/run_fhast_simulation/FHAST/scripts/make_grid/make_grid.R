########################################
# This script runs the necessary functions to make and save a rive grid
########################################

##### Load functions used in the script #####
source(here("scripts","make_grid","make_grid_functions.R"))

# inputs
# grid_center_line_path, hab_path, grid_top_marker_path
# outputs
# temp_river_grid_path, temp_river_grid_shape_path

temp_river_grid_path <- here(temp_folder, "river_grid.rds")

temp_river_grid_shape_path <- here(temp_folder, "river_grid.shp")

input_output_file_paths <- c(grid_center_line_path, hab_path,
                             grid_top_marker_path, temp_river_grid_path,
                             temp_river_grid_shape_path)

hash_storage <-here(temp_folder, "make_grid_run_hashes.txt")

if (!compare_last_run_hashes(hash_storage, input_output_file_paths)) {

  ##### Pre Processing #####
  # get a list of distances for buffers
  distances_list = make_distances_list(resolution = habitat_parm$resolution,
                                       buffer = habitat_parm$buffer)
  
  ##### Main Work #####
  # Load the center line and smooth it
  smooth_line = grid_center_line %>%
    # bandwidth = resolution*10 was a good value in testing
    smooth(method = "ksmooth",
           max_distance = habitat_parm$resolution,
           bandwidth = habitat_parm$resolution*10)
  
  # Make the buffers which are the lateral grid dividers
  # This next commented line will filter for only polygons
  buffers = make_buffers(distances = distances_list,
                         line = smooth_line,
                         resolution = habitat_parm$resolution)
  
  # Make a file to tell left from right bank
  large_buffer = make_large_buffer(distances = distances_list,
                                   line = smooth_line)
  
  # Place sample points along the line
  sample_points = make_sample_points(resolution = habitat_parm$resolution,
                                     line = smooth_line)
  
  # Make the Voronoi cells
  vor_cells = make_vor_cells(points = sample_points,
                             top = grid_top_marker,
                             resolution = habitat_parm$resolution)
  
  # Combine the buffers and vornoi cells to make the grid
  grid = make_grid(resolution = habitat_parm$resolution,
                   cells = vor_cells,
                   buffers = buffers,
                   large_buffer = large_buffer) %>% 
    # set left and right bank correctly
    mutate(lat_dist = ifelse(lat_dist>0, 
                             ifelse(left_or_right<0,
                                    lat_dist,
                                    -lat_dist),
                             0))
  
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
write_sf(result, here(output_shape_folder, "river_grid.shp"),
         driver ="ESRI Shapefile")
