#################################################
# This script runs multiple FHAST runs 
#################################################

##### Inputs #####
# Enter your output file to amend on you computer 
output_folder = "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/spawning_runs/outputs"

# Do you want to write the outputs
write = TRUE

# Do you want to run FAHST (FHAST will just read in existing outputs and do post processing)
run = FALSE

##### Load Libraries ######
library(here)
library(broom)
source(here("scripts","main","load_libraries.R"))
cbPalette <- c("#999999",
               "#0072B2",
               "#D55E00",
               "#F0E442",
               "#56B4E9",
               "#E69F00",
               "#009E73",
               "#CC79A7")

##### Load compare redd data #####
redd_data = readRDS("C:/Users/pndph/Documents/Research/Projects/FHAST/Work/spawning_runs/background_data/redd_presence_data.rds") %>% 
  filter(Present == 1) %>% 
  select(D, V) %>% 
  rename(velocity = V,
         depth = D) %>% 
  pivot_longer(cols = c(velocity, depth), names_to = "type")

rls_data_1 = read.csv("C:/Users/pndph/Documents/Research/Projects/FHAST/Work/spawning_runs/background_data/reproductive_lifespan_hendrey.csv",
                    skip = 1) %>% 
  group_by(type) %>% 
  mutate(number_dead = lag(total_survi, default = 1) - total_survi) %>%
  ungroup() %>% 
  mutate(number_dead = round(number_dead * 1000)) %>% 
  uncount(number_dead) %>% 
  mutate(data_set = ifelse(type == "early", 1, 2)) %>% 
  select(data_set, day)

rls_data_2 = read.csv("C:/Users/pndph/Documents/Research/Projects/FHAST/Work/spawning_runs/background_data/reproductive_lifespan_doctor.csv",
                      skip = 1) %>% 
  mutate(data_set = 3) 

rls_data_3 = read.csv("C:/Users/pndph/Documents/Research/Projects/FHAST/Work/spawning_runs/background_data/reproductive_lifespan_morbey.csv",
                      skip = 1) %>% 
  mutate(data_set = 4)

rls_data = rls_data_1 %>% 
  bind_rows(rls_data_2) %>% 
  bind_rows(rls_data_3) %>% 
  group_by(data_set) %>% 
  sample_n(1000, replace = TRUE)

##### List the File names #####
# create the master list
ml = list()
# any of the below list you want to remove
remove = c(100)

base_config_file = "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/spawning_runs/input_data/configure_files/100_adults.txt"
base_fish_file = "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/spawning_runs/input_data/fish/100.csv"
base_flow_file = "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/spawning_runs/input_data/daily/enviromental_input_dist.csv"

run_data = data.frame(expand.grid(count = c(seq(1e4, 2e5, 3e4)),
                                  iqr=(c(21, 42, 63)),
                                  flow = c(200, 400, 600)))


file_names = c()

# get the config file
config_data = read.csv(
  file = base_config_file,
  sep = ",",
  row.names = 1,
  header = FALSE) %>%
  # Trim off white spaces form values
  rename(value = 1) %>%
  mutate(value = str_trim(value, side = c("both")))

make_config_files = function(count,
                             iqr,
                             flow,
                             config_file_path,
                             fish_file_path,
                             base_flow_file){

  config_file = read.csv(
    file = config_file_path,
    sep = ",",
    row.names = 1,
    header = FALSE) %>%
    # Trim off white spaces form values
    rename(value = 1) %>%
    mutate(value = str_trim(value, side = c("both")))
  
  config_file["fish population",] = str_replace(config_file["fish population",],
                                                basename(config_file["fish population",]),
                                                paste0(format(count, scientific=F), "-", iqr, ".csv"))
  config_file["run name",] = paste0(format(count, scientific=F), "-",
                                    iqr, "-",
                                    format(flow, scientific=F),
                                    "_adults")
  config_file["daily conditions",] = str_replace(config_file["daily conditions",],
                                                 basename(config_file["daily conditions",]),
                                                 paste0(format(flow, scientific=F), ".csv"))
  
  fish_file = read.csv(base_fish_file) %>% 
    mutate(number = count,
           interquartile = iqr)
  
  flow_file = read.csv(base_flow_file,
                       row.names = 1,
                       header = FALSE) 
  flow_file["flow mean",] = flow
  
  write.table(config_file,
            str_replace(config_file_path,
                        basename(config_file_path),
                        paste0(format(count, scientific=F), "-",
                               iqr, "-",
                               format(flow, scientific=F),
                               "_adults.txt")),
            sep = ",",
            col.names = FALSE,
            quote = FALSE)
  
  write.csv(fish_file,
            str_replace(config_file["fish population",],
                                   basename(config_file["fish population",]),
                                   paste0(format(count, scientific=F), "-", iqr, ".csv")),
            row.names = FALSE)
  
  write.table(flow_file,
            str_replace(config_file["daily conditions",],
                        basename(config_file["daily conditions",]),
                        paste0(format(flow, scientific=F), ".csv")),
            sep = ",",
            col.names = FALSE,
            quote = FALSE)
  
  file_names <<- append(file_names, str_replace(config_file_path,
                                                basename(config_file_path),
                                                paste0(format(count, scientific=F), "-",
                                                       iqr, "-",
                                                       format(flow, scientific=F),
                                                       "_adults.txt")))
  
}

pwalk(.l = list(run_data$count, run_data$iqr, run_data$flow),
      ~make_config_files(..1, ..2, ..3,
                         base_config_file,
                         base_fish_file,
                         base_flow_file))


