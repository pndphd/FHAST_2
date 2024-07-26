########################################
# This script makes graphs and summaries from the
# ABM outputs
########################################

##### Run the initialization scripts #####
# Make sure weighted.mean isn't over written
weighted.mean = stats::weighted.mean

# Load Libraries and some base parameters
source(here("scripts","main","load_libraries.R"))
source(here("scripts","make_abm_summary","make_abm_summary_functions.R"))

##### Load the data #####

detailed_data_temp <- read.csv(file = here(output_temp_folder, "detailed_pop_output.csv"),
                               skip = 1) %>% 
  mutate(date = ymd(time)) %>% 
  filter(juveniles != 0)
cell_data_temp <- read.csv(file = here(output_temp_folder, "cell_info_output.csv"),
                           skip = 1) %>% 
  mutate(date = ymd(time))
event_data_temp <- read.csv(file = here(output_temp_folder, "events_output.csv"),
                            skip = 1) %>% 
  mutate(date = ymd(time))

##### Pre-calculations #####
# get a list of species
species_list = unique(detailed_data_temp$Species)

# do some general calculations
detailed_data = detailed_data_temp %>%
  mutate(all_survival_prob = (juveniles - dead_fish)/juveniles,
         nonmigrant_survival_prob = (nonmigrants - dead_nonmigrants)/nonmigrants,
         #smolt_survival_prob = (smolts - dead_smolt)/smolts,
         migrant_survival_prob = (migrants - dead_migrants)/migrants,
         rear_survival_prob = (rearers - dead_rearers)/rearers,
         run_day = as.numeric(date - min(date)))

mortality_breakdown = detailed_data %>% 
  group_by(Species) %>% 
  summarise(predation = sum(predation_deaths, na.rm = TRUE),
            poor_condition = sum(poor_condition_deaths, na.rm = TRUE),
            stranding = sum(stranding_deaths, na.rm = TRUE),
            temperature = sum(high_t_deaths, na.rm = TRUE)) %>% 
  pivot_longer(cols = !matches("Species"), names_to = "Cause", values_to = "Count")

# separate based on species
detailed_data_list = map(species_list, ~filter(detailed_data, Species == .x ))
event_data_list = map(species_list, ~filter(event_data_temp, Species == .x ))

# Calculate values
summary_table = detailed_data_list %>% 
  map_df(~make_abm_table(.x))

##### Make plots #####
rearing_plot = map(detailed_data_list,
                   ~make_line_plot(data_frame = .x,
                                 x_axis = date,
                                 y_axis = rearers,
                                 x_lab =  "Date",
                                 y_lab = "Rearing Fish",
                                title = .x$Species[1])) %>% 
  wrap_plots(ncol = 1, widths = plot_widths,
             heights = length(detailed_data_list) * plot_widths)

# X11()
# print(rearing_plot)

growth_plot = map(detailed_data_list,
                   ~make_line_plot(data_frame = .x,
                                   x_axis = date,
                                   y_axis = mean_rearing_growth_length,
                                   x_lab =  "Date",
                                   y_lab = "Growth (cm)",
                                   title = .x$Species[1])) %>% 
  wrap_plots(ncol = 1, widths = plot_widths,
             heights = length(detailed_data_list) * plot_widths)
# X11()
# print(growth_plot)

count_v_growth_plot = map(detailed_data_list,
                  ~make_color_scatter_plot(data_frame = .x,
                                  x_axis = rearers,
                                  y_axis = mean_rearing_mass_growth_fra,
                                  x_lab =  "Count",
                                  y_lab = "Fraction Mass Increase",
                                  color = run_day,
                                  color_lab = "Run Day",
                                  title = .x$Species[1])) %>% 
  wrap_plots(ncol = 1, widths = plot_widths,
             heights = length(detailed_data_list) * plot_widths)

# X11()
# print(count_v_growth_plot)

count_v_length_plot = map(detailed_data_list,
                          ~make_color_scatter_plot(data_frame = .x,
                                                   x_axis = rearers,
                                                   y_axis = mean_rearing_growth_length,
                                                   x_lab =  "Count",
                                                   y_lab = "Growth (cm)",
                                                   color = run_day,
                                                   color_lab = "Run Day",
                                                   title = .x$Species[1])) %>% 
  wrap_plots(ncol = 1, widths = plot_widths,
             heights = length(detailed_data_list) * plot_widths)

# X11()
# print(count_v_length_plot)

mortality_plot = ggplot(data = mortality_breakdown) +
  theme_classic(base_size = 20) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  labs(x = "Cause", y = "Mortality Counts") +
  geom_bar(aes(x = Cause, y = Count, fill = Species),
           stat="identity", position=position_dodge()) +
  scale_fill_manual(values = cbPalette)
# X11()
# print(mortality_plot)
  
##### Save things #####
plot_list = list(rearing_plot,
                 growth_plot,
                 count_v_growth_plot,
                 count_v_length_plot,
                 mortality_plot)
plot_name_list = list("abm_rearing_plot",
                      "abm_growth_plot",
                      "abm_count_v_growth_plot",
                      "abm_count_v_length_plot",
                      "abm_mortality_plot")
plot_dimeshions = list((length(detailed_data_list)) * plot_widths,
                       (length(detailed_data_list)) * plot_widths,
                       (length(detailed_data_list)) * plot_widths,
                       (length(detailed_data_list)) * plot_widths,
                        plot_widths)

table_list = list(summary_table)
table_name_list = list("abm_summary_table")

object_list = c(plot_list, table_list)
object_name_list = c(plot_name_list, table_name_list) 

walk2(object_list, object_name_list, ~saveRDS(
  object = .x,
  file = here(output_temp_folder, paste0(.y, ".rds"))))

# Save for future use
pwalk(list(plot_list, plot_name_list, plot_dimeshions), ~ggsave(
  plot = ..1,
  height = ..3,
  filename = here(output_temp_folder, paste0(..2, ".png")),
  limitsize = FALSE,
  device = "png"))

# save as output
pwalk(list(plot_list, plot_name_list, plot_dimeshions), ~ggsave(
  plot = ..1,
  height = ..3,
  filename = here(output_folder, paste0(..2, ".png")),
  limitsize = FALSE,
  device = "png"))

# Move over the abm outputs to the output folder
write.csv(detailed_data_temp,
          file = here(output_folder, "abm_detailed_pop_output.csv"))
write.csv(cell_data_temp,
          file = here(output_folder, "abm_cell_info_output.csv"))
write.csv(event_data_temp,
          file = here(output_folder, "abm_events_output.csv"))
