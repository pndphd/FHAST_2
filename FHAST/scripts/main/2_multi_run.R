#################################################
# This script runs multiple FHAST runs 
#################################################

##### In4506s #####
output_file = "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/compare.csv"

write = TRUE
run = TRUE

area_base	= 0.18
area_effect = 0.08
density = 0.003
food = 0.42
base_wood = 0.05
fish_number = 10000
length = rep(20,36)
  
##### Load Libraries ######
library(tidyverse)
library(here)
library(broom)

##### List the File names #####
remove = c(100)

file_names = c(
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/michel_2015_1.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/michel_2015_2.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/michel_2015_3.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/michel_2015_4.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/michel_2015_5.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/michel_2015_6.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/michel_2015_7.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/michel_2015_8.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/michel_2015_9.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/michel_2015_10.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/michel_2015_11.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/sandstorm_2020_1.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/sandstorm_2020_2.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/sandstorm_2020_3.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/sandstorm_2020_4.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/sandstorm_2020_5.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/sandstorm_2020_6.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/sandstorm_2020_7.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/sandstorm_2020_8.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/sandstorm_2020_9.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/singer_2012_1.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/singer_2012_2.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/singer_2012_3.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/singer_2012_4.txt",  
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/sommer_2001_1998.txt",
  # "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/sommer_2001_1999.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/steel_2020_2013_1.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/steel_2020_2013_2.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/steel_2020_2013_3.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/steel_2020_2013_4.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/steel_2020_2013_5.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/steel_2020_2013_6.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/steel_2020_2014_1.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/steel_2020_2014_2.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/steel_2020_2014_3.txt",
  "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con_gs/steel_2020_2014_4.txt"
)

compare_values = rep(0.1,36)

file_names = file_names[-remove]
compare_values = compare_values[-remove]

##### Run the Sims #####
run_multi = function(file_name){
  ml$path$config_file <<- file_name
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
                                                file = "daily_input_filed.csv",
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
                          str_locate(name, "ar_con_gs/")[2]+7,
                          str_locate(name, "ar_con_gs/")[2]+10))

plot = ggplot(labeled %>% filter(run == 1 || run == 7),
              aes(x = field_data,
                  y = g_value, 
                  color = factor(run))) +
  theme_classic() +
  geom_abline(intercept = 0, slope = 1) +
  coord_cartesian(xlim = c(0,1), ylim = c(0,1))+
  geom_point(size = 4, shape = 1)+
  coord_cartesian(xlim = c(0.1, 0.3), ylim = c(0.1, 0.3)) +
  labs(x = "Filed Growth",
       y = "Model Growth")
print(plot)