# get the output folder
output_folder = config_data["output path", ]

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
    mutate(run_name = str_sub(basename(name), 1, -5),
           iqr = str_sub(run_name,
                         str_locate_all(run_name, "-")[[1]][[1]]+1,
                         str_locate_all(run_name, "-")[[1]][[2]]-1),
           flow = str_sub(run_name,
                          str_locate_all(run_name, "-")[[1]][[2]]+1,
                          str_locate_all(run_name, "_")[[1]][[1]]-1))
  output = data
}

get_age_at_death = function(name, file){
  new_name = paste0(output_folder, "/", str_sub(basename(name), 1, -5), "_outputs/temporary/", file)
  data = read.csv(new_name, skip = 1) %>% 
    filter(event == "adult died") %>% 
    select(species, age) %>% 
    mutate(run_name = str_sub(basename(name), 1, -5),
           iqr = str_sub(run_name,
                         str_locate_all(run_name, "-")[[1]][[1]]+1,
                         str_locate_all(run_name, "-")[[1]][[2]]-1),
           flow = str_sub(run_name,
                          str_locate_all(run_name, "-")[[1]][[2]]+1,
                          str_locate_all(run_name, "_")[[1]][[1]]-1))
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
           count = str_sub(run_name, 0, str_locate_all(run_name, "-")[[1]][[1]]-1),
             iqr = str_sub(run_name,
                           str_locate_all(run_name, "-")[[1]][[1]]+1,
                           str_locate_all(run_name, "-")[[1]][[2]]-1),
           flow = str_sub(run_name,
                          str_locate_all(run_name, "-")[[1]][[2]]+1,
                          str_locate_all(run_name, "_")[[1]][[1]]-1),
           fraction_dead = dead_eggs/(total_alive_eggs + dead_eggs) )
  output = data
}



##### Analyze the Data #####
redd_d_and_v_data = map_df(file_names,
                           ~get_redd_d_and_v(.x,
                                             file = "adult_events_output.csv")) %>% 
  pivot_longer(cols = c(velocity, depth), names_to = "type")

age_at_death = map_df(file_names,
                      ~get_age_at_death(.x,
                                        file = "adult_events_output.csv"))

super_imp_data = map_df(file_names,
                        ~get_super_imp(.x,
                                       file = "detailed_pop_output.csv"))


v_d_equation = data.frame(value = seq(0,10,0.01)) %>% 
  mutate(velocity = (1+exp(-(-1.06 + 2.77 * value - 1.22 * value^2)))^-1,
         depth = (1+exp(-(-1.02 + 1.46 * value - 0.18 * value^2)))^-1) %>% 
  pivot_longer(cols = c(velocity, depth), names_to = "type", values_to = "prob")

v_d_plot = ggplot(redd_d_and_v_data) +
  theme_classic(base_size = 20) +
  theme(axis.ticks.y = element_blank(),
        axis.text.y = element_blank(),
        strip.background = element_blank(),
        strip.placement='outside',
        # legend.position = "inside",
        # legend.position.inside = c(0.85, 0.3),
        legend.background = element_blank()) +
  geom_density(data = redd_data, aes(x=value, color = "Field Data"),
               adjust = 6,
               # color = "gray30",
               linewidth = 1) +
  # geom_path(data = v_d_equation, aes(x=value, y = prob)) +
  geom_density(aes(x=value, group = run_name, color = flow), linewidth = 0.1, adjust = 2) +
  facet_wrap(type ~ .,
             nrow = 2,
             scales = "free",
             strip.position = 'bottom',
             labeller = as_labeller(c(depth='Redd Depth (m)',
                                      velocity='Redd Velocity (m/s)'))) +
  scale_color_manual(values = c(cbPalette[1:3], "gray30"),
                     name = expression(Flow ~ (m^3/s)),
                     guide = guide_legend(override.aes = list(linewidth = 2))) +
  coord_cartesian(xlim = c(0,6)) +
  labs(x = NULL,
       y = NULL)
print(v_d_plot)
ggsave(here(output_folder, "figures", "v_d_plot.png"),
       v_d_plot,
       device = "png",
       height = 4,
       width = 5)

age_plot = ggplot(age_at_death) +
  theme_classic(base_size = 20) +
  theme(axis.ticks.y = element_blank(),
        axis.text.y = element_blank(),
        legend.position = "inside",
        legend.position.inside = c(0.85, 0.75),
        legend.background = element_blank()) +
  geom_density(data = rls_data,
               aes(x = day, color = "Field Data", y = after_stat(scaled)),
               adjust = 4,
               linewidth = 1) +
  geom_density(aes(x=age, group = run_name, color = flow, y = after_stat(scaled)),
               linewidth = 0.3,
               adjust = 2) +
  scale_color_manual(values = c(cbPalette[2:4], "gray50"),
                     name = expression(Flow ~ (m^3/s)),
                     guide = guide_legend(override.aes = list(linewidth = 2))) +
  coord_cartesian(xlim = c(0,50)) +
  labs(x = "Survival Post Spawn (days)",
       y = NULL)
print(age_plot)
ggsave(here(output_folder, "figures", "age_plot.png"),
       age_plot,
       device = "png",
       height = 4,
       width = 5)

super_plot = ggplot(data = super_imp_data,
                    aes(x = total_redds,
                        y = fraction_dead,
                        color = iqr,
                        group = interaction(flow,iqr))) +
  theme_classic(base_size = 20) +
  theme(legend.position = "inside", 
        legend.position.inside = c(0.8, 0.25),
        legend.background = element_blank()) +
  geom_point(shape = 1,size = 4, stroke = 1) +
  scale_color_manual(values = cbPalette) +
  labs(x = "Redd Count",
       y = "Fraction Eggs Dead",
       color = "IQR (days)")
print(super_plot)
ggsave(here(output_folder, "figures", "super_plot.png"),
       super_plot,
       device = "png",
       height = 4,
       width = 5)
