########################################
# This is a set of functions commonly
# used in FHAST for maths
########################################
# calculate the logistic function in the style of inSALMO
convert_logistic_parameters <- function(parm_10, parm_90){
  parm_10 <- as.numeric(parm_10)
  parm_90 <- as.numeric(parm_90)
  log_d <- log(0.9/0.1)
  log_c <- log(0.1/0.9)
  log_b <- (log_c - log_d)/(parm_10 - parm_90)
  log_a <-  log_c - (log_b * parm_10)
  list(log_a = log_a,
       log_b = log_b)
}

# calculate the logistic Values
calc_logistic <- function(parm_10 = NULL,
                          parm_90 = NULL,
                          value = NULL){
  logistic_params <- convert_logistic_parameters(parm_10, parm_90)
  z = logistic_params$log_a + (logistic_params$log_b * value)
  s = exp(z)/(1 + exp(z))
  return(s)
}

# calculate the beta Sigmofish_index functionO
calc_beta_sig <- function(parm_A = NULL,
                          parm_B = NULL,
                          temp = NULL){
  
  s = (1 + (parm_A - temp)/(parm_A - parm_B)) *
    (temp/parm_A)^(parm_A / (parm_A - parm_B))
  
  return(s)
}

get_estimate_for_linear_model <- function(intercept, slope, x){
  intercept + slope * x
}