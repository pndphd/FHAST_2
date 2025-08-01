################################################################################
# This runs the scripts and functions to sample shape files with the grid
################################################################################

##### Load the functions #####
# Load the function to sample shapes on the grid
source(here("scripts","sample_shapes","sample_shapes_functions.R"))

ml$path$shape_data = here(ml$path$output_temp_folder, paste0("shape_data_input.rds"))

ml$path$shape_data_csv = here(ml$path$output_temp_folder, paste0("shape_data_input.csv"))

input_output_file_paths = c(ml$path$river_grid, ml$path$shade_file,
                            ml$path$cover, ml$path$hab,
                            ml$path$aoi, ml$path$wild,
                            ml$path$shape_data_csv)

hash_storage = here(ml$path$output_temp_folder, "sample_shapes_run_hashes.txt")

if (!compare_last_run_hashes(hash_storage, input_output_file_paths)) {
  ##### Main Work #####
  # get what is classified as benthic food habitat
  benthic_food_habitat = ml$df$habitat_parms$hab_benthic_hab %>% 
    str_split(",") %>% 
    pluck(1) %>% 
    str_trim(side = "both")
  # get what is classified as cover habitat
  cover_habitat = ml$df$habitat_parms$cover_hab %>% 
    str_split(",") %>% 
    pluck(1) %>% 
    str_trim(side = "both")
  # get what is classified as small cover habitat
  small_cover_habitat = ml$df$habitat_parms$small_cover_hab %>% 
    str_split(",") %>% 
    pluck(1) %>% 
    str_trim(side = "both")
  
  # make a list of files and variable names
  cover_names = list("veg", "wood", "fine", "gravel", "cobble", "rock")
  
  # Get a list of data frames with just one for each df that 
  shape_dfs = map(cover_names, ~select(ml$df$cover, matches(.x))) 
  
  the_variables = c(cover_names, as.list(paste0("shade_", seq(1,12,1))))
  shape_files = c(shape_dfs, ml$df$shade)
                    
  # Sample all the shapes over the grid
  sampeled_shapes = sample_all_shapes(ml$df$grid,
                                      shape_files,
                                      the_variables,
                                      the_variables) %>%
    # Add in column for benthic food, cover and small cover
    mutate(ben_food_fra = rowSums(across(all_of(benthic_food_habitat))),
           cover_fra = rowSums(across(all_of(cover_habitat))),
           small_cover_fra = rowSums(across(all_of(small_cover_habitat))))
  
 
  
  # Add in the AOI
  if(ml$path$aoi == "no_aoi"){
    ml$df$shape_data = sampeled_shapes %>%
      mutate(aoi = 1) %>% 
      st_as_sf(sf_column_name = "geometry") 
  } else {
    # Load the aoi shape
    ml$df$aoi = ml$df$aoi %>% 
    mutate(aoi = 1) %>% 
    select(aoi)
    
    ml$df$shape_data = sample_shape_with_grid(ml$df$grid, ml$df$aoi, "aoi", "aoi") %>%
      mutate(aoi = ifelse(aoi>0,1,0)) %>% 
      select(aoi, ID) %>% 
      right_join(sampeled_shapes, by = c("ID")) %>% 
      st_as_sf(sf_column_name = "geometry")
  }
  
  shapes_csv = sampled_to_csv(ml$df$shape_data)
  
  ##### Save Outputs #####
  write.csv(shapes_csv,
            ml$path$shape_data_csv,
            na = "-9999",
            row.names = FALSE)
  
  saveRDS(ml$df$shape_data, file = ml$path$shape_data)
  
  store_last_run_hashes(hash_storage, input_output_file_paths)
  
  rm(cover_names,
     shape_dfs,
     shape_files,
     the_variables,
     benthic_food_habitat,
     cover_habitat,
     small_cover_habitat,
     shapes_csv,
     sampeled_shapes)
}

##### Load and save the outputs #####
ml$df$shape_data = readRDS(file = ml$path$shape_data)
write_sf(ml$df$shape_data, here(ml$path$output_shape_folder, "sampeled_shape.shp"),
         driver ="ESRI Shapefile")

ml$df$full_grid = ml$df$shape_data %>% 
  select(-area) %>% 
  left_join(ml$df$sampeled_grid, by = c("lat_dist", "dist"))

rm(input_output_file_paths,
   hash_storage)

################################################################################
# End
################################################################################