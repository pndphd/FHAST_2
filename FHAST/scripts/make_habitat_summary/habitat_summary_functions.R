################################################################################
# This makes functions for the summarize habitat script
################################################################################

##### Get daily V and D #####
get_daily_data <- function(... ,
                           v_d_data,
                           dl,
                           sig_figs) {
  
  # get todays variabel values
  current = list(...)

  # select just the shade for this month
  shade_data = dl$df$full_grid 
  
  # Get the flows just above and below this days flow
  high_flow <- min(subset(dl$df$flows, dl$df$flows > current$flow_cms))
  low_flow <- max(subset(dl$df$flows, dl$df$flows <= current$flow_cms))
  flow_fraction <- (current$flow_cms - low_flow) / (high_flow - low_flow)
  
  # Get the low flow match first
  low_flow_df <- v_d_data %>%
    filter(flow == low_flow) %>%
    mutate(fraction_low_depth = depth * (1 - flow_fraction),
           fraction_low_velocity = velocity * (1 - flow_fraction),
           fraction_low_wetted = wetted_fraction * (1 - flow_fraction))
  
  # Get the mid flow values and join to the habitat df
  mid_flow_df <- v_d_data %>%
    filter(flow == high_flow) %>%
    mutate(fraction_high_depth = depth * (flow_fraction),
           fraction_high_velocity = velocity * (flow_fraction),
           fraction_high_wetted = wetted_fraction * (flow_fraction)) %>%
    select(fraction_high_depth, fraction_high_velocity, dist,
           lat_dist, fraction_high_wetted) %>%
    left_join(low_flow_df, by = c("dist", "lat_dist")) %>%
    mutate(depth = round(fraction_low_depth + fraction_high_depth, sig_figs),
           velocity = round(fraction_low_velocity + fraction_high_velocity, sig_figs),
           wetted_fraction = round(fraction_low_wetted + fraction_high_wetted, sig_figs)) %>%
    mutate(date = current$date,
           temp = current$temp_c,
           turb = current$turb_ntu,
           photoperiod = current$photoperiod) %>%
    select(date, depth, velocity, wetted_fraction, dist, lat_dist, temp, turb,
           photoperiod) %>% 
    # Join to the full grid data
    left_join(dl$df$full_grid, by = c("dist", "lat_dist")) %>% 
    # just keep shade values for that month
    mutate(wetted_area = area*wetted_fraction,
           across(.cols = ends_with(paste0("shade_", current$month)),
                  ~.x,
                  .names = "shade")) %>% 
    select(-starts_with(c("shade_", "wetd.D", "mean.V", "mean.D")))


  # Do migration calculations for adults
  if(dl$var$adult_run){
    todays_adults = dl$df$fish_schedule %>% 
      filter(date == current$date & lifestage == "adult")
    if (nrow(todays_adults) == 0) {
      migration_data <- data.table(date = NA,
                                   species = NA_character_,
                                   energy_cost = NA,
                                   paths = NA,
                                   number = NA_real_)
    } else {
      todays_adults <- todays_adults %>%
        select(species, number)
      migration_data <- get_path_min_costs_all_species(mid_flow_df,
                                                       dl$df$fish_parms,
                                                       dl$df$habitat_parms,
                                                       todays_adults)
    }
  } else {migration_data <- NA}
  
  return(list(v_and_d = mid_flow_df, mig_data = migration_data))
}

##### Makes dataframe with info on each cell at each flow #####
make_cell_data <- function(dl){
  habitat_temp <- dl$df$sampeled_grid %>%
    # remove some unneeded columns
    select(-starts_with("mig_path_"),
           -bottom_area,
           -mean.correction_factor) %>% 
    left_join(select(dl$df$shape_data, dist, lat_dist, aoi),
              by = c("dist", "lat_dist"))
  
  # Make the data just one depth, vel and wetted area per flow per cell
  input_variables <- c("mean.D", "mean.V", "wetd.")
  output_variables <- c("depth", "velocity", "wetted_fraction")
  spread_data <- future_map2(
    input_variables, output_variables,
    ~ spread_flows(habitat_temp, .x, .y)) %>%
    reduce(left_join, by = c("lat_dist", "dist", "flow"))
  
  #construct a data frame with all possible flows over the model area
  habitat <- habitat_temp %>%
    select(-starts_with("mean.D"),
           -starts_with("mean.V"),
           -starts_with("wetd.D")) %>%
    right_join(spread_data, by = c("lat_dist", "dist")) %>%
    select(wetted_fraction, velocity, depth, dist, lat_dist, flow)

  # remove some unused things
  rm(spread_data, habitat_temp)
  
  return(habitat)
}

