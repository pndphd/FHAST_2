################################################################################
# This program takes in a shade shape file and calculates shade values
# for mid day, half way between sun rise and mid day, and half way
# between mid-day and sun set
# any where shaded in these times is considered shaded
################################################################################

##### Tolerance #####
# the units of tolerance to simplify shape
# units are whatever the crs of the shape file is
simplfly_tolarence = ml$df$habitat_parms$resolution/2

# Set a different validity check then the default one... for some reason
rgeos::set_RGEOS_CheckValidity(2L)

##### Load functions #####
# Load Libraries and some base parameters
source(here("scripts","make_shade","make_shade_functions.R"))
source(here("scripts","make_shade","tree_growth_functions.R"))

ml$path$shade_file = here(ml$path$output_temp_folder,
                          paste0("shade_file_", ml$df$habitat_parms$veg_growth_years,".rds"))

input_output_file_paths = c(ml$path$canopy,
                            ml$path$tree_growth,
                            ml$path$daily_input_csv,
                            ml$path$river_grid,
                            ml$path$shade_file)

hash_storage = here(ml$path$output_temp_folder, "calculate_shade_hashes.txt")

if (!compare_last_run_hashes(hash_storage, input_output_file_paths)) {
  ##### Load Files #####
  # Make a clip mask form the river grid
  clip_mask = ml$df$grid %>%
    summarise() %>% 
    st_buffer(dist = 100)
  
  # Load the canopy cover zone file 
  # simplify it to speed up
  if(ml$var$juvenile_run == TRUE && !(ml$path$canopy == "no_canopy")){
    # make attributes constant to suppress warnings
    st_agr(ml$df$canopy) = "constant"
    st_agr(clip_mask) = "constant"
    
    shade_shape = ml$df$canopy %>% 
      st_intersection(clip_mask) %>% 
      # Filter out empty ones
      filter(!st_is_empty(.)) %>% 
      grow_trees(parms = ml$df$tree_growth_parms,
                 years = ml$df$habitat_parms$veg_growth_years) %>%
      # This procedure simplifies the canopy while making it remain valid
      st_simplify(dTolerance = simplfly_tolarence) %>%
      st_buffer(0) %>%
      st_simplify(dTolerance = simplfly_tolarence) %>%
      group_by(height) %>%
      summarize() %>% 
      ungroup()
  } else {
    # Make a dummy shape for shade if just adults in the run 
    shade_shape = ml$df$top_marker %>%
      mutate(height = ml$df$habitat_parms$resolution) %>%
      select(height) %>%
      st_buffer(ml$df$habitat_parms$resolution * 10, nQuadSegs = 2) 
  }
  
  # Make a list on months but in time format
  # also add in an arbitrary year and time
  times_list = as.list(paste0("2010-", seq(1,12,1), "-15 12:00:00"))
  
  # Run the function and combine all the shade layers by month
  result = future_map(times_list, ~make_shade_shape(shade_shape, .x)) %>% 
    future_map(~summarise(.x, shade = sum(shade)/sum(shade), do_union = TRUE)) %>% 
    future_map2(seq(1,12,1), ~rename(.x, !!paste0("shade_", .y) := shade))

  # make all 0's if using dummy shade file
  if(ml$var$juvenile_run == FALSE || ml$path$canopy == "no_canopy"){
    result = map2(.x = result,
                   .y = paste0("shade_", seq(1,12)),
                   .f = ~mutate(.x, {{.y}} := 0))
  }
  
  # save the files
  saveRDS(result, file = ml$path$shade_file)

  store_last_run_hashes(hash_storage, input_output_file_paths)
  rm(simplfly_tolarence, 
     result,
     clip_mask,
     shade_shape,
     times_list)
}

##### Load and save the outputs #####
ml$df$shade = readRDS(file = ml$path$shade_file)
walk(.x = seq(1,12,1),
     .f = ~write_sf(ml$df$shade[[.x]],
                    here(ml$path$output_shape_folder, paste0("shade_shape", .x, ".shp")),
                    driver ="ESRI Shapefile"))

# Clean up
rm(hash_storage,
   input_output_file_paths,
   simplfly_tolarence)

################################################################################
# End
################################################################################
