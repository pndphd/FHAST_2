################################################################################
# This script is the functions for the multi_run.R script
# It goes through and changes the input files to run the simulations and log the
# results automatically 
################################################################################

##### run_multi ################################################################
# The main function to run the FHAST models
run_multi = function(file_name,
                     variable_names,
                     variable_values){

  # file_name = "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_cs/michel_2015_1.csv"
  # variable_names = c("temperature predator area baseline",
  #                    "temperature predator area effect",
  #                    "pred_per_area",
  #                    "drift food density",
  #                    "wood",
  #                    "number",
  #                    "length",
  #                    "file") 
  # 
  # # List of the variable values you want to overwrite for each run
  # variable_values = c(0.18,
  #                     0.08,
  #                     0.03,
  #                     0.022,
  #                     0.05,
  #                     10000,
  #                     16.4,
  #                     "test.csv") 

  ##### Setup ##################################################################
  # The log to track input values
  input_log = data.frame(name = basename(file_name))
  
  ##### Main input file ########################################################
  # Read the main input file
  input_file = read.csv(file = file_name,
                        header = FALSE,
                        stringsAsFactors = FALSE) %>%
    rename(variable = 1, path = 2) %>% 
    mutate(variable = str_replace(variable, " ", "_")) 
  
  # Make them a named list for easy access
  input_parameters = as.list(input_file$path) %>% 
    setNames(input_file$variable)
  
  ##### Variables ##############################################################
  # Make the variables into a data frame
  variable_df = data.frame(names = variable_names, values = variable_values) %>%
    pivot_wider(names_from = names, values_from = values)
  
  # Make them a named list for easy access
  variable_list = as.list(variable_values) %>% 
    setNames(variable_names)
  
  ##### Fish input file ########################################################
  # Read and change the fish population file
  fish_population_file = read.csv(file = here(dirname(file_name),
                                              input_parameters$fish_population))
  # Make a secure copy
  file.copy(from = here(dirname(file_name),
                        input_parameters$fish_population),
            to = here(dirname(file_name),
                      paste0(input_parameters$fish_population, "_backup")),
            overwrite = TRUE)
  
  # Update the data frame
  fish_population_tmp = fish_population_file %>%
    select(-intersect(variable_names, names(.)))
  fish_population_new = variable_df %>% 
    select(intersect(variable_names, names(fish_population_file))) %>% 
    bind_cols(fish_population_tmp) 

  # Add to the log of inputs
  input_log = input_log %>% 
    bind_cols(fish_population_new) %>% 
    rename(fish_length = length,
           fish_count = number,
           fish_enter_date = date,
           fish_lenght_sd = sd,
           fish_interquartile = interquartile)
  
  # Write a back up csv
  write.csv(fish_population_new,
            file = here(dirname(file_name),
                        input_parameters$fish_population),
            row.names = FALSE)
  
  # Write the new csv
  write.csv(fish_population_new,
            file = here(dirname(file_name),
                        input_parameters$fish_population),
            row.names = FALSE)
  
  ##### Daily input file #######################################################
  # Read in the input file
  daily_input_file = read.csv(file = here(dirname(file_name),
                                          input_parameters$daily_conditions)) %>% 
    mutate(type = trimws(type, which = "both"))
  
  # Make a secure copy
  file.copy(from = here(dirname(file_name),
                        input_parameters$daily_conditions),
            to = here(dirname(file_name),
                      paste0(input_parameters$daily_conditions, "_backup")),
            overwrite = TRUE)
  
  if("file" %in% variable_names){
    message("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") 
    message("WARNING: Replaceing Hydrograph File.")
    message("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
    # Replace the variable
    daily_input_new = daily_input_file %>%
      mutate(hydrograph = ifelse(type == "file",
                                 variable_list$file,
                                 hydrograph ))
    
    # Write the new csv
    write.csv(daily_input_new,
              file = here(dirname(file_name),
                          input_parameters$daily_conditions),
              row.names = FALSE)
    
    # Add to the input log
    input_log = input_log %>% 
      bind_cols(pivot_wider(daily_input_new,
                            names_from = type,
                            values_from = hydrograph))
  } else {
    # Add to the input log
    input_log = input_log %>% 
      bind_cols(pivot_wider(daily_input_file,
                            names_from = type,
                            values_from = hydrograph))
  }
  
  # Rename input_log columns
  input_log = input_log %>% 
    rename(hydrograph_file = file,
           hydrograph_start = "start date",
           hydrograph_end = "end date")
  
  ##### Habitat Parameters ########################################################
  #Read in the file
  habitat_parameters_file = read.csv(file = here(dirname(file_name),
                                          input_parameters$habitat_parameters),
                                     header = FALSE) %>%
    rename(variable = 1, value = 2) %>% 
    mutate(variable = trimws(variable, which = "both"))
  
  # Make a secure copy
  file.copy(from = here(dirname(file_name),
                        input_parameters$habitat_parameters),
            to = here(dirname(file_name),
                      paste0(input_parameters$habitat_parameters, "_backup")),
            overwrite = TRUE)
  
  # Switch out variables
  habitat_parameters_new = seq(1,NROW(habitat_parameters_file)) %>% 
    map_df(~habitat_parameters_file[.x,] %>% 
             mutate(value = ifelse(variable %in% variable_names,
                                   as.character(variable_values[which(variable_names == variable)]),
                                   as.character(value))))
  
  # Update input log 
  input_log = input_log %>%
    bind_cols(pivot_wider(habitat_parameters_new,
                          names_from = variable,
                          values_from = value)) %>%
  rename_with(~str_replace_all(.x, " ","_"), contains(" "))
  
  # Write the new csv
  write.table(habitat_parameters_new,
            file = here(dirname(file_name),
                        input_parameters$habitat_parameters),
            row.names = FALSE,
            col.names = FALSE,
            sep = ",")
    
  ##### Interaction Parameters #################################################
  #Read in the file
  interaction_parameters_file = read.csv(file = here(dirname(file_name),
                                                 input_parameters$interaction_parameters),
                                     header = FALSE) %>%
    rename(variable = 1, value = 2) %>% 
    mutate(variable = trimws(variable, which = "both"))
  
  # Make a secure copy
  file.copy(from = here(dirname(file_name),
                        input_parameters$interaction_parameters),
            to = here(dirname(file_name),
                      paste0(input_parameters$interaction_parameters, "_backup")),
            overwrite = TRUE)
  
  # Switch out variables
  interaction_parameters_new = seq(1,NROW(interaction_parameters_file)) %>% 
    map_df(~interaction_parameters_file[.x,] %>% 
             mutate(value = ifelse(variable %in% variable_names,
                                   as.numeric(variable_values[which(variable_names == variable)]),
                                   value)))
  
  # Update input log 
  input_log = input_log %>%
    bind_cols(pivot_wider(interaction_parameters_new,
                          names_from = variable,
                          values_from = value)) %>%
    rename_with(~str_replace_all(.x, " ","_"), contains(" "))
  
  # Write the new csv
  write.table(interaction_parameters_new,
              file = here(dirname(file_name),
                          input_parameters$interaction_parameters),
              row.names = FALSE,
              col.names = FALSE,
              sep = ",")
  
  ##### Predator Parameters #################################################
  # Read in the file
  predator_parameters_file = read.csv(file = here(dirname(file_name),
                                                     input_parameters$predator_parameters)) %>%
    mutate(species = trimws(species, which = "both"))
  
  # Make a secure copy
  file.copy(from = here(dirname(file_name),
                        input_parameters$predator_parameters),
            to = here(dirname(file_name),
                      paste0(input_parameters$predator_parameters, "_backup")),
            overwrite = TRUE)
  
  # Switch out variables
  predator_parameters_long = predator_parameters_file %>% 
    pivot_longer(cols = -species)
  predator_parameters_new = seq(1,NROW(predator_parameters_long)) %>% 
    map_df(~predator_parameters_long[.x,] %>% 
             mutate(value = ifelse(species %in% variable_names,
                                   as.numeric(variable_values[which(variable_names == species)]),
                                   value))) %>% 
    pivot_wider(names_from = "name", values_from = "value")
  
  # Update input log 
  input_log = input_log %>%
    bind_cols(pivot_wider(predator_parameters_new[,1:2],
                          names_from = species,
                          values_from = 2)) %>%
    rename_with(~str_replace_all(.x, " ","_"), contains(" "))
  
  # Write the new csv
  write.table(predator_parameters_new,
              file = here(dirname(file_name),
                          input_parameters$predator_parameters),
              row.names = FALSE,
              sep = ",")
  
  ##### Wildcard Parameters #################################################
  # Read in the file
  wildcard_file = read.csv(file = here(dirname(file_name),
                                                  input_parameters$wildcard)) 
  
  # Make a secure copy
  file.copy(from = here(dirname(file_name),
                        input_parameters$wildcard),
            to = here(dirname(file_name),
                      paste0(input_parameters$wildcard, "_backup")),
            overwrite = TRUE)
  
  # Switch out variables
  wildcard_long = wildcard_file %>% 
    pivot_longer(cols = everything(), names_to = "variable", values_to = "value")
  wildcard_new = seq(1,NROW(wildcard_long)) %>% 
    map_df(~wildcard_long[.x,] %>% 
             mutate(value = ifelse(variable %in% variable_names,
                                   as.numeric(variable_values[which(variable_names == variable)]),
                                   value))) %>% 
    pivot_wider(names_from = "variable", values_from = "value")
  
  # Update input log 
  input_log = input_log %>%
    bind_cols(wildcard_new) %>%
    rename_with(~str_replace_all(.x, " ","_"), contains(" "))
  
  # Write the new csv
  write.table(wildcard_new,
              file = here(dirname(file_name),
                          input_parameters$wildcard),
              row.names = FALSE,
              sep = ",")
  
  ##### RUN THE MODEL ##########################################################
  pass_arguments <<- c(file_name, 0)
  source(here("scripts","main","run_all.R"))
  
  ##### Revert the input files #################################################
  
  # Fish file
  write.csv(fish_population_file,
            file = here(dirname(file_name),
                        input_parameters$fish_population),
            row.names = FALSE)
  
  # Delete the secure copy 
  file.remove(here(dirname(file_name),
                   paste0(input_parameters$fish_population, "_backup")))
  
  # Daily conditions
  write.csv(daily_input_file,
            file = here(dirname(file_name),
                        input_parameters$daily_conditions),
            row.names = FALSE)
  
  # Delete the secure copy 
  file.remove(here(dirname(file_name),
                   paste0(input_parameters$daily_conditions, "_backup")))
  
  # Habitat Parameters
  write.table(habitat_parameters_file,
            file = here(dirname(file_name),
                        input_parameters$habitat_parameters),
            row.names = FALSE,
            col.names = FALSE,
            sep = ",")
  
  # Delete the secure copy 
  file.remove(here(dirname(file_name),
       paste0(input_parameters$habitat_parameters, "_backup")))
  
  # Interactions Parameters
  write.table(interaction_parameters_file,
              file = here(dirname(file_name),
                          input_parameters$interaction_parameters),
              row.names = FALSE,
              col.names = FALSE,
              sep = ",")

  # Delete the secure copy 
  file.remove(here(dirname(file_name),
                   paste0(input_parameters$interaction_parameters, "_backup")))
  
  # Predator Parameters
  write.table(predator_parameters_file,
              file = here(dirname(file_name),
                          input_parameters$predator_parameters),
              row.names = FALSE,
              col.names = TRUE,
              sep = ",")
  
  # Delete the secure copy 
  file.remove(here(dirname(file_name),
                   paste0(input_parameters$predator_parameters, "_backup")))
  
  # Wildcard
  write.table(wildcard_file,
              file = here(dirname(file_name),
                          input_parameters$wildcard),
              row.names = FALSE,
              sep = ",")
  
  # Delete the secure copy 
  file.remove(here(dirname(file_name),
                   paste0(input_parameters$wildcard, "_backup")))
  
  return(input_log)
}

##### Functions to process runs ################################################
get_survival = function(name, add, file, column, fish_input){
  #name = str_sub(name, 4, -1)
  new_name = paste0(str_sub(name, 1, -5), add, "/", file)
  data = read.csv(new_name)
  output = data.frame(name = basename(name),
                      modeled_survival = 1-sum(select(data, contains(column)))/fish_input)
}

get_temperature = function(name, add, file, column, fish_input){
  #name = str_sub(name, 4, -1)
  new_name = paste0(str_sub(name, 1, -5), add, "/", file)
  data = read.csv(new_name) %>%
    mutate(temp_c = as.numeric(temp_c))
  output = data.frame(name = basename(name),
                      modeled_temperature = colMeans(select(data, contains(column))))
}

get_growth = function(name, add, file, column_1, column_2, fish_input){
  #name = str_sub(name, 4, -1)
  new_name = paste0(str_sub(name, 1, -5), add, "/", file)
  data = read.csv(new_name) %>%
    mutate(growth = as.numeric(mean_rearing_growth_length),
           rearers = as.numeric(rearers),
           weighted = growth * rearers) %>%
    summarise(rearers = sum(rearers),
            weight = sum(weighted)) %>%
    mutate(growth_rate = weight/rearers)
  output = data.frame(name =basename(name),
                      g_value = data$growth_rate)
}

################################################################################
# END
################################################################################
