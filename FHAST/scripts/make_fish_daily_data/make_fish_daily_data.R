##### Description #####
# This script takes an input file and reads form it what type of flow and
# temperature input file the program should make. It then makes it.

##### Load the functions
source(here("scripts",  "make_fish_daily_data", 
            "make_fish_daily_data_functions.R"))

##### Run the main function
ml$df$fish_schedule = load_fish_timeseries(ml$df$fish_pop) %>%
  # take out dates that aren't in the environmental data
  filter(mdy(date) >= min(ymd(ml$df$daily_input$date)) &
           mdy(date) <= max(ymd(ml$df$daily_input$date))) %>% 
  mutate(date = mdy(date))

# Check if you removed fish
if(NROW(ml$df$fish_schedule) < NROW(load_fish_timeseries(ml$df$fish_pop))){
  message(paste0("!!!!!!!!!!!!!\n",
                 "!!!WARNING!!! Some fish removed because they are outside the model time window. \n",
                 "!!!!!!!!!!!!!\n"))
}

# Get flags to check what runs to do
ml$var$juvenile_run = ifelse(NROW(filter(ml$df$fish_schedule, lifestage == "juvenile"))>0, T ,F)
ml$var$adult_run = ifelse(NROW(filter(ml$df$fish_schedule, lifestage == "adult"))>0, T ,F)
ml$var$spawner_run = ifelse(NROW(filter(ml$df$fish_schedule, lifestage == "spawner"))>0, T ,F)

# Get all the fish combos
ml$df$fish_combos = ml$df$fish_schedule %>% 
  select(lifestage, species) %>% 
  distinct()

##### Save the result #####
write.csv(ml$df$fish_schedule,
          file = here(ml$path$output_temp_folder, "daily_fish_input.csv"),
          row.names = FALSE)

# make one file to for output
write.csv(x = ml$df$fish_schedule,
          file = here(ml$path$output_folder, "daily_fish_input.csv"),
          row.names = FALSE)

##### Make a plot #####
ml$plot$time_series_plot_fish = plot_fish_timeseries(ml$df$fish_schedule)

display_plot(ml$plot$time_series_plot_fish, 12, 12, preview_flag)

################################################################################
# End
################################################################################
