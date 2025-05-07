################################################################################
# This script loads all functions to help parameter conversion
################################################################################

# Adds some additional parameters to the fish_parms list for madult migration
calculate_adult_parameters <- function(fish_parms){
  num_species <- length(fish_parms$specie)
  fish_parm_lol <- map(1:num_species, ~ map(fish_parms, .x))
  fish_parms[["fish_mass_g"]] <- map_dbl(fish_parm_lol, get_fish_body_mass)
  fish_parms[["swim_speed_max_m_per_s"]] <- map_dbl(fish_parm_lol, get_max_swim_speed)
  return(fish_parms)
}

# Calculates the parameters need to estimate the optimal swim speed curve 
get_swim_speed_model_params <- function(fish_parms, fish_index){

  fish_length <- fish_parms$eg_adult_length[fish_index]
  fish_mass <- fish_parms$fish_mass_g[fish_index]
  swim_speed_max <- fish_parms$swim_speed_max_m_per_s[fish_index]
  
  dt <- make_environment_dt(swim_speed_max) %>% 
    .[, ucrit := get_ucrit(fish_parms, fish_index, temperature)]
  dt$swim_speed_martin <- pmap_dbl(list(dt$velocity, dt$temperature, dt$ucrit), 
                                   ~ optimize(get_cost_of_travel, 
                                              interval =  c(..1 + 1e-6, swim_speed_max), 
                                              water_velocity_m_per_s = ..1, 
                                              fish_parms = fish_parms,
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
  
  list(max_water_vel_m_per_s = water_velocity_at_max_burst,
       ucrit_cutoff_m_per_s = ucrit_cutoff,
       pars_min_water_vel_ucrit_int = parameters_for_min_water_velocity_at_ucrit[[1]],
       pars_min_water_vel_ucrit_slope = parameters_for_min_water_velocity_at_ucrit[[2]],
       pars_max_water_vel_ucrit_int = parameters_for_max_water_velocity_at_ucrit[[1]],
       pars_max_water_vel_ucrit_slope = parameters_for_max_water_velocity_at_ucrit[[2]])
}

# Runs through the main swim speed param function for all species 
get_swim_speed_parameters_for_all_species <- function(fish_parms){
  fish_ids <- 1:length(fish_parms$specie)
  future_map(fish_ids, 
             get_swim_speed_model_params, 
             fish_parms = fish_parms) %>% 
    pmap(c)
}

# Makes a simulated environment with different temp and water velocity
make_environment_dt <- function(swim_speed_max){
  
  CJ(temperature = seq(1,25,1),
     velocity = seq(0, swim_speed_max, swim_speed_max/50))
}

# Martin et al. model of movement cost vs. distance 
get_cost_of_travel <- function(swim_speed_m_per_s, 
                               water_velocity_m_per_s, 
                               ucrit_m_per_s,
                               fish_parms,
                               fish_index,
                               temperature_C,
                               ratio) {
  
  anaerobic_fuel_recovery_parameter <- 1.82
  length = fish_parms$eg_adult_length[fish_index] 
  seconds_per_day <- 86400
  
  base_metabolic_rate <- calc_met(fish_parms,
                                  fish_index,
                                  length,
                                  temperature_C,
                                  0)/seconds_per_day

  critical_metabolic_rate <- calc_met(fish_parms,
                                      fish_index,
                                      length,
                                      temperature_C,
                                      ucrit_m_per_s)/seconds_per_day

  total_metabolic_rate <- calc_met(fish_parms,
                                   fish_index,
                                   length,
                                   temperature_C,
                                   swim_speed_m_per_s)/seconds_per_day

  (total_metabolic_rate + # aerobic component
      base_metabolic_rate * pmax(0, anaerobic_fuel_recovery_parameter * (total_metabolic_rate - critical_metabolic_rate) / (critical_metabolic_rate - base_metabolic_rate)) + # energy spent due to waiting to recover from anerobic activity
      pmax(0, (anaerobic_fuel_recovery_parameter - 1) * (total_metabolic_rate - critical_metabolic_rate))) / # cost of recovering fuel after anerobic activity
    (ratio * swim_speed_m_per_s - water_velocity_m_per_s)
}

################################################################################
# End 
################################################################################

