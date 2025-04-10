##### Description #####
# This script takes an input file and reads form it what type of flow and
# temperature input file the program should make. It then makes it.

##### Load the functions
source(here("scripts",  "make_fish_daily_data", 
            "make_fish_daily_data_functions.R"))

##### Run the main function
fish_schedule_full = load_fish_timeseries(ml$df$fish_pop) 
  
fish_schedule = fish_schedule_full %>%
  # take out dates that aren't in the enviromental data
  filter(mdy(date) >= min(mdy(daily_input_data$date)) &
           mdy(date) <= max(mdy(daily_input_data$date)))

# Check if you removed fish
if(NROW(fish_schedule) < NROW(fish_schedule_full)){
  message(paste0("!!!!!!!!!!!!!\n",
                 "!!!WARNING!!! Some fish removed because they are outside the model time window. \n",
                 "!!!!!!!!!!!!!\n"))
}

# Get flags to check what runs to do
juvenile_run = ifelse(NROW(filter(fish_schedule, lifestage == "juvenile"))>0, T ,F)
adult_run = ifelse(NROW(filter(fish_schedule, lifestage == "adult"))>0, T ,F)

##### Save the result #####
write.csv(fish_schedule,
          file = here(temp_folder, "daily_fish_input.csv"),
          row.names = FALSE)

# make one file to for output
write.csv(x = fish_schedule,
          file = here(output_folder, "daily_fish_processed.csv"),
          row.names = FALSE)

##### Make a plot #####
fish_plot_data <- fish_schedule %>%
  mutate(Group = str_c(species, " ", lifestage))

time_series_plot_fish <- plot_fish_timeseries(fish_schedule)

display_plot(time_series_plot_fish, 12, 12, preview_flag)
