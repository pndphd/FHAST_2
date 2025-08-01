#################################################
# This script runs multiple FHAST runs 
#################################################

##### Inputs #####
# Enter your output file to amend on you computer 
output_file = "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/compare.csv"

# Do you want to write the outputs
write = TRUE

# Do you want to run FAHST (FHAST will just read in existing outputs and do post processing)
run = TRUE

# Write in the parameters you are using. they will be noted in the output file 
# The base area for predators
number	= 0.18
# the parameter for how temperature affects predation area 
area_effect = 0.08
# the density of predators
density = 0.003
# density of drift or search food (whatever you are comparing to)
food = 0.022
# a base level of wood for the wildcard shape
base_wood = 0.05
# the number of fish you are putting in
fish_number = 10000
# the lenghts 
length = rep(c(5,7),6)
  
##### Load Libraries ######
library(tidyverse)
library(here)
library(broom)

##### List the File names #####
# create the master list
ml = list()
# any of the below list you want to remove
remove = c(100)

# list of input files to run
file_names = c(
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/spawning_runs/input_data/configure_files/100_adults.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/spawning_runs/input_data/configure_files/1000_adults.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/spawning_runs/input_data/configure_files/10000_adults.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/spawning_runs/input_data/configure_files/50000_adults.txt"
)

# get the config file
config_file = read.csv(
  file = file_names[1],
  sep = ",",
  row.names = 1,
  header = FALSE) %>%
  # Trim off white spaces form values
  rename(value = 1) %>%
  mutate(value = str_trim(value, side = c("both")))

# get the output folder
output_folder = config_file["output path", ]

file_names = file_names[-remove]

##### Run the Sims #####
run_multi = function(file_name){
  config_file_name <<- file_name
  source(here("scripts","main","run_all.R"))
}

if (run){
  walk(file_names, ~run_multi(.x))
}


##### Functions to process runs ######
get_redd_d_and_v = function(name, file){
  new_name = paste0(output_folder, "/", str_sub(basename(name), 1, -5), "_outputs/temporary/", file)
  data = read.csv(new_name, skip = 1) %>% 
    filter(event == "spawn") %>% 
    select(species, velocity, depth) %>% 
    mutate(run_name = str_sub(basename(name), 1, -5))
  output = data
}

get_super_imp = function(name, file){
  new_name = paste0(output_folder, "/", str_sub(basename(name), 1, -5), "_outputs/temporary/", file)
  data = read.csv(new_name, skip = 1) %>% 
    group_by("Species") %>% 
    filter(time == max(time)) %>% 
    ungroup() %>% 
    select(Species, dead_eggs, total_redds, total_alive_eggs) %>% 
    mutate(run_name = str_sub(basename(name), 1, -5),
           fraction_dead = dead_eggs/(total_alive_eggs + dead_eggs) )
  output = data
}

get_temperature = function(name, add, file, column, fish_input){
  #name = str_sub(name, 4, -1)
  new_name = paste0(str_sub(name, 1, -5), add, "/", file)
  data = read.csv(new_name) %>% 
    mutate(temp_c = as.numeric(temp_c))
  output = data.frame(name =str_sub(name, 1, -5),
                      t_value = colMeans(select(data, contains(column))))
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
  output = data.frame(name =str_sub(name, 1, -5),
                      g_value = data$growth_rate)
}

##### Analyze the Data #####
redd_d_and_v_data = map_df(file_names,
                           ~get_redd_d_and_v(.x,
                                             file = "adult_events_output.csv"))

super_imp_data = map_df(file_names,
                        ~get_super_imp(.x,
                                       file = "detailed_pop_output.csv"))

growth_data = map_df(file_names, ~get_growth(.x,
                                                add = "_outputs",
                                                file = "abm_detailed_pop_output.csv",
                                                column_1 = "mean_rearing_growth_length",
                                                column_2 = "rearers",
                                                fish_input = 10000))

compare = left_join(survival_data,temp_data, by = "name") %>% 
  left_join(growth_data, by = "name") %>% 
  mutate(time_stamp = str_replace(Sys.time(), " ", "_"),
         area_base	= area_base,
         area_effect = area_effect,
         density = density,
         food = food,
         base_wood = base_wood,
         length = length,
         field_data = compare_values,
         fish_count = fish_number)
  
##### Write the Output #####
if (write) {
  if (file.exists(output_file)){
    file.copy(output_file, 
              str_replace(output_file, ".csv", "_old.csv"))
    
    run = max(read.csv(output_file)$run) + 1
    
    compare = mutate(compare, run = run)
    
    write.table(x = compare,
                file = output_file,
                sep = ",",
                col.names = FALSE,
                row.names = FALSE,
                append = TRUE)
  }else {
    compare = mutate(compare, run = 1)
    write.table(x = compare,
                file = output_file,
                sep = ",",
                row.names = FALSE)
  }
}

data_base = read.csv(output_file) 

summary = data_base %>% 
  mutate(percent_diff = abs(d_value - field_data)/field_data) %>% 
  group_by(run) %>% 
  summarise(percent_diff = mean(percent_diff, na.rm = T))
            
slopes = data_base %>% 
  group_by(run) %>% 
  nest() %>% 
  mutate(model = map(data, ~lm(d_value ~ field_data, data = .x) %>% 
                       tidy)) %>% 
  unnest(model) %>% 
  filter(term == 'field_data')

labeled = data_base %>% 
  mutate(author = str_sub(name,
                          str_locate(name, "ar_con/")[2]+7,
                          str_locate(name, "ar_con/")[2]+10))

plot = ggplot(labeled %>% filter(run == 14 | run == 21) ,
              aes(x = field_data,
                  y = d_value, 
                  color = factor(run))) +
  theme_classic() +
  geom_abline(intercept = 0, slope = 1) +
  coord_cartesian(xlim = c(0,1), ylim = c(0,1))+
  geom_point(size = 4, shape = 1)+
  # coord_cartesian(xlim = c(0.5, 1), ylim = c(0.5, 1)) +
  labs(x = "Filed Growth",
       y = "Model Growth")
print(plot)
