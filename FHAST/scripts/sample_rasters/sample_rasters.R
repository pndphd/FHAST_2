################################################################################
# This file runs the functions to sample rasters onto a grid 
################################################################################

##### Function Check and Load #####
# Make sure the area function is raster::area 
area = raster::area

# load the functions for this script
source(here("scripts", "sample_rasters", "sample_rasters_functions.R"))

ml$path$depth_and_velocity_csv = here(ml$path$output_temp_folder,
                                      paste0("depth_velocity_data_input.csv"))

input_output_file_paths = list.files(ml$path$raster_folder, full.names=TRUE)
input_output_file_paths = append(input_output_file_paths, ml$path$river_grid)
input_output_file_paths = append(input_output_file_paths,
                                 ml$path$depth_and_velocity_csv)
input_output_file_paths = append(input_output_file_paths,
                                 ml$path$fish_pop)

hash_storage = here(ml$path$output_temp_folder, "sample_raster_run_hashes.txt")

##### Load the flow list #####
# find all the depth and velocity rasters
d_files = list.files(ml$path$raster_folder, "D\\d+.tif", full.names=TRUE)
v_files = list.files(ml$path$raster_folder, "V\\d+.tif", full.names=TRUE)
# remove just the values from the file lists.
ml$df$flows = str_remove(d_files, coll(ml$path$raster_folder)) %>% 
  str_sub(start = 3) %>% 
  str_extract(".*(?=\\.)") %>% 
  as.numeric() %>% 
  sort()
v_values = str_remove(v_files, coll(ml$path$raster_folder)) %>% 
  str_sub(start = 3) %>% 
  str_extract(".*(?=\\.)") %>% 
  as.numeric() %>% 
  sort()

# check the flows aren't outside values
if(min(v_values) > min(ml$df$daily_input$flow_cms) |
   max(v_values) < max(ml$df$daily_input$flow_cms)){
  message(paste0("!!!!!!!!!!!\n",
                 "!!!ERROR!!! The hydrograph file has flow values outside the range of the V & D rasters. \n",
                 "!!!!!!!!!!!\n"))
  stop()
}
  
if (!compare_last_run_hashes(hash_storage, input_output_file_paths)) {
  ##### Main Part #####
  # Put all the rasters in a stack
  raster_stack_d = load_rasters(type = "depth",
                                folder = ml$path$raster_folder,
                                clip_mask = ml$df$grid)
  
  # Put all the rasters in a stack
  raster_stack_v = load_rasters(type = "velocity",
                                folder = ml$path$raster_folder,
                                clip_mask = ml$df$grid) 

  # Check that teh values all match
  if (!(all(ml$df$flows==v_values))) {
    stop('The velocity and depth flow values do not mtach.')
  }
  # Check that all CRSs are the same
  if (!(compareCRS(raster_stack_v, raster_stack_d) &
        compareCRS(crs(ml$df$grid), crs(raster_stack_d)))) {
    stop('The CRSs of some of your files are not the same.')
  }

  # Sample the grid over the raster stack
  sampeled_grid_d = sample_grid(stack = raster_stack_d,
                                grid = ml$df$grid,
                                flows = ml$df$flows,
                                type = "depth")
  
  # Sample the grid over the raster stack
  sampeled_grid_both = sample_grid(stack = raster_stack_v,
                              grid = ml$df$grid,
                              flows = ml$df$flows,
                              type = "velocity") %>% 
    left_join(sampeled_grid_d, by = c("lat_dist", "dist", "area"))
  
  # Add in the accessible migration cells for each species
  # Find the flow level
  ml$df$sampeled_grid =  map2_dfc(.x = ml$df$fish_parms$specie,
                                  .y = ml$df$fish_parms$adult_migration_min_flow,
                                  .f = ~ make_migration_paths(flows = ml$df$flows,
                                                              flow_level = .y,
                                                              species = .x,
                                                              df_in = sampeled_grid_both)) %>% 
    bind_cols(sampeled_grid_both)
  
  ##### Save Outputs #####
  # write the data
  write.csv(ml$df$sampeled_grid,
            ml$path$depth_and_velocity_csv,
            na = "0", 
            row.names = FALSE)
  
  store_last_run_hashes(hash_storage, input_output_file_paths)
  suppressWarnings(rm(raster_stack_d,
                      raster_stack_v,
                      sampeled_grid_d,
                      sampeled_grid_both))
}

suppressWarnings(rm(input_output_file_paths,
                    hash_storage,
                    d_files,
                    v_files,
                    v_values))

ml$df$sampeled_grid = read.csv(ml$path$depth_and_velocity_csv)

################################################################################
# End
################################################################################