##### Spreads out the flows so they are just one depth and v per flow #####
spread_flows <- function(v_d_data, input_variable, output_variable) {
  spread_df <- v_d_data %>%
    # spread out the flows
    select(
      starts_with(input_variable),
      dist,
      lat_dist
    ) %>%
    pivot_longer(
      cols = starts_with(input_variable),
      names_to = "temp_flow",
      values_to = output_variable
    ) %>%
    mutate(flow = as.numeric(str_sub(string = temp_flow, start = 7))) %>%
    select(-temp_flow) %>% 
    distinct()
}

##### Make summaries of daily data #####
make_data_summary = function(..., dl){
  # Get the attributes of the current fish
  fish_type = list(...)

  # get the life stage
  ls = fish_type$lifestage
  
  # Which species are we looking at
  id = which(dl$df$fish_parms$specie == fish_type$species)
  
  # Give the parameter list a shorter name 
  pl = dl$df$fish_parms

  # Get the example length
  fish_length =  ifelse(ls == "juvenile", pl$eg_juvenile_length[id], pl$eg_adult_length[id])
  
  # Calculate the fish mass
  fish_mass = pl$length_mass_a[id] * fish_length^pl$length_mass_b[id]
  
  # get example width for benthic feeding based on fish having the density of water 1g/cm^3
  # and being approximated as a rectangle
  fish_width = sqrt(fish_mass/fish_length)

  # Check if the fish feeds
  feeding_flag = ifelse(ls == "adult" & pl$adult_feeding[id] == 0, 0, 1)
  
  # Calculate max swim speed temperature function value
  max_swim_speed_temp = calc_beta_sig(parm_A = pl$ucrit_c[id],
                                      parm_B = pl$ucrit_d[id],
                                      temp = dl$df$full_habitat$temp[1])
  # Calculate the max swim speed
  max_swim_speed = (pl$ucrit_a[id] / fish_length + pl$ucrit_b[id]) *
    max_swim_speed_temp * fish_length / 100
  
  # calculate the wall factor reduction in velocity
  wall_factor = ifelse(pl$benthic_fish[id] == 0, 1,
                       # all the following hard coded constants from the
                       # relationship for the law of the wall
                       dl$df$habitat_parms$base_wall_factor)

  # If there are juveniles do predation calculations
  if(dl$var$juvenile_run & ls == "juvenile"){
    pred_results = map_dfc(seq(1, length(dl$df$pred_parm[[1]]), 1),
                           ~calc_all_preds(.x, dl, fish_length)) %>% 
      mutate(hab_rating = rowSums(across(starts_with("hab_rating"))),
             pred_mort_risk = rowSums(across(starts_with("pred_mort_risk")))) %>% 
      select(hab_rating, pred_mort_risk)
    
    # Bind the pred column to the habitat ones
    dl$df$full_habitat = bind_cols(dl$df$full_habitat, pred_results)
    
    # Clean up
    rm(pred_results)
    gc()
  }
  
  # Do the calculation for habitat and feeding
  calc_hab_and_feed = function(df, add){

    df = mutate(df, velocity = velocity + add)
    
    output = df %>%
      mutate(# Set if they use small cover
      cover_fra = if(pl$small_cover_length[id] >= fish_length) small_cover_fra else cover_fra,
      # Reduce velocity for benthic fish and in cover fish if habitat is available
      benthic_flag = pl$benthic_fish[id], 
      shelter_fraction = if_else(fish_length^2/1e4 < wetted_area*cover_fra & pl$benthic_fish[id] == 0,
                                 dl$df$habitat_parms$shelter_frac,
                                 1),
      experienced_vel = wall_factor*velocity*shelter_fraction) %>% 
      # Remove places where the velocity is higher than Ucrit
      filter(experienced_vel <= max_swim_speed,
             depth > 0) %>% 
      mutate(# Calculate teh active and passive metabolic rate
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
      drift_eaten = capture_success *capture_area * dl$df$habitat_parms$hab_drift_con *
        velocity * 86400 * photoperiod,
      ben_eaten = pi * pl$feeding_speed[id] * fish_length / fish_width *
        86400 * (1 - photoperiod)  *
        fish_width^2 * dl$df$habitat_parms$hab_bentic_con / (1E4 *
                                                               log(pl$feeding_speed[id] * fish_length / fish_width *
                                                                     (1 - photoperiod) * 86400)),
      ben_avaiable = dl$df$habitat_parms$hab_bentic_con *
        ben_food_fra * wetted_area,
      # Calculate the food eaten
      intake_ben_energy = pmin(ben_eaten, ben_avaiable, cmax)* dl$df$habitat_parms$hab_bentic_ene,
      intake_drift_energy = pmin(drift_eaten, cmax)* dl$df$habitat_parms$hab_drift_ene,
      # Calculate the energy intake and net energy
      energy_intake = (intake_ben_energy *pl$benthic_fish[id] + 
                         intake_drift_energy * (1 - pl$benthic_fish[id])) * feeding_flag,
      net_energy = energy_intake - fish_met_j_per_day) %>% 
      # Remove the temportay columns
      select(!any_of(c( "shelter_fraction",
             "experienced_vel", "fish_met_j_per_day_active", "fish_met_j_per_day_passive",
             "cmax", "turbidity_fun", "detection_dist", "capture_area", "capture_success",
             "drift_eaten", "ben_eaten", "ben_avaiable", "intake_ben_energy",
             "intake_drift_energy")))
  }
# browser()
# 
# 
# tic()
#   # Correct for search feeding in low velocity water 
# 
#   test3 = calc_hab_and_feed(dl$df$full_habitat, 0) %>% 
#     bind_rows(calc_hab_and_feed(.,1/4*max_swim_speed)) %>% 
#     bind_rows(calc_hab_and_feed(.,1/4*max_swim_speed)) %>%
#     bind_rows(calc_hab_and_feed(.,1/4*max_swim_speed)) %>% 
#     group_by(dist, lat_dist, date) %>% 
#     filter(net_energy == max(net_energy)) %>% 
#     ungroup()
#   gc()
#   toc()
#   
#   tic()
  
  test3 = calc_hab_and_feed(dl$df$full_habitat, 0)
  dl$df$full_habitat =seq(1/4*max_swim_speed, 3/4*max_swim_speed, length.out = 4) %>% 
    map_df(~calc_hab_and_feed(test3, .x)) %>% 
    bind_rows(test3) %>% 
    group_by(dist, lat_dist, date) %>% 
    filter(net_energy == max(net_energy)) %>% 
    ungroup()
  gc()
# toc()

# tic()
# # Correct for search feeding in low velocity water 
# 
#   habitat3 =seq(0.0, 3/4*max_swim_speed, length.out = 4) %>% 
#     map_df(~calc_hab_and_feed(dl$df$full_habitat, .x)) %>% 
#     group_by(dist, lat_dist, date) %>% 
#     filter(net_energy == max(net_energy)) %>% 
#     ungroup()
# gc()
# toc()
  
  average_map_full = dl$df$full_habitat %>% 
    select(-date) %>% 
    group_by(lat_dist, dist, geometry) %>% 
    summarise_all(list(~mean(., na.rm = TRUE))) %>%
    st_as_sf() %>%
    ungroup() %>%
    mutate(below_d_cutoff = ifelse(depth < dl$df$habitat_parms$dep_cutoff, 1, 0) ,
           below_v_cutoff = ifelse(velocity < dl$df$habitat_parms$vel_cutoff, 1, 0),
           below_group = below_d_cutoff + 10*below_v_cutoff)

  average_map = dl$df$full_habitat %>% 
    filter(aoi == 1) %>% 
    select(-date) %>% 
    group_by(lat_dist, dist, geometry) %>% 
    summarise_all(list(~mean(., na.rm = TRUE))) %>% 
    st_as_sf() %>% 
    ungroup() %>% 
    mutate(below_d_cutoff = ifelse(depth < dl$df$habitat_parms$dep_cutoff, 1, 0) ,
           below_v_cutoff = ifelse(velocity < dl$df$habitat_parms$vel_cutoff, 1, 0),
           below_group = below_d_cutoff + 10*below_v_cutoff) 

  # Make the average daily data 
  average_day_full = dl$df$full_habitat %>%
    mutate(total_cover = wetted_area * cover_fra) %>%
    st_drop_geometry() %>% 
    select(-geometry) %>% 
    group_by(date) %>% 
    summarise_all(list(~mean(., na.rm = TRUE))) %>% 
    ungroup() %>%
    left_join(select(dl$df$daily_input, date, flow_cms), by = "date")
  
  average_day = dl$df$full_habitat %>%
    st_drop_geometry() %>% 
    select(-geometry) %>% 
    filter(aoi == 1) %>% 
    mutate(total_cover = wetted_area * cover_fra) %>% 
    group_by(date) %>% 
    summarise_all(list(~mean(., na.rm = TRUE))) %>% 
    ungroup() %>% 
    left_join(select(dl$df$daily_input, date, flow_cms), by = "date")

  # Remove the habitat file and clean up 
  return(list(map = average_map,
              day =  average_day,
              map_full = average_map_full,
              day_full =  average_day_full,
              lifestage = ls,
              species = pl$specie[id]))
}


