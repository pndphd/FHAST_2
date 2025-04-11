##### Description ######################
# This script takes an input file and reads form it what type of flow and temperature
# input file the program should make. It then makes it.
########################################

##### Load the functions #####
source(here("scripts",  "make_environ_daily_data", "make_enviro_daily_data_functions.R"))

##### Main Work #####
# Convert the input file into the desired CSV output
daily_input_data <- load_daily_conditions(ml$df$daily)

# calculate photo period use grid top marker as location
daily_w_photo_period = calc_photo_period(ml$df$top_marker, daily_input_data)

##### Make the Files #####
# make one file to be used in the rest of the process
write.csv(x = daily_w_photo_period,
          file = here(ml$path$output_temp_folder, "daily_input_file.csv"),
          row.names = FALSE)

# make one file to for output
write.csv(x = daily_w_photo_period,
          file = here(ml$path$output_folder, "daily_conditions_processed.csv"),
          row.names = FALSE)

# Copy the input file over to the output folder for refrence
write.table(ml$df$daily,
            file = here(ml$path$output_folder, "daily_conditions.txt"),
            row.names = F,
            col.names = F)

##### Plots #####
# Make the time series plot
time_series_plot <- make_daily_timeseries_plot(daily_w_photo_period)
# Print in outside window
display_plot(time_series_plot, 16, 12, preview_flag)

# Make the histogram plot
hist_plot <- make_daily_histogram_plot(daily_w_photo_period)
# Print in outside window using patchwork
display_plot(hist_plot, 10, 10)
