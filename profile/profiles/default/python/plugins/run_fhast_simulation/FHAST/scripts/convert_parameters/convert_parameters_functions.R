########################################
# This script loads all functions to help parametr conversion
########################################

# 2 Pivot functions
params_pivot_longer <- function(df) {
  df %>% 
    pivot_longer(cols = -term, names_to = "species", values_to = "estimate") %>% 
    select(species, term, estimate) %>% 
    arrange(species)
}

params_pivot_wider <- function(df) {
  df %>% 
    select(1:2) %>% 
    pivot_wider(names_from = term, values_from = pikeminnow)
}

write_rds_temp_folder <- function(df, filename) {
  write_rds(df, here(temp_folder,  filename))
}

select_model_param <- function(df, param) {
  df %>% 
    filter(name == param) %>% 
    pull(value) %>% as.numeric()
}

make_variables <- function(df, filename) {
  do.call("<<-",list(filename,df))
}

# adds some additional parameters to the fish_parm list for madult migration
calculate_adult_parameters <- function(fish_parm){
  num_species <- length(fish_parm$specie)
  fish_parm_lol <- map(1:num_species, ~ map(fish_parm, .x))
  fish_parm[["fish_mass_g"]] <- map_dbl(fish_parm_lol, get_fish_body_mass)
  fish_parm[["swim_speed_max_m_per_s"]] <- map_dbl(fish_parm_lol, get_max_swim_speed)
  return(fish_parm)
}

# calculates the parameters need to estimate the optimal swim speed curve 
get_swim_speed_model_params <- function(fish_parm, fish_index){

  #fish_parm <- map(fish_parm, ~.x[[fish_id]])
  fish_length <- fish_parm$eg_adult_length[fish_index]
  fish_mass <- fish_parm$fish_mass_g[fish_index]
  swim_speed_max <- fish_parm$swim_speed_max_m_per_s[fish_index]
  
  dt <- make_environment_dt(swim_speed_max) %>% 
    .[, ucrit := get_ucrit(fish_parm, fish_index, temperature)]
  dt$swim_speed_martin <- pmap_dbl(list(dt$velocity, dt$temperature, dt$ucrit), 
                                   ~ optimize(get_cost_of_travel, 
                                              interval =  c(..1 + 1e-6, swim_speed_max), 
                                              water_velocity_m_per_s = ..1, 
                                              fish_parm = fish_parm,
                                              fish_index = fish_index, 
                                              temperature_C = ..2, 
                                              ucrit_m_per_s = ..3,
                                              ratio = 1)$minimum)
  
  min_speeds <- dt[, .(min_speed = min(swim_speed_martin)), by = "temperature"]
  
  ucrit_cutoff <- min_speeds[dt, on = "temperature"] %>%
    .[min_speed == max(min_speed)] %>%
    .$min_speed %>%
    .[[1]]
  
  min_vel_ucrit <- dt[signif(swim_speed_martin,4) == signif(ucrit,4), .(min = min(velocity)), by = "temperature"]
  parameters_for_min_water_velocity_at_ucrit <- min_vel_ucrit[dt, on = "temperature", nomatch = 0] %>%
    .[, c("ucrit", "min")] %>%
    .[ucrit > ucrit_cutoff,] %>% 
    lm(min ~ ucrit, data = .) %>%
    .[[1]]
  
  max_vel_ucrit <- dt[signif(swim_speed_martin,4) == signif(ucrit,4), .(max = max(velocity)), by = "temperature"]
  
  water_velocity_at_max_burst <- dt[signif(swim_speed_martin,4) == signif(swim_speed_max, 4)] %>% 
    .$velocity %>% 
    min()
  
  parameters_for_max_water_velocity_at_ucrit <- max_vel_ucrit[dt, on = "temperature", nomatch = 0] %>%
    .[, c("ucrit", "max")] %>%
    lm(max ~ ucrit, data = .) %>%
    .[[1]]
  
  list(
    max_water_vel_m_per_s = water_velocity_at_max_burst,
    ucrit_cutoff_m_per_s = ucrit_cutoff,
    pars_min_water_vel_ucrit_int = parameters_for_min_water_velocity_at_ucrit[[1]],
    pars_min_water_vel_ucrit_slope = parameters_for_min_water_velocity_at_ucrit[[2]],
    pars_max_water_vel_ucrit_int = parameters_for_max_water_velocity_at_ucrit[[1]],
    pars_max_water_vel_ucrit_slope = parameters_for_max_water_velocity_at_ucrit[[2]]
  )
}

# runs through the main swim speed param function for all species 
get_swim_speed_parameters_for_all_species <- function(fish_parm){
  fish_ids <- 1:length(fish_parm$specie)
  future_map(fish_ids, 
             get_swim_speed_model_params, 
             fish_parm = fish_parm) %>% 
    pmap(c)
}

# makes a simulated environment with different temp and water velocity
make_environment_dt <- function(swim_speed_max){
  
  CJ(
    temperature = seq(1,25,1),
    velocity = seq(0, swim_speed_max, swim_speed_max/50))
}

# Martin et al. model of movement cost vs. distance 
get_cost_of_travel <- function(swim_speed_m_per_s, 
                               water_velocity_m_per_s, 
                               ucrit_m_per_s,
                               fish_parm,
                               fish_index,
                               temperature_C,
                               ratio) {
  
  anaerobic_fuel_recovery_parameter <- 1.82
  length = fish_parm$eg_adult_length[fish_index] 
  seconds_per_day <- 86400
  
  base_metabolic_rate <- calc_met(fish_parm,
                                  fish_index,
                                  length,
                                  temperature_C,
                                  0)/seconds_per_day

  critical_metabolic_rate <- calc_met(fish_parm,
                                      fish_index,
                                      length,
                                      temperature_C,
                                      ucrit_m_per_s)/seconds_per_day

  total_metabolic_rate <- calc_met(fish_parm,
                                   fish_index,
                                   length,
                                   temperature_C,
                                   swim_speed_m_per_s)/seconds_per_day

  (total_metabolic_rate + # aerobic component
      base_metabolic_rate * pmax(0, anaerobic_fuel_recovery_parameter * (total_metabolic_rate - critical_metabolic_rate) / (critical_metabolic_rate - base_metabolic_rate)) + # energy spent due to waiting to recover from anerobic activity
      pmax(0, (anaerobic_fuel_recovery_parameter - 1) * (total_metabolic_rate - critical_metabolic_rate))) / # cost of recovering fuel after anerobic activity
    (ratio * swim_speed_m_per_s - water_velocity_m_per_s)
}