##### Put results in Bins #####
get_bined_results = function(df = NULL, 
                             column = NULL,
                             name = NULL,
                             bin_count = 4){

  df_bare = st_drop_geometry(df)
  total_area = sum(df_bare$wetted_area, na.rm = TRUE)
  bins = seq(0,
             max(select(df_bare, {{column}}), na.rm = TRUE),
             length.out = bin_count)
 
  
  result = df_bare %>%
    group_by(name = cut({{column}}, breaks = bins)) %>%
    summarise(area = round(sum(wetted_area),2),
              percent_area = round(sum(wetted_area)/total_area * 100,3)) %>% 
    na.omit()
  
  return(result)
}

##### do the predator calculations #####
calc_all_preds = function(p_id, dl, fish_length){

  pred_habitat = dl$df$full_habitat
  # Get the pred and prey length
  pred_length = exp(dl$df$pred_parm$pred_length_mean[[p_id]])
  prey_length = exp(dl$df$pred_parm$gape_a[[p_id]] +
                      dl$df$pred_parm$gape_b[[p_id]] * pred_length^2)
  # Check if it is vulnerable to predation
  length_pred_bonous = ifelse(fish_length >= prey_length, 0, 1)
  pred_habitat = pred_habitat %>% 
    mutate(shaded = ifelse(shade > 0.5, 1, 0),
           substrate = rowSums(across(gravel:rock)),
           # if rocky substrate is the majority in a cell, then 1, else 0
           substrate = if_else(substrate >= fine & substrate > 0, 1, 0),
           # Calculate the predation function
           input = dl$df$pred_parm$pred_glm_int[[p_id]] +
             dl$df$pred_parm$pred_glm_shade[[p_id]] * shaded +
             dl$df$pred_parm$pred_glm_veg[[p_id]] * veg +
             dl$df$pred_parm$pred_glm_wood[[p_id]] * wood +
             dl$df$pred_parm$pred_glm_depth[[p_id]] * depth +
             dl$df$pred_parm$pred_glm_velocity[[p_id]] * velocity +
             dl$df$pred_parm$pred_glm_substrate[[p_id]] * substrate,
           # Calculate the habitat rating
           hab_rating = 1 / (1 + exp(-input)) *
             ifelse(wetted_area > 0, 1, 0)) %>% 
    group_by(date) %>% 
    mutate(# Place predators
      predators = replace_na(round((hab_rating * wetted_area) /
                                     sum(hab_rating * wetted_area) *
                                     reach_preds), 0)) %>% 
    ungroup() %>% 
    mutate(# Calculate the temp effect 
      temp_effect = 1 / (1 + exp(-(temp* dl$df$pred_parm$area_pred_b[[p_id]] +
                                     dl$df$pred_parm$area_pred_a[[p_id]]))),
      # Calculate the fraction of area the predators occupy
      porp_area = pmin(predators * (ml$df$habitat_parms$reaction_distance *
                                      ml$df$habitat_parms$t_area_effect * temp_effect) / (wetted_area),
                       predators),
      # calculate the distance to cover
      dis_to_cover_m = pmax(sqrt(area) * (ml$df$habitat_parms$int_pct_cover +
                                            ml$df$habitat_parms$sqrt_pct_cover * sqrt(cover_fra) +
                                            ml$df$habitat_parms$pct_cover * cover_fra +
                                            ml$df$habitat_parms$sqrt_pct_cover_x_pct_cover * cover_fra ^ 1.5),
                            0),
      # Calculate the survival bonuses 
      survival_bonus = 1/(1+exp(-(ml$df$habitat_parms$dis_to_cover_int +
                                    ml$df$habitat_parms$dis_to_cover_m * dis_to_cover_m))),
      turb_bonus = 1 / (1 + exp(-1 *(ml$df$habitat_parms$turbidity_int +
                                       turb * ml$df$habitat_parms$turbidity_slope))),
      survival_prob = 1 - (1 - survival_bonus) * (1 - turb_bonus),
      # Calculate the predation risk and include the length bonus
      pred_mort_risk = if_else(porp_area > 1,
                               1 - (survival_prob ^ porp_area),
                               porp_area * (1 - survival_prob)) * length_pred_bonous) %>% 
    # Remove temporary columns
    select(hab_rating, pred_mort_risk) %>% 
    rename_with( ~ paste0(.x, paste0("_" , p_id)))
}

