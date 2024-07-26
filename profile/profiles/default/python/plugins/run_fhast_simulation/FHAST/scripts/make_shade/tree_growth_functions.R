########################################
# This program takes in a shade shape alters it if we are 
# doing a run in future with tree growth
########################################


grow_tree <- function(height_m = NULL,
                      species_in = NULL,
                      time = NULL,
                      growth_parms = tree_growth_parms){

  height_cm = height_m * 100
  
  # Make everything lowercase
  species_in = str_to_lower(species_in)
  growth_parms = growth_parms %>% 
    mutate(species = str_to_lower(species))
  
  # select the species or use default
  if (species_in %in% growth_parms$species) {
    pars = growth_parms %>% 
      filter(species == species_in )
  } else {
    # check if a default is provided
    if(!("default" %in% growth_parms$species)){
      stop("No species match from canopy shape file and
           no default parameter set provided in the tree growth input file.")
    }
    pars = growth_parms %>% 
      filter(species == "default" )
  }

  # Make some conversion parameters
  b2 <- 2*(pars$h_max-137)/pars$d_max
  b3 <- (pars$h_max-137)/pars$d_max^2
 
  # Calculate the initial DBH
  dbh_0 <- (b2 - sqrt(b2^2 - 4 * b3 * (height_cm - 137))) / (2 * b3)

  # Calculate the final result
  dbh_temp = dbh_0
  for(i in 1:time){
    dbh_temp <- dbh_temp + pars$g * dbh_temp * (1-dbh_temp*height_cm/pars$d_max/pars$h_max)/
      (274+2 * b2 * dbh_temp - 4 * b3 * dbh_temp^2)
  }
  dbh_f = dbh_temp 
  # Divide by 100 to cm to m
  height_f <- (137 + b2 * dbh_f - b3 * dbh_f^2)/100

  # Calculate start and end canopy diameters
  # Uses cm as input but returned meters (boooo)
  diameter_0 = find_diameter(dbh_0, pars)
  diameter_f = find_diameter(dbh_f, pars)
  
  # Get how much it moved laterally
  radius_increase = (diameter_f - diameter_0)/2
  
  # return and convert to m
  return(c(height_f, radius_increase))
}

find_diameter = function(dbh_in, parms_in){

 if(parms_in$eq_name == "lin"){
   diameter = parms_in$a + parms_in$b * dbh_in
  } else if (parms_in$eq_name == "quad"){
    diameter = parms_in$a + parms_in$b * dbh_in + parms_in$c * dbh_in^2
  } else if (parms_in$eq_name == "cub"){
    diameter = parms_in$a + parms_in$b * dbh_in + parms_in$c *dbh_in^2 + parms_in$d * dbh_in^3
  } else if (parms_in$eq_name == "loglogw3"){
    diameter = exp(parms_in$a + parms_in$b*log(log(dbh_in + 1)) + (dbh_in)*(parms_in$c/2))
  } else {
    stop("Missing dbh to canopy diameter equation in tree_growth_parameters.csv file.")
  }
}

grow_trees = function(shape = NULL,
                      parms = NULL,
                      years = NULL){
  
  # add in a species column if not present
  # this will default to the default parameters
  cols <- c(species = "none")
  if (years > 0){
    # Do the calculations
    new_canopy <- shape %>% 
      add_column(!!!cols[setdiff(names(cols), names(.))]) %>% 
      rowwise() %>% 
      mutate(new_height = grow_tree(height_m = height,
                                species = species,
                                time = years,
                                growth_parms = parms)[1],
             radius_increase = grow_tree(height_m = height,
                                         species = species,
                                         time = years,
                                         growth_parms = parms)[2]) %>% 
      mutate(height = new_height) %>% 
      st_buffer(dist = .$radius_increase) %>% 
      select(-radius_increase, -new_height, -species )
      return(new_canopy)
  } else {
    return(shape)
  }
  

  
}
