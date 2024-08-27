########################################
# This file runs the functions to sample rasters onto a grid 
########################################
##### Function Check and Load #####
# Make sure the area function is raster::area 
area = raster::area

# load the functions for this script
source(here("scripts", "sample_rasters", "sample_rasters_functions.R"))
source(here("scripts", "sample_rasters", "make_migration_path.R"))

# inputs
# temp_river_grid_path, raster_folder_files
# outputs
# temp_netlogo_depth_velocity_path

temp_river_grid_path <- here(temp_folder,  
                         paste0("river_grid.rds"))
temp_netlogo_depth_velocity_path <- here(temp_folder, 
                                         paste0("Depth_Velocity_Data_Input.csv"))

input_output_file_paths <- list.files(raster_folder, full.names=TRUE)
input_output_file_paths <- append(input_output_file_paths, temp_river_grid_path)
input_output_file_paths <- append(input_output_file_paths,
                                  temp_netlogo_depth_velocity_path)
input_output_file_paths <- append(input_output_file_paths,
                                  fish_population_path)

hash_storage <-here(temp_folder, "sample_raster_run_hashes.txt")

if (!compare_last_run_hashes(hash_storage, input_output_file_paths)) {

  ##### Load some files #####
  # load the river grid
  river_grid = readRDS(temp_river_grid_path)

  ##### Load the flow list #####
  # find all the depth and velocity rasters
  d_files = list.files(raster_folder, "D\\d+.tif", full.names=TRUE)
  v_files = list.files(raster_folder, "V\\d+.tif", full.names=TRUE)
  # remove just the values from the file lists.
  d_values = str_remove(d_files, coll(raster_folder)) %>% 
    str_sub(start = 3) %>% 
    str_extract(".*(?=\\.)") %>% 
    as.numeric() %>% 
    sort()
  v_values = str_remove(v_files, coll(raster_folder)) %>% 
    str_sub(start = 3) %>% 
    str_extract(".*(?=\\.)") %>% 
    as.numeric() %>% 
    sort()
  
  # check the folow arent outside values
  if(min(v_values) > min(daily_w_photo_period$flow_cms) | 
     max(v_values) < max(daily_w_photo_period$flow_cms)){
    message(paste0("!!!!!!!!!!!\n",
                   "!!!ERROR!!! The hydrograph file has flow values outside the range of the V & D rasters. \n",
                   "!!!!!!!!!!!\n"))
    stop()
  }

  ##### Main Part #####
  # Put all the rasters in a stack
  raster_stack_d = load_rasters(type = "depth",
                                folder = raster_folder,
                                clip_mask = river_grid)
  
  
  # Put all the rasters in a stack
  raster_stack_v = load_rasters(type = "velocity",
                                folder = raster_folder,
                                clip_mask = river_grid) 


  # Check that teh values all match
  if (!(all(d_values==v_values))) {
    stop('The velocity and depth flow values do not mtach.')
  }
  # Check that all CRSs are the same
  if (!(compareCRS(raster_stack_v, raster_stack_d) &
        compareCRS(crs(river_grid), crs(raster_stack_d)))) {
    stop('The CRSs of some of your files are not the same.')
  }

  # Sample the grid over the raster stack
  sampeled_grid_d = sample_grid(stack = raster_stack_d,
                                grid = river_grid,
                                flows = d_values,
                                type = "depth")
  
  # Sample the grid over the raster stack
  sampeled_grid_both = sample_grid(stack = raster_stack_v,
                              grid = river_grid,
                              flows = d_values,
                              type = "velocity") %>% 
    left_join(sampeled_grid_d, by = c("lat_dist", "distance", "area"))
  
  # Add in the accessible migration cells for each species
  # Find the flow level
  sampeled_grid =  map2_dfc(.x = fish_parm$specie,
                           .y = fish_parm$adult_migration_min_flow,
                           .f = ~ make_migration_paths(flows = d_values,
                                                       flow_level = .y,
                                                       species = .x,
                                                       df_in = sampeled_grid_both)) %>% 
    bind_cols(sampeled_grid_both)
  
  ##### Save Outputs #####
  # write the data
  write.csv(sampeled_grid,
            temp_netlogo_depth_velocity_path,
            na = "0", 
            row.names = FALSE)
  
  ##### Make Plots #####
  if(0){
    # Plot and example
    stats_plot = sampeled_grid %>% 
      mutate(depth = ifelse(is.nan(mean.D300),NA, mean.D300)) 
    g = ggplot(stats_plot, aes(x = x , y = y , fill = depth )) +
      theme_classic() +
      geom_raster(na.rm = TRUE)
    g
    
    # Plot the bottom difference
    stats_plot = sampeled_grid %>% 
      mutate(difference = ifelse((bottom_area-area) == 0, NA, (bottom_area-area)))
    g = ggplot(stats_plot, aes(x = x , y = y , fill = (difference) )) +
      theme_classic() +
      geom_raster(na.rm = T)
    g
  }
  
  store_last_run_hashes(hash_storage, input_output_file_paths)
}
