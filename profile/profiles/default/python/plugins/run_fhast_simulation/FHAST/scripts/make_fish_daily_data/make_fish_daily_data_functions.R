##### Description #####
# These are the functions for the make_the_input_file

# Make the function to calculate fish per day
spread_out_fish <- function(...) {

  current <- tibble(...)
  # Get the standard deviation
  sd <- (current$interquartile / 2) / qnorm(0.75)
  df <- data.frame(date = seq(from = current$date - 100 * current$interquartile,
                             to = current$date + 100 * current$interquartile,
                             by = 1)) %>%
    mutate(difference = as.numeric(date - current$date),
           value = 1 / (sd * sqrt(2 * pi)) * exp(-0.5 * (difference / sd) ^ 2),
           raw_number = value * current$number,
           wrong_number = round(raw_number, 0)) %>%
    filter(wrong_number > 0) %>%
    # Correct for the tails that were taken off
    mutate(fraction = value / sum(value),
           number = round(fraction * current$number, 0),
           species = current$species,
           lifestage = current$lifestage,
           length = current$length,
           length_sd = current$sd) %>%
    select(date, number, species, lifestage, length, length_sd)
  return(df)
}

load_fish_timeseries <- function(input_file_in) {
  ##### Make the Files #####
  # make the list of days and fish
  fish_schedule <- input_file_in %>%
    pmap_dfr(~spread_out_fish(...)) %>%
    arrange(date) %>%
    group_by(species, lifestage) %>% 
    # change to account for super individuals
    mutate(date = format(date, "%m/%d/%Y"),
           cum_sum = floor(cumsum(number)/habitat_parm$superind_ratio),
           number = ifelse(lifestage == "adult", number,
                           cum_sum-lag(cum_sum, default = 0))) %>% 
    ungroup() %>% 
    select(-cum_sum)
  return(fish_schedule)
}

plot_fish_timeseries <- function(fish_schedule) {
  fish_plot_data <- fish_schedule %>%
    mutate(Group = str_c(species, " ", lifestage),
           plot_number = ifelse(lifestage == "adult",
                                number,
                                number * habitat_parm$superind_ratio))
  
  time_series_plot_fish <- ggplot(data = fish_plot_data, aes(x = mdy(date),
                                                             y = plot_number,
                                                             color = Group)) +
    theme_classic(base_size = 20) +
    theme(legend.position = "top") +
    theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1)) +
    geom_path(linetype = "solid") +
    scale_color_viridis_d() +
    labs(x = "Date",
         y = "Count",
         caption = paste0("A time series graph of fish entering the system\n",
                          "broken out by species and lifestage.")) +
    theme(plot.caption = element_text(hjust = 0, size = 15))

  return(time_series_plot_fish)
}
