################################################################################
# This script takes an input file and reads form it what type of flow and
# temperature input file the program should make. It then makes it.
################################################################################

##### Load the functions #####
source(here("scripts",
            "make_environ_daily_data",
            "make_enviro_daily_data_functions.R"))

##### Main Work #####
# Convert the input file into the desired CSV output
ml$df$daily_input = load_daily_conditions(ml$df$daily) %>% 
  calc_photo_period(ml$df$top_marker) %>% 
  mutate(date = mdy(date))

##### Make the Files #####
# make one file to be used in the rest of the process
ml$path$daily_input_csv = here(ml$path$output_temp_folder, "daily_input_file.csv")
write.csv(x = ml$df$daily_input,
          file = ml$path$daily_input_csv,
          row.names = FALSE)

# make one file to for output
write.csv(x = ml$df$daily_input,
          file = here(ml$path$output_folder, "daily_input_file.csv"),
          row.names = FALSE)

##### Plots #####
# Make the time series plot
ml$plot$time_series_plot = make_daily_timeseries_plot(ml$df$daily_input)
# Print in outside window
display_plot(ml$plot$time_series_plot, 16, 12, preview_flag)

# Make the histogram plot
ml$plot$hist_plot = make_daily_histogram_plot(ml$df$daily_input)
# Print in outside window using patchwork
display_plot(ml$plot$hist_plot, 10, 10)

################################################################################
# End 
################################################################################
