########################################
# This runs the scripts and functions to sample shape files with the grid
########################################

##### Load the functions #####
# Load the function to sample shapes on the grid
source(here("scripts","sample_shapes","sample_shapes_functions.R"))

# inputs
# temp_river_grid_path, temp_shape_file_path, ml$path$cover, ml$path$hab, ml$path$aoi
# outputs
# temp_netlogo_shape_data_path

temp_river_grid_path <- here(ml$path$output_temp_folder, paste0("river_grid.rds"))
temp_shape_file_path <- here(ml$path$output_temp_folder, paste0("shade_file_", ml$df$habitat_parms$veg_growth_years,".rds"))

temp_RDS_shape_data_path <- here(ml$path$output_temp_folder,
                                     paste0("Shape_Data_Input.rds"))

temp_netlogo_shape_data_path <- here(ml$path$output_temp_folder,
                                     paste0("Shape_Data_Input.csv"))

input_output_file_paths <- c(temp_river_grid_path, temp_shape_file_path,
                             ml$path$cover, ml$path$hab, ml$path$aoi, ml$path$wild,
                             temp_netlogo_shape_data_path)

hash_storage <-here(ml$path$output_temp_folder, "sample_shapes_run_hashes.txt")

# if (!compare_last_run_hashes(hash_storage, input_output_file_paths)) {

  ##### Load Files #####
  # Load the grid file
  river_grid = readRDS(temp_river_grid_path)
  # Load the shade file
  shade_file = readRDS(temp_shape_file_path) 
  
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
  shape_files = c(shape_dfs, shade_file)
                    
  # Sample all the shapes over the grid
  sampeled_shapes = sample_all_shapes(river_grid,
                                      shape_files,
                                      the_variables,
                                      the_variables) %>%
    # Add in column for benthic food, cover and small cover
    mutate(ben_food_fra = rowSums(across(all_of(benthic_food_habitat))),
           cover_fra = rowSums(across(all_of(cover_habitat))),
           small_cover_fra = rowSums(across(all_of(small_cover_habitat))))
  
 
  
  # Add in the AOI
  if(is.na(ml$path$aoi)){
    sampeled_w_aoi = sampeled_shapes %>%
      mutate(aoi = 1) %>% 
      st_as_sf(sf_column_name = "geometry") 
  } else {
    # Load the aoi shape
    ml$df$aoi = ml$df$aoi %>% 
    mutate(aoi = 1) %>% 
    select(aoi)
    
    sampeled_w_aoi = sample_shape_with_grid(river_grid, ml$df$aoi, "aoi", "aoi") %>%
      mutate(aoi = ifelse(aoi>0,1,0)) %>% 
      select(aoi, ID) %>% 
      right_join(sampeled_shapes, by = c("ID")) %>% 
      st_as_sf(sf_column_name = "geometry")
  }
  
  shapes_csv = sampled_to_csv(sampeled_w_aoi)
  
  ##### Save Outputs #####
  write.csv(shapes_csv,
            temp_netlogo_shape_data_path,
            na = "-9999",
            row.names = FALSE)
  
  saveRDS(sampeled_w_aoi, file = temp_RDS_shape_data_path)
  
  store_last_run_hashes(hash_storage, input_output_file_paths)
# }

##### Load and save the outputs #####
result = readRDS(file = temp_RDS_shape_data_path)
write_sf(result, here(ml$path$output_shape_folder, "sampeled_shape.shp"),
         driver ="ESRI Shapefile")

###########################################
# SETUP COMPLETE. YOU MAY NOW RUN NETLOGO #
###########################################
