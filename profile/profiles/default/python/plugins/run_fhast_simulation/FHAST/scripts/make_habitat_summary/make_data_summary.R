# Function to make summaries of daily data

make_data_summary = function(..., habitat){

  # Get the attributes of the current fish
  fish_type = list(...)
  
  # get the life stage
  ls = fish_type$life_stage
  
  # Which species are we looking at
  id = which(fish_parm$specie == fish_type$species)
  
  # Give the parameter list a shorter name 
  pl = fish_parm
  
  # Get the example length
  fish_length =  ifelse(ls == "juvenile", pl$eg_juvenile_length[id], pl$eg_adult_length[id])
  
  # Calculate the fish mass
  fish_mass = pl$length_mass_a[id] * fish_length^pl$length_mass_b[id]
  
  # get example width for benthic feeding based on fish having the density of water 1g/cm^3
  # and being approximated as a rectangle
  fish_width = sqrt(fish_mass/fish_length)
  
  # Check if the fish feeds
  feeding_flag = ifelse(ls == "adult" & pl$adult_feeding[id] == 0, 0, 1)

  # calculate the wall factor reduction in velocity
  wall_factor = ifelse(pl$benthic_fish[id] == 0, 1,
                       # all the following hard coded constants from the
                       # relationship for the law of the wall
                       habitat_parm$base_wall_factor)

  # If there are juveniles do predation calculations
  if(juvenile_run & ls == "juvenile"){
    pred_results = map_dfc(seq(1, length(pred_parm[[1]]), 1),
                           ~calc_all_preds(.x, habitat, fish_length)) %>% 
      mutate(hab_rating = rowSums(across(starts_with("hab_rating"))),
             pred_mort_risk = rowSums(across(starts_with("pred_mort_risk")))) %>% 
      select(hab_rating, pred_mort_risk)
    
    # Bind the pred column to the habitat ones
    habitat = bind_cols(habitat, pred_results)
    
    # Clean up
    rm(pred_results)
    gc()
  }
  
  # Do the calculation for habitat and feeding
  habitat = habitat %>% 
    mutate(# Set if they use small cover
      cover_fra = if(pl$small_cover_length[id] >= fish_length) small_cover_fra else cover_fra,
      # Calculate max swim speed temperature function value
      max_swim_speed_temp = calc_beta_sig(parm_A = pl$ucrit_c[id],
                                          parm_B = pl$ucrit_d[id],
                                          temp = temp),
      # Calculate the max swim speed
      max_swim_speed = (pl$ucrit_a[id] / fish_length + pl$ucrit_b[id]) *
        max_swim_speed_temp * fish_length / 100,
      # Reduce velocity for benthic fish and in cover fish if habitat is available
      benthic_flag = pl$benthic_fish[id], 
      shelter_fraction = if_else(fish_length^2/1e4 < wetted_area*cover_fra & pl$benthic_fish[id] == 0,
                                 habitat_parm$shelter_frac,
                                 1),
      experienced_vel = wall_factor*velocity*shelter_fraction,
      # Calculate teh active and passive metabolic rate
      fish_met_j_per_day_active = calc_met(params = pl,
                                           fish_index = id,
                                           length = fish_length,
                                           temp = temp,
                                           velocity = experienced_vel),
      fish_met_j_per_day_passive = calc_met(params = pl,
                                            fish_index = id,
                                            length = fish_length,
                                            temp = temp,
                                            velocity = 0),
      # Calculate the total metabolic rate (benthic fish are assumed to be active at night)
      fish_met_j_per_day = ifelse(benthic_flag == 0,
                                  fish_met_j_per_day_active * (photoperiod) +
                                    fish_met_j_per_day_passive * (1 - photoperiod),
                                  fish_met_j_per_day_active * (1 - photoperiod) +
                                    fish_met_j_per_day_passive * (photoperiod)),
      # Remove places where the velocity is higher than Ucrit
      fish_met_j_per_day = ifelse(experienced_vel>max_swim_speed | depth <= 0, NA, fish_met_j_per_day),
      # Calculate cmax
      cmax = pl$cmax_a[id] * fish_mass^(1 + pl$cmax_b[id]) *
        calc_beta_sig(parm_A = pl$cmax_c[id],
                      parm_B = pl$cmax_d[id],
                      temp = temp),
      # Calculate the turbidity function
      turbidity_fun = ifelse(turb <= pl$turbid_threshold[id], 1,
                             pl$turbid_min[id] + (1 - pl$turbid_min[id]) *
                               exp(pl$turbid_exp[id] *
                                     (turb - pl$turbid_threshold[id]))),
      # Calculate detection distance, capture area, and success
      detection_dist = (pl$react_dist_a[id] +
                          pl$react_dist_b[id] * fish_length) * turbidity_fun,
      capture_area = 2 * detection_dist * pmin(depth, detection_dist),
      capture_success = calc_logistic(parm_10 = pl$capture_V1[id],
                                      parm_90 = pl$capture_V9[id],
                                      value = velocity/max_swim_speed),
      # Calculate food eaten per day
      drift_eaten = capture_success *capture_area * habitat_parm$hab_drift_con *
        velocity * 86400 * photoperiod,
      ben_eaten = pi * pl$feeding_speed[id] * fish_length / fish_width *
        86400 * (1 - photoperiod)  *
        fish_width^2 * habitat_parm$hab_bentic_con / (1E4 *
        log(pl$feeding_speed[id] * fish_length / fish_width *
              (1 - photoperiod) * 86400)),
      ben_avaiable = habitat_parm$hab_bentic_con *
        ben_food_fra * wetted_area,
      # Calculate the food eaten
      intake_ben_energy = pmin(ben_eaten, ben_avaiable, cmax)* habitat_parm$hab_bentic_ene,
      intake_drift_energy = pmin(drift_eaten, cmax)* habitat_parm$hab_drift_ene,
      # Calculate the energy intake and net energy
      energy_intake = (intake_ben_energy *pl$benthic_fish[id] + 
                         intake_drift_energy * (1 - pl$benthic_fish[id])) * feeding_flag,
      net_energy = energy_intake - fish_met_j_per_day) %>% 
    # Remove the temportay columns
    select(-ben_food_fra, -max_swim_speed_temp, -max_swim_speed, -shelter_fraction,
           -experienced_vel, -fish_met_j_per_day_active, -fish_met_j_per_day_passive,
           -cmax, -turbidity_fun, -detection_dist, -capture_area, -capture_success,
           -drift_eaten, -ben_eaten, -ben_avaiable, -intake_ben_energy,
           -intake_drift_energy, -small_cover_fra)

  # Make the average map
  average_map_full = habitat %>% 
    select(-date) %>% 
    group_by(lat_dist, distance) %>% 
    summarise_all(list(~mean(., na.rm = TRUE))) %>% 
    ungroup()
  
  average_map = habitat %>% 
    filter(aoi == 1) %>% 
    select(-date) %>% 
    group_by(lat_dist, distance) %>% 
    summarise_all(list(~mean(., na.rm = TRUE))) %>% 
    ungroup()
  
  # Make the average daily data 
  average_day_full = habitat %>%
    mutate(total_cover = wetted_area * cover_fra,
           date = mdy(date)) %>% 
    group_by(date) %>% 
    summarise_all(list(~mean(., na.rm = TRUE))) %>% 
    ungroup()
  
  average_day = habitat %>%
    filter(aoi == 1) %>% 
    mutate(total_cover = wetted_area * cover_fra,
           date = mdy(date)) %>% 
    group_by(date) %>% 
    summarise_all(list(~mean(., na.rm = TRUE))) %>% 
    ungroup()
  
  # Remove the habitat file and clean up 
  rm(habitat)
  gc()
  
  return(list(average_map = average_map,
              average_day =  average_day,
              average_map_full = average_map_full,
              average_day_full =  average_day_full,
              lifestage = ls,
              species = pl$specie[id]))
}