##### Make summary statistics #####
make_summary_stats = function(df, day_df, value_name){
  output = data.frame(cover_area_m2 = sum(df$cover_fra * df$wetted_area)) %>%
    mutate(near_shore_cover_area_m2 = sum(df$wetted_area *
                                            (df$area > df$wetted_area) *
                                            df$cover_fra),
           near_shore_cover_area_below_v_m2 = sum(df$wetted_area *
                                                    (df$velocity < ml$df$habitat_parms$vel_cutoff) *
                                                    (df$area > df$wetted_area) *
                                                    df$cover_fra),
           percent_near_shore_area = sum(df$wetted_area *
                                           (df$area > df$wetted_area))/
             sum(df$wetted_area) * 100,
           CBC_percent = sum((df$cover_fra) * df$wetted_area *
                               (df$depth < ml$df$habitat_parms$dep_cutoff) *
                               (df$velocity < ml$df$habitat_parms$vel_cutoff)) /
             sum(df$wetted_area) * 100,
           average_cover_percent = sum((df$cover_fra) * df$wetted_area) /
             sum(df$wetted_area) * 100,
           max_wetted_area_m2 = max(day_df$wetted_area),
           min_wetted_area_m2 = min(day_df$wetted_area),
           full_inundation_days = NROW(filter(day_df, wetted == 1))) %>%
    pivot_longer(cols = everything(), names_to = "Item", values_to = "Value") %>% 
    mutate(Item = str_replace_all(Item, c("-" = " ", "_" = " ")),
           Item = str_replace_all(Item, "m2", "(m^2)"),
           Value = round(Value,2)) %>% 
    rename({{value_name}} := Value)
}

