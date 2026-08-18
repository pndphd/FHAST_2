################################################################################
# This script runs multiple FHAST runs 
################################################################################

##### Inputs ###################################################################
# Enter your output file
# This is a CSV file to which this script will append your results 
output_file = "../../../calibration/sacramento_above_ar_con_cs/compare.csv"
input_file = "../../../calibration/sacramento_above_ar_con_cs/input_files_list.csv"

# Do you want to write the outputs
write = TRUE

# Do you want to run FAHST 
# (FALSE will just read in existing outputs and do post processing)
run = TRUE

# List of the variable you want to overwrite for each run
# They will not be over ridden in the input file permanently, just for this run
variable_names = c("temperature predator area baseline",
                   "temperature predator area effect",
                   "pred_per_area",
                   "drift food density",
                   "wood",
                   "number")

# List of the variable values you want to overwrite for each run
variable_values = c(0.18,
                    0.08,
                    0.003,
                    0.022,
                    0.05,
                    10000)

##### Load Libraries and color pallet ##########################################
source("developer_scripts/load_libraries_ect.R")
source("developer_scripts/multi_run_functions.R")

##### Load the files paths #####################################################
file_names = read.csv(input_file) %>% 
  mutate(path = trimws(path, which = "both"))

##### Run the model ############################################################
if (run){
  input_log = map_dfr(file_names$path,
                      ~run_multi(file_name = .x,
                                 variable_names = variable_names,
                                 variable_values = variable_values))
}

##### Analyze the Data #########################################################
# Get the survival data form the ABM results
survival_data = map_df(file_names$path, ~get_survival(.x,
                                                 add = "_outputs",
                                                 file = "abm_detailed_pop_output.csv",
                                                 column = "dead_fish",
                                                 fish_input = 10000))

# Get the temperature data 
temp_data = map_df(file_names$path, ~get_temperature(.x,
                                                add = "_outputs",
                                                file = "daily_input_file.csv",
                                                column = "temp_c",
                                                fish_input = 10000))

#Get the growth data 
growth_data = map_df(file_names$path, ~get_growth(.x,
                                                add = "_outputs",
                                                file = "abm_detailed_pop_output.csv",
                                                column_1 = "mean_rearing_growth_length",
                                                column_2 = "rearers",
                                                fish_input = 10000))

# Join all and add a time stamp
compare = file_names %>% 
  mutate(name = basename(path)) %>% 
  select(-path) %>% 
  left_join(input_log, by = "name") %>% 
  left_join(temp_data, by = "name") %>%
  left_join(survival_data, by = "name") %>%
  left_join(growth_data, by = "name") %>%
  mutate(time_stamp = str_replace(Sys.time(), " ", "_"))

##### Write the Output #########################################################
if (write) {
  if (file.exists(output_file)){
    file.copy(output_file,
              str_replace(output_file, ".csv", "_old.csv"))

    # Give the run a number
    run = max(read.csv(output_file)$run) + 1
    compare = mutate(compare, run = run)

    #Append the data
    write.table(x = compare,
                file = output_file,
                sep = ",",
                col.names = FALSE,
                row.names = FALSE,
                append = TRUE)
  }else {
    # Make a new compare file
    compare = mutate(compare, run = 1)
    write.table(x = compare,
                file = output_file,
                sep = ",",
                row.names = FALSE)
  }
}

##### Make Plots ###############################################################
data_base = read.csv(output_file)
old_data = read.csv(here(dirname(output_file), "compare_pre_update.csv" )) %>% 
  filter(best == 1)

summary = data_base %>%
  mutate(percent_diff = abs(modeled_survival - field_survival)/field_survival) %>%
  group_by(run) %>%
  summarise(percent_diff = mean(percent_diff, na.rm = T))

slopes = data_base %>%
  group_by(run) %>%
  nest() %>%
  mutate(model = map(data, ~lm(modeled_survival ~ field_survival, data = .x) %>%
                       tidy)) %>%
  unnest(model) %>%
  filter(term == 'field_survival')

# Plot survial vs temp

# Plot the 1:1 survival plot
plot = ggplot(data_base ,
              aes(x = field_survival,
                  y = modeled_survival,
                  # color = modeled_temperature)) +
                   color = factor(run))) +
  theme_classic() +
  geom_abline(intercept = 0, slope = 1) +
  coord_cartesian(xlim = c(0,1), ylim = c(0,1))+
  geom_point(size = 4, shape = 1) +
  geom_point(data = old_data, aes(x = field_data , y = d_value), shape = 4)+
  coord_cartesian(xlim = c(0.5, 1), ylim = c(0.5, 1)) +
  # scale_color_viridis_c() +
  labs(x = "Filed Survival",
       y = "Model Survival")
print(plot)

##### END ######################################################################
