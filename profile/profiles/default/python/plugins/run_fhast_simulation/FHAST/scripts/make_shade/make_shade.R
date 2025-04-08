########################################
# This program takes in a shade shape file and calculates shade values
# for mid day, half way between sun rise and mid day, and half way
# between mid-day and sun set
# any where shaded in these times is considered shaded
########################################

##### Tolerance #####
# the units of tolerance to simplify shape
# units are whatever the crs of the shape file is
simplfly_tolarence = habitat_parm$resolution/2

# Set a different validity check then the default one... for some reason
rgeos::set_RGEOS_CheckValidity(2L)

##### Load functions #####
# Load Libraries and some base parameters
source(here("scripts","make_shade","make_shade_functions.R"))
source(here("scripts","make_shade","tree_growth_functions.R"))

temp_daily_file_path <- here(temp_folder,  "daily_input_file.csv")
temp_river_grid_path <- here(temp_folder, "river_grid.rds")
temp_shade_file_path <- here(temp_folder,  paste0("shade_file_", habitat_parm$veg_growth_years,".rds"))
temp_netlogo_daily_input_path <- here(temp_folder, "daily_input_file.csv")

input_output_file_paths <- c(ml$path$canopy, ml$path$tree_growth,
                             temp_daily_file_path,
                             temp_river_grid_path,
                             temp_shade_file_path)

hash_storage <-here(temp_folder, "calculate_shade_hashes.txt")

if (!compare_last_run_hashes(hash_storage, input_output_file_paths)) {
  ##### Load Files #####
  # load the daily files
  daily_file <- read.csv(file = temp_daily_file_path)
  
  # load the river grid and make it a mask
  river_grid = readRDS(temp_river_grid_path) 
  
  # Make a clip mask form the river grid
  clip_mask = river_grid %>%
    summarise() %>% 
    st_buffer(dist = 100)
  
  # Load the canopy cover zone file 
  # simplify it to speed up
  if(juvenile_run == TRUE){
    # make attributes constant to supress warnings
    st_agr(canopy_shape) = "constant"
    st_agr(clip_mask) = "constant"
    
    shade_shape = canopy_shape %>% 
      st_intersection(clip_mask) %>% 
      # Filter out empty ones
      filter(!st_is_empty(.)) %>% 
      grow_trees(parms = tree_growth_parms,
                 years = habitat_parm$veg_growth_years) %>%
      # This procedure simplifies the canopy while making it remain valid
      st_simplify(dTolerance = simplfly_tolarence) %>%
      st_buffer(0) %>%
      st_simplify(dTolerance = simplfly_tolarence) %>%
      group_by(height) %>%
      summarize() %>% 
      ungroup()
  } else {
    # Make a dummy shape for shade if just adults in the run 
    shade_shape = grid_center_line %>% 
      st_centroid() %>% 
      mutate(height = 1) %>% 
      select(height) %>% 
      st_buffer(1, nQuadSegs = 2)
  }
  
  # Make a list on months but in time format
  # also add in an arbitrary year and time
  times_list = as.list(paste0("2010-", seq(1,12,1), "-15 12:00:00"))
  
  # calculate photo period
  daily_w_photo_period = calc_photo_period(shade_shape, daily_file)
  
  # Run the function and combine all the shade layers by month
  result = future_map(times_list, ~make_shade_shape(shade_shape, .x)) %>% 
    future_map(~summarise(.x, shade = sum(shade)/sum(shade), do_union = TRUE)) %>% 
    future_map2(seq(1,12,1), ~rename(.x, !!paste0("shade_", .y) := shade))

  # save the files
  saveRDS(result, file = temp_shade_file_path)

  store_last_run_hashes(hash_storage, input_output_file_paths)
}

##### Load and save the outputs #####
  result = readRDS(file = temp_shade_file_path)
  walk(.x = seq(1,12,1), .f = ~write_sf(result[[.x]], here(output_shape_folder, paste0("shade_shape", .x, ".shp")),
                                        driver ="ESRI Shapefile"))
