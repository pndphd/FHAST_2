#################################################
# This script runs multiple FHAST runs 
#################################################

##### Inputs #####
# Enter your output file to amend on you computer 
output_file = "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/compare.csv"

# Do you want to write the outputs
write = TRUE

# Do you want to run FAHST (FLASE will just read in existing outputs and do post processing)
run = TRUE

# Write in the parameters you are using. they will be noted in the output file 
# The base area for predators
area_base	= 0.18
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
# any of th ebelow list you want to remove
remove = c(100)

# list of input files to run
file_names = c(

  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/michel_2015_1.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/michel_2015_2.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/michel_2015_3.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/michel_2015_4.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/michel_2015_5.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/michel_2015_6.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/michel_2015_7.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/michel_2015_8.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/michel_2015_9.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/michel_2015_10.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/michel_2015_11.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/sandstorm_2020_1.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/sandstorm_2020_2.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/sandstorm_2020_3.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/sandstorm_2020_4.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/sandstorm_2020_5.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/sandstorm_2020_6.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/sandstorm_2020_7.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/sandstorm_2020_8.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/sandstorm_2020_9.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/singer_2012_1.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/singer_2012_2.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/singer_2012_3.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/singer_2012_4.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/sommer_2001_1998.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/sommer_2001_1999.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/steel_2020_2013_1.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/steel_2020_2013_2.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/steel_2020_2013_3.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/steel_2020_2013_4.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/steel_2020_2013_5.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/steel_2020_2013_6.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/steel_2020_2014_1.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/steel_2020_2014_2.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/steel_2020_2014_3.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/steel_2020_2014_4.txt"
  
  #American
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/american_river_cal/satter_2001_1.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/american_river_cal/satter_2001_2.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/american_river_cal/satter_2002_1.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/american_river_cal/satter_2002_2.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/american_river_cal/satter_2004_1.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/american_river_cal/satter_2004_2.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/american_river_cal/satter_2006_1.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/american_river_cal/satter_2006_2.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/american_river_cal/satter_2007_1.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/american_river_cal/satter_2007_2.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/american_river_cal/satter_2008_1.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/american_river_cal/satter_2008_2.txt"
)

# growth values on the american
# American
# compare_values = rep(c(0.13, 0.19),6)

# survival values on the sacramento
# Sacramento
compare_values = c(
                   rep(0.92, 11),
                   0.919,
                   0.976,
                   0.92,
                   0.935,
                   0.934,
                   0.952,
                   0.78,
                   0.985714286,
                   0.977011494,
                   0.756,
                   0.756,
                   0.678,
                   0.687,
                   0.052,
                   0.043,
                   0.7300608,
                   0.80934084,
                   0.82719252,
                   0.85484322,
                   0.84523824,
                   0.82719252,
                   0.85484322,
                   0.72093504,
                   0.78253392,
                   0.82719252
                   )

file_names = file_names[-remove]
compare_values = compare_values[-remove]

##### Run the Sims #####
run_multi = function(file_name){
  wild_card_file_name <<- file_name
  source(here("scripts","main","run_all.R"))
}

if (run){
  walk(file_names, ~run_multi(.x))
}


##### Functions to process runs ######
get_survival = function(name, add, file, column, fish_input){
  #name = str_sub(name, 4, -1)
  new_name = paste0(str_sub(name, 1, -5), add, "/", file)
  data = read.csv(new_name)
  output = data.frame(name =str_sub(name, 1, -5),
                      d_value = 1-sum(select(data, contains(column)))/fish_input)
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
survival_data = map_df(file_names, ~get_survival(.x,
                                                 add = "_outputs",
                                                 file = "abm_detailed_pop_output.csv",
                                                 column = "dead_fish",
                                                 fish_input = 10000))

temp_data = map_df(file_names, ~get_temperature(.x,
                                                add = "_outputs",
                                                file = "daily_conditions_processed.csv",
                                                column = "temp_c",
                                                fish_input = 10000))

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
