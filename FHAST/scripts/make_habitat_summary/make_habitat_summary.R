################################################################################
# This is the main script to summarize habitat over the time window
################################################################################

##### Load Functions ###########################################################
source(here("scripts", "make_habitat_summary", "habitat_summary_plot_functions.R"))
source(here("scripts", "make_habitat_summary", "migration_path_functions.R"))
source(here("scripts", "make_habitat_summary", "habitat_summary_functions.R"))

##### Pre Processing ###########################################################

# Make a data frame with each cell at each flow value
v_d_data = make_cell_data(dl = ml) 

# Make an average predator from the predator parameter file
ml$df$pred_parm = read_csv(file = ml$path$predator,
                      col_types = cols(.default = "d", species = "c")) %>%
  # the 1 ensures the names are kept
  rename(species_temp = species) %>% 
  pivot_longer(cols=c(-species_temp), names_to="specie") %>%
  pivot_wider(names_from=c(species_temp)) %>% 
  mutate(area_pred_a = convert_logistic_parameters(area_pred_10, area_pred_90)[[1]],
         area_pred_b = convert_logistic_parameters(area_pred_10, area_pred_90)[[2]]) %>%
  select(-specie) %>% 
  as.list() 

##### Main Processing ##########################################################
# Get daily habitat and adult data 
# Make a list with one item being the daily habitat data 
# and the second being the migration data
daily_data_sets = ml$df$daily_input %>% 
  pmap(.f = ~get_daily_data(..., 
                            v_d_data = v_d_data,
                            dl = ml,
                            sig_figs = 10)) 

# Extract the habitat data that varies each day
ml$df$full_habitat = daily_data_sets %>% 
  map_df(.f = ~.x$v_and_d) %>%
  group_by(date) %>% 
  # Add in variable to calculate inundation and total predators
  mutate(reach_preds = round(ml$df$habitat_parms$pred_per_area * sum(wetted_area)),
         wetted = ifelse(wetted_area > 0, 1, 0)) %>% 
  ungroup() 

# Extract the migration data
if(ml$var$adult_run == TRUE){
  # Extract the data
  temp_adult_migration = daily_data_sets %>% 
    map_df(.f = ~.x$mig_data) %>% 
    na.omit()

  # Sum all paths in each cell by species
  paths = temp_adult_migration[, rbindlist(paths), by = .(species, number)] %>%
    .[, num_paths := num_paths * number] %>%
    .[, .(num_paths = sum(num_paths)), by = .(species, dist, lat_dist)] %>%
    as_tibble()

  # Combine all energy costs into one list per species
  energy_costs <- temp_adult_migration[, .(energy_cost = list(unlist(energy_cost))),
                                        by = .(species)] %>%
    as_tibble()
  
  adult_migration = list(paths = paths, energy_costs = energy_costs)
}

# Remove the large daily file and collect trash
rm(daily_data_sets, energy_costs, paths, temp_adult_migration, v_d_data)
ml$df$shape_data = NULL
ml$df$sampeled_grid = NULL
gc()

##### Get the averages both temporal and spatial (for aoi and non aoi) #####
# Get the summaries of the daily data

ml$sum = ml$df$fish_combos %>% 
  pmap(.f=~make_data_summary(..., dl = ml)) %>%
  # !!!!!!!! future_pmap(.f=~make_data_summary(..., dl = ml)) %>%
  setNames(map(., ~paste0(.x$species, "-", .x$lifestage))) 

# Format adult migration data 
if (ml$var$adult_run == 1){
  ml$df$adult_migration_energy_data = adult_migration$energy_costs %>% 
    unnest(energy_cost)
  ml$df$adult_migration_map_data = adult_migration$paths %>% 
    group_by(species) %>% 
    mutate(num_paths = num_paths/max(num_paths)) %>% 
    ungroup() %>% 
    left_join(ml$df$grid, by = c("dist", "lat_dist")) %>% 
    st_as_sf() %>% 
    split(f = .$species)
  
  rm(adult_migration)
}

##### Summary Stats For the Habitat #####
# The summary set for everything including outside the aoi
ml$table$summary_stats = make_summary_stats(df = ml$sum[[1]]$map_full,
                                   day_df = ml$sum[[1]]$day_full,
                                   value_name = "Full_Value") %>% 
      left_join(make_summary_stats(df = ml$sum[[1]]$map,
                                   day_df = ml$sum[[1]]$day,
                                   value_name = "AOI_Value"), by = "Item")

# The summary set divided up by the cutoffs 
ml$table$summary_stats_cutoff = make_summary_stats_cutoff(df = ml$sum[[1]]$map)

##### Summary Stats For the Fish #####
# A set of summary stats for net energy of fish in the AOI
ml$table$fish_energy_area_stats <- ml$sum %>%
  deep_pluck("map") %>%
  map2_df(names(ml$sum),
          ~ get_bined_results(df = .x,
                              column = net_energy,
                              name = "energy j/d") %>% 
           mutate(fish = .y)) 

# A set of summary stats for the fish in the full habitat
ml$table$fish_summary_stats_full <- deep_pluck(ml$sum, "map_full") %>%
  map_df(~ data.frame(met_j_per_day_full =
                        round(mean(.x$fish_met_j_per_day, na.rm = TRUE),2))) %>% 
  mutate(type = names(ml$sum)) 

# A set of summary stats for the fish
ml$table$fish_summary_stats <- deep_pluck(ml$sum, "map") %>%
  map_df(~ data.frame(met_j_per_day =
                        round(mean(.x$fish_met_j_per_day, na.rm = TRUE),2))) %>% 
  mutate(type = names(ml$sum))
       
# For the migrating adults
if (ml$var$adult_run == 1){
  ml$table$migration_summary_stats = ml$df$adult_migration_energy_data %>% 
    group_by(species) %>% 
    summarise(migration_energy_cost = mean(energy_cost, na.rm = TRUE)) %>% 
    ungroup()
} else{
  ml$table$migration_summary_stats = data.frame(migration_energy_cost = 0,
                                                Species = "None")
}

# For juveniles
if(ml$var$juvenile_run == 1){
  # A set of summary stats for the predator rating in the AOI
  ml$table$predator_rating_area_stats = ml$sum[[1]]$map %>%
    get_bined_results(column = hab_rating,
                      name = "predator rating") 
  
  # A set of summary stats for the fish mortality risk in the AOI
  ml$table$mort_risk_area_stats = deep_pluck(ml$sum, "map") %>% 
    .[grep("juvenile", names(.))] %>%
    map2_df(names(.[grep("juvenile", names(.))]),
            ~ get_bined_results(df = .x,
                                column = pred_mort_risk,
                                name = "mortailit risk") %>% 
              mutate(fish = .y)) 
}

################################################################################
# End
################################################################################