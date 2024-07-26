# Function to get daily V and D
get_daily_data <- function(... ,
                           habitat_data,
                           fixed_data,
                           flows_list,
                           fish_schedule,
                           migration_area,
                           sig_figs) {
  current = list(...)

  # Get the month for later use in shade
  this_month <- month(mdy(current$date))

  shade_data = fixed_data %>%
    mutate(across(.cols = ends_with(paste0("shade_", this_month)),
                  ~.x,
                  .names = "shade")) %>% 
    select(shade, distance, lat_dist)

  # Get the flows just above and below this days flow
  high_flow <- min(subset(flows_list, flows_list > current$flow_cms))
  low_flow <- max(subset(flows_list, flows_list <= current$flow_cms))
  flow_fraction <- (current$flow_cms - low_flow) / (high_flow - low_flow)
  
  # Get the low flow match first
  filter_low_flow <- habitat_data %>%
    filter(flow == low_flow) %>%
    mutate(fraction_low_depth = depth * (1 - flow_fraction),
           fraction_low_velocity = velocity * (1 - flow_fraction),
           fraction_low_wetted = wetted_fraction * (1 - flow_fraction))

  mid_flow <- habitat_data %>%
    filter(flow == high_flow) %>%
    mutate(fraction_high_depth = depth * (flow_fraction),
           fraction_high_velocity = velocity * (flow_fraction),
           fraction_high_wetted = wetted_fraction * (flow_fraction)) %>%
    select(fraction_high_depth, fraction_high_velocity, distance,
           lat_dist, fraction_high_wetted) %>%
    left_join(filter_low_flow, by = c("distance", "lat_dist")) %>%
    mutate(depth = round(fraction_low_depth + fraction_high_depth, sig_figs),
           velocity = round(fraction_low_velocity + fraction_high_velocity, sig_figs),
           wetted_fraction = round(fraction_low_wetted + fraction_high_wetted, sig_figs)) %>%
    mutate(date = current$date) %>%
    # Select out this month's shade
    mutate(wetted_area = area*wetted_fraction,
           temp = current$temp_c,
           turb = current$turb_ntu,
           photoperiod = current$photoperiod)  %>% 
    select(date, depth, velocity, wetted_area, distance, lat_dist, temp, turb,
           photoperiod, area) %>% 
    left_join(shade_data, by = c("distance", "lat_dist"))

if(adult_run){
  todays_adults = filter(fish_schedule, date == current$date & lifestage == "adult")
  if (nrow(todays_adults) == 0) {
    migration_data <- data.table(date = NA_character_, species = NA_character_, energy_cost = NA, paths = NA, number = NA_real_)
  } else {
    todays_adults <- todays_adults %>%
      select(species, number)
    habitat_area = mid_flow %>% 
      left_join(migration_area, by = c("lat_dist", "distance"))
    migration_data <- get_path_min_costs_all_species(habitat_area, fish_parm, habitat_parm, todays_adults)
  }
} else {migration_data <- NA}

  return(list(v_and_d = mid_flow, mig_data = migration_data))
}