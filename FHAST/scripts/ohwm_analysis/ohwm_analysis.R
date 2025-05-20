################################################################################
# This script takes two shape files (OHWM and project foot print) and gets
# overlap
################################################################################

##### Developer options ########################################################
# Uncomment for development to pick a specific file and run from IDE

if (!exists("pass_arguments")){
  pass_arguments = NULL
  pass_arguments[2] = "C:/Users/pndph/Desktop/Temp/test2/temporary/re_clip2_LAR_OHWM_18,500_cfs.shp"
  pass_arguments[3] = "C:/Users/pndph/Desktop/Temp/ARCF_C3A_project_features_test2.shp/ARCF_C3A_project_features_test2.shp"
  pass_arguments[1] = "C:/Users/pndph/Desktop/Temp/test2"
}

################################################################################

##### Run setup ################################################################

# # install and load the here package if necessary
if(!require(c("here"), character.only = T)){install.packages(package)}

# Load Libraries
source(here("scripts","main","load_libraries.R"))
 
# Make blank list
ml = list(var = list(),
          df = list(),
          plot = list(),
          path = list(),
          string = list(),
          sum = list(),
          table = list())

# Load Functions

# get the input and output folders
ml$path$output_folder = pass_arguments[1]
ml$path$output_temp_folder = ml$path$output_folder
ml$path$ohwm = pass_arguments[2]
ml$path$footprint = pass_arguments[3]

##### Read in data #############################################################
message("Read OHWM.\n")
ml$df$ohwm = st_read(ml$path$ohwm) %>% 
  select(geometry)
message("Read OHWM: Done.\n")
message("Read Footprint.\n")
ml$df$footprint = st_read(ml$path$footprint) %>% 
  rename_with(str_to_title, !matches("geometry")) %>% 
  select(Feature, Project) %>% 
  mutate(Inside = FALSE)
message("Read Footprint: Done.\n")
 
##### Process in and out footprint #############################################

# make feature lookup table
ml$df$lookup_table = ml$df$footprint %>% 
  select(Feature) %>% 
  st_drop_geometry() %>% 
  distinct() %>% 
  mutate(Type = 1:n())

message("Calculate Summaries.\n")

ml$df$footprint_in = ml$df$footprint %>% 
  st_intersection(ml$df$ohwm) %>% 
  mutate(Inside = TRUE)

ml$df$footprint_out = ml$df$footprint %>% 
  st_difference(ml$df$ohwm)

ml$df$footprint_out_dis = st_union(ml$df$footprint_out)

ml$df$footprint_in_dis = st_union(ml$df$footprint_in)

ml$df$footprint_processed = ml$df$footprint_out %>%  
  bind_rows(ml$df$footprint_in) %>% 
  mutate(area = st_area(.))

##### Make table and summary stats #############################################

# Make a summary tabel
ml$table$summary = ml$df$footprint_processed %>% 
  st_drop_geometry() %>% 
  group_by(Feature, Project, Inside) %>% 
  summarise(Area = as.numeric(round(sum(area),2))) %>% 
  filter(Area != 0) %>% 
  left_join(ml$df$lookup_table, by = "Feature") %>% 
  mutate(Feature = str_to_title(Feature))

# get the percent of total footprint in the ohwm
ml$var$percent_in = ml$table$summary %>% 
  group_by(Inside) %>% 
  summarise(area = sum(Area)) %>% 
  mutate(total = sum(area),
         percent = area*100/total) %>% 
  filter(Inside == TRUE) %>% 
  .$percent %>% 
  round(1)

# Get the total area  
ml$var$total_area = sum(ml$table$summary$Area)

# get the units
ml$var$measure_units = st_crs(ml$df$footprint_out_dis) %>%
    .$units

message("Calculate Summaries: Done.\n")

##### Make plot ################################################################

message("Make Plots.\n")

ml$plot$output_map = ggplot(data = ml$df$footprint_in %>% 
                      left_join(ml$df$lookup_table, by = "Feature") ) +
  theme_classic(base_size = 20) +
  theme(axis.text.x = element_text(angle = 90)) +
  geom_sf(aes(fill = factor(Type)), color = "black") +
  scale_fill_viridis_d(name = "Type") +
  geom_sf(data = ml$df$footprint_out_dis, fill = "white") 

ggsave(here(ml$path$output_folder, "ohwm_map.png"),
       ml$plot$output_map,
       height = 7,
       width = 7,
       units = "in",
       device = "png")

message("Make Plots: Done.\n")

##### Write Reports ############################################################

# make the html doc
message("Make OHWM report.\n")
rmarkdown::render(input = here("scripts", "ohwm_analysis", "ohwm_report.Rmd"),
                  output_format = "html_document",
                  output_file = here(ml$path$output_folder, "ohwm_report.html"),
                  quiet = TRUE)

message("Make OHWM report: Done.\n")

################################################################################
# End
################################################################################