##### Make summary statistics woith cutoffs #####
make_summary_stats_cutoff = function(df){
  output =  data.frame(percent_area_below_no_cutoffs =
                                       sum((df$below_group == 0) *
                                             df$wetted_area) /
                                       sum(df$wetted_area) * 100) %>% 
    mutate(percent_area_below_v_cutoff = sum((df$below_group == 10) *
                                               df$wetted_area) /
             sum(df$wetted_area) * 100,
           percent_area_below_d_cutoff = sum((df$below_group == 1) *
                                               df$wetted_area) /
             sum(df$wetted_area) * 100,
           percent_area_below_both_cutoffs = sum((df$below_group == 11) *
                                                   df$wetted_area) /
             sum(df$wetted_area) * 100,
           area_below_no_cutoffs = sum((df$below_group == 0) *
                                         df$wetted_area),
           area_below_v_cutoff = sum((df$below_group == 10) *
                                       df$wetted_area),
           area_below_d_cutoff = sum((df$below_group == 1) *
                                       df$wetted_area),
           area_below_both_cutoffs = sum((df$below_group == 11) *
                                           df$wetted_area),
           mean_cover_below_no_cutoffs = sum((df$below_group == 0) *
                                               df$cover_fra *
                                               df$wetted_area)/
             sum((df$below_group == 0) * df$wetted_area),
           mean_cover_below_v_cutoff = sum((df$below_group == 10) *
                                             df$cover_fra *
                                             df$wetted_area)/
             sum((df$below_group == 0) * df$wetted_area),
           mean_cover_below_d_cutoff = sum((df$below_group == 1) *
                                             df$cover_fra *
                                             df$wetted_area)/
             sum((df$below_group == 0) * df$wetted_area),
           mean_cover_below_both_cutoffs = sum((df$below_group == 11) *
                                                 df$cover_fra *
                                                 df$wetted_area)/
             sum((df$below_group == 0) * df$wetted_area))  %>%
    pivot_longer(cols = everything(), names_to = "Item", values_to = "Value") %>% 
    mutate(V_Cutoff = ifelse(str_detect(Item, "_v_") | str_detect(Item, "both"),
                             "Below V", "Above V"),
           D_Cutoff = ifelse(str_detect(Item, "_d_") | str_detect(Item, "both"),
                             "Below D", "Above D"),
           Item = str_remove(Item, pattern = "_below.*"),
           Item = str_replace(Item, "_", " "),
           Value = round(Value,3)) %>% 
    relocate(matches("Item", "D_Cutoff")) %>% 
    pivot_wider(names_from = V_Cutoff, values_from = Value) %>% 
    arrange(Item, D_Cutoff) %>% 
    rename(" " = D_Cutoff)
}

##### Pluck list from 1 level deep #####
deep_pluck = function(list, name){
  output = seq(1, length(list)) %>% 
    map(~list[[.x]][[name]]) %>%
    setNames(names(list) )
}

################################################################################
# End
################################################################################