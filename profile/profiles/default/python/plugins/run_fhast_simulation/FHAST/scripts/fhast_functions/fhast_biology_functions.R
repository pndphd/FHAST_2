########################################
# This is a set of functions commonly
# used in FHAST for biology stuff
########################################

# Get the fish body mass
get_fish_body_mass <- function(params) {
  a <- params$length_mass_a
  b <- params$length_mass_b
  a * params$eg_adult_length^b
}

# Calculate max sustanind swimm speed
get_ucrit <- function(params, fish_index, temperature_C) {
  # ucrit in body lengths per second
  a <- params$ucrit_a[fish_index]
  b <- params$ucrit_b[fish_index]
  c <- params$ucrit_c[fish_index]
  d <- params$ucrit_d[fish_index]
  
  ucrit_in_body_lengths <- 
    (a / params$eg_adult_length[fish_index] + b) *
    (1 + (c - temperature_C) / (c - d)) * ((temperature_C / c)^(c / (c - d)))
  
  m_per_cm <- 0.01
  # ucrit in m per second; body length is in cm
  ucrit_in_body_lengths *  params$eg_adult_length[fish_index] * m_per_cm
}

# Calculate thet max swimm speed
get_max_swim_speed <- function(params) {
  m_per_cm <- 0.01
  body_length_m <- params$eg_adult_length * m_per_cm
  0.4 + 7.4 * body_length_m
}

# this function calculates a fishes metabolic cost
calc_met <- function(params = NULL,
                     fish_index = NULL,
                     length = NULL,
                     temp = NULL,
                     velocity = NULL){

    fish_mass = params$length_mass_a[fish_index] *
    length^params$length_mass_b[fish_index]
  
  fish_met_log = params$met_int[fish_index] +
    params$met_lm[fish_index] * log(fish_mass) +
    params$met_lt[fish_index] * log(temp) +
    # velocity is in body lengths/sec
    params$met_v[fish_index] * velocity  +
    params$met_lm_lt[fish_index] * log(fish_mass) * log(temp) +
    params$met_t[fish_index] * temp +
    params$met_lm_t[fish_index] * log(fish_mass) * temp +
    params$met_sqv[fish_index] * sqrt(velocity)
    
  
  fish_met_j_per_day = exp(fish_met_log)
  
  return(fish_met_j_per_day)
}
