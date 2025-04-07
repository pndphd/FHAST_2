##### Description ######################
# These are the functions for the make_the_input_file
########################################

##### Functions #####
# The main formating function
load_daily_conditions = function(daily_inputs_in) {
  ##### Make the Files #####
  # Error check in case user put in an actual hydrograph file
  if(NCOL(daily_inputs_in)>1){
    message(paste0("!!!!!!!!!!!\n",
                   "!!!ERROR!!! Too many columns in the environmental input file. \n",
                   "!!!!!!!!!!!\n",
                   "You may be entering a hydrograph file and not a \n",
                   "refrence file pointing to it."))
    stop()
    
  }
  
  # Get what type of file it is
  file_type = daily_inputs_in["type",]
  
  # get dates in correct R format
  start_date = mdy(daily_inputs_in["start date",])
  end_date = mdy(daily_inputs_in["end date",])

  # Make a sequence of dates and put in dumb excel format
  dates = seq(start_date, end_date, 1) %>% 
    format("%m/%d/%Y")
  days = seq(1, length(dates))

  # Get parameters
  params = read_parameters(daily_inputs_in, file_type)
    
  if (file_type == "distribution"){
    
    # get the starting values
    start_flow = get_starting_values(params$flow_type, params$flow_mean)
    start_temp = get_starting_values(params$temp_type, params$temp_mean)
    start_turb = get_starting_values(params$turb_type, params$turb_mean)

    # Make placeholder data set
    output_data = data.frame(date = dates,
                            day = days,
                            flow_cms_con = accumulate(rep(start_flow, length(dates)),
                                                  ~calc_next_value(.x,
                                                                    params$flow_mean,
                                                                    params$flow_SD,
                                                                    params$flow_autocor,
                                                                    params$flow_type)),
                            turb_ntu_con = accumulate(rep(start_turb, length(dates)),
                                                      ~calc_next_value(.x,
                                                                        params$turb_mean,
                                                                        params$turb_SD,
                                                                        params$turb_autocor,
                                                                        params$turb_type)),
                            temp_c_con = accumulate(rep(start_temp, length(dates)),
                                                ~calc_next_value(.x,
                                                                  params$temp_mean,
                                                                  params$temp_SD,
                                                                  params$temp_autocor,
                                                                  params$temp_type))) %>% 
      # Change the value depending on the increase
      # Also check for the min values and 0 for temperature and turbidity
      mutate(flow_cms = pmax(flow_cms_con + params$flow_change * (day - 1), params$flow_min),
            temp_c = pmax(temp_c_con + params$temp_change * (day - 1), 0),
            turb_ntu = pmax(turb_ntu_con + params$turb_change * (day - 1), 0)) %>% 
      select(-flow_cms_con, -temp_c_con, -turb_ntu_con)
    
  } else if (file_type == "hydrograph"){

    # Get parameters
    hydro_file_name = daily_inputs_in["file",]
    # Read in the file and convert to date
    daily_folder = str_sub(daily_path,
                           end = max(unlist(str_locate_all(daily_path, "/"))))
    message(daily_path)
    hydro_file = read.csv(file = here(daily_folder, hydro_file_name)) %>% 
      mutate(date = mdy(date))
    
    # Check that all the needed columns are there
    if(!("flow_cms" %in% colnames(hydro_file)) |
       !("temp_c" %in% colnames(hydro_file)) |
       !("turb_ntu" %in% colnames(hydro_file))){
      message(paste0("!!!!!!!!!!!\n",
                     "!!!ERROR!!! The hydrograph file is missing a required column. \n",
                     "!!!!!!!!!!!\n",
                     "The columns are flow_cms, temp_c, & turb_ntu"))
      stop()
      
    }

    # Check that all the days are there
    if(as.numeric(max(hydro_file$date) - min(hydro_file$date)) != NROW(hydro_file)-1){
      message(paste0("!!!!!!!!!!!\n",
                     "!!!ERROR!!! The hydrograph file is missing some or has duplicate days. \n",
                     "!!!!!!!!!!!\n"))
      stop()
      
    }
    
    # use left join to just get dates wanted and convert to dumb excel date format
    output_data = data.frame(date = dates,
                            day = days) %>% 
      mutate(date = mdy(date)) %>% 
      left_join(hydro_file, by = "date") %>% 
      mutate(date = format(date, "%m/%d/%Y"))

  } else if (file_type == "link"){

    # get the starting values
    start_flow = get_starting_values(params$flow_type, params$flow_mean)

    # Make placeholder data set
    output_data = data.frame(date = dates,
                            day = days,
                            flow_cms_con = accumulate(rep(start_flow, length(dates)),
                                                      ~calc_next_value(.x,
                                                                        params$flow_mean,
                                                                        params$flow_SD,
                                                                        params$flow_autocor,
                                                                        params$flow_type))) %>% 
      # Change the value depending on the increase
      # Also check for the min values and 0 for temperature and Turbidity
      rowwise() %>% 
      mutate(flow_cms = pmax(flow_cms_con + params$flow_change * (day - 1), params$flow_min),
            temp_c_temp = (params$temp_a + params$temp_b * flow_cms),
            temp_c = temp_c_temp* params$temp_cor + 
              (1 - params$temp_cor) * rnorm(1, mean = temp_c_temp, sd = params$temp_SD),
            turb_ntu_temp = (params$turb_a + params$turb_b * flow_cms),
            turb_ntu = turb_ntu_temp* params$turb_cor + 
              (1 - params$turb_cor) * rnorm(1, mean = turb_ntu_temp, sd = params$turb_SD)) %>% 
      select(-flow_cms_con, -temp_c_temp, -turb_ntu_temp) %>% 
      ungroup()
  }
  output = output_data %>% 
    mutate(month = month(as_date(date, format = "%m/%d/%Y")))
  
  return (output)
}

# Make the function to calculate the next value in the distribution
calc_next_value = function(current_value, mean, sd, autocor, dist_type_in){
  # Select next vlue depending on desired distribution
  if (dist_type_in == "normal") {
    new_value = current_value * autocor +
      (1-autocor) * rnorm(1, mean = mean, sd = sd)
  } else if (dist_type_in == "lognormal") {
    new_value = current_value * autocor +
      (1-autocor) * rlnorm(1, mean = mean, sd = sd)
  } else {
    stop('\nInvalid distribution type.')
  }
  
  return(new_value)
}

# This function just reads in the parameters based on the file type
read_parameters <- function(input_file_in, file_type_in){
  output_list = list()
  if (file_type_in == "distribution"){
    output_list$temp_type = input_file_in["temperature distribution",]
    output_list$temp_mean = as.numeric(input_file_in["temperature mean",])  
    output_list$temp_SD = as.numeric(input_file_in["temperature SD",])
    output_list$temp_autocor = as.numeric(input_file_in["temperature autocorrelation",])
    output_list$temp_change = as.numeric(input_file_in["temperature change",])
    output_list$flow_type = input_file_in["flow distribution",]
    output_list$flow_mean = as.numeric(input_file_in["flow mean",])
    output_list$flow_SD = as.numeric(input_file_in["flow SD",])
    output_list$flow_autocor = as.numeric(input_file_in["flow autocorrelation",])
    output_list$flow_change = as.numeric(input_file_in["flow change",])
    output_list$flow_min = as.numeric(input_file_in["flow min",])
    output_list$turb_type = input_file_in["turbidity distribution",]
    output_list$turb_mean = as.numeric(input_file_in["turbidity mean",])
    output_list$turb_SD = as.numeric(input_file_in["turbidity SD",])
    output_list$turb_autocor = as.numeric(input_file_in["turbidity autocorrelation",])
    output_list$turb_change = as.numeric(input_file_in["turbidity change",])
    
  } else if (file_type_in == "hydrograph"){
    hydro_file_name = input_file_in["file",]
    
  } else if (file_type_in == "link"){
    output_list$temp_SD = as.numeric(input_file_in["temperature SD",])
    output_list$temp_cor = as.numeric(input_file_in["temperature correlation",])
    output_list$temp_a = as.numeric(input_file_in["temperature intercept",])
    output_list$temp_b = as.numeric(input_file_in["temperature slope",])
    output_list$turb_SD = as.numeric(input_file_in["turbidity SD",])
    output_list$turb_cor = as.numeric(input_file_in["turbidity correlation",])
    output_list$turb_a = as.numeric(input_file_in["turbidity intercept",])
    output_list$turb_b = as.numeric(input_file_in["turbidity slope",])
    output_list$flow_type = input_file_in["flow distribution",]
    output_list$flow_mean = as.numeric(input_file_in["flow mean",])
    output_list$flow_SD = as.numeric(input_file_in["flow SD",])
    output_list$flow_autocor = as.numeric(input_file_in["flow autocorrelation",])
    output_list$flow_change = as.numeric(input_file_in["flow change",])
    output_list$flow_min = as.numeric(input_file_in["flow min",])
    
  } else {
    stop('\nYou did not select a valid type.
         \nPlease select "link", "distribution", or "hydrograph"')
  }

    return(output_list)
}

# Get starting values. Just the means
get_starting_values <- function(dist_type, mean_value){
    if (dist_type == "normal") {
      start_value = mean_value
    } else if (dist_type == "lognormal") {
      start_value = exp(mean_value)
    } else {
      stop('\nYou did not select a valid flow distribution type.\nPlease select "normal" or "log"')
    }
  return(start_value)
}

# A function to calculate photo period
calc_photo_period = function(shape_file_in,
                             df_in){
  location = shape_file_in %>% 
    summarize(geometry = st_union(geometry)) %>% 
    st_centroid() %>% 
    st_transform(st_crs("EPSG:4326"))

  df_out = df_in %>% 
    mutate(photo_time = as.POSIXct(x = mdy(date),
                                   tz = tz_lookup(location, method = "accurate")),
           sun_set = sunriset(crds = st_coordinates(location),
                              dateTime = photo_time,
                              crs=CRS(st_crs(location)$proj4string),
                              direction="sunset",
                              POSIXct.out=TRUE)$day_frac,
           sun_rise = sunriset(crds = st_coordinates(location),
                               dateTime = photo_time,
                               crs=CRS(st_crs(location)$proj4string),
                               direction="sunrise",
                               POSIXct.out=TRUE)$day_frac,
           photoperiod = sun_set - sun_rise) %>% 
    select(-photo_time, -sun_rise, - sun_set)
}

# Make the time series plot
make_daily_timeseries_plot = function(output_data) {
  # Plot each time series
time_series_plot_f = ggplot(data = output_data, aes(x = mdy(date), y = flow_cms)) +
  theme_classic(base_size = 20) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  geom_path(linetype = "solid") +
  labs(x = "Date", y = "Flow (cms)") +
  theme(axis.title.x = element_blank(),
        axis.text.x = element_blank(),
        axis.ticks.x = element_blank())
time_series_plot_t = ggplot(data = output_data, aes(x = mdy(date), y = temp_c)) +
  theme_classic(base_size = 20) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  geom_path(linetype = "solid") +
  labs(x = "Date", y = "Temperature (\u00B0C)") +
  theme(axis.title.x = element_blank(),
        axis.text.x = element_blank(),
        axis.ticks.x = element_blank())
time_series_plot_u = ggplot(data = output_data, aes(x = mdy(date), y = turb_ntu)) +
  theme_classic(base_size = 20) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  geom_path(linetype = "solid") +
  labs(x = "Date",
       y = "Turbidity (NTUs)",
       caption = paste0("Three time series graph of the daily conditions.")) +
  theme(plot.caption = element_text(hjust = 0, size = 15))

# merge them all into 1 plot
time_series_plot = time_series_plot_f /
  time_series_plot_t/
  time_series_plot_u
  return (time_series_plot)
}

# The function fo the combinde histogram plot
make_daily_histogram_plot = function(output_data) {
  # Make the plots
  temp_hist_plot = make_hist_plot(output_data,
                                  "temp_c",
                                  "Temperature (\u00B0C)")
  flow_hist_plot = make_hist_plot(output_data,
                                  "flow_cms",
                                  "Flow (cms)")
  turb_hist_plot = make_hist_plot(output_data,
                                  "turb_ntu",
                                  "Turbidity (NTUs)",
                                  caption = "Three histograms of the daily conditions.") 
  hist_plot = flow_hist_plot /
    temp_hist_plot /
    turb_hist_plot 
  return (hist_plot)
}

# Make the function for histogram plots
make_hist_plot = function(data_in, variabel, legend, caption = ""){
  out_hist_plot = ggplot(data = data_in, aes(x = !! sym(variabel))) +
    theme_classic(base_size = 20) +
    theme(axis.title.y=element_blank(),
          axis.text.y=element_blank(),
          axis.ticks.y=element_blank(), 
          plot.caption = element_text(hjust = 0, size = 15)) +
    geom_histogram(aes(y=after_stat(density)),
                   bins = 30,
                   color = ml$df$palette[1],
                   fill = ml$df$palette[1],
                   alpha = 0.25) +
    scale_x_continuous(expand = expansion(mult = c(0, 0.05))) +
    scale_y_continuous(expand = expansion(mult = c(0, 0.05))) +
    labs(x = legend,
         caption = caption)
  
  return(out_hist_plot)
}
