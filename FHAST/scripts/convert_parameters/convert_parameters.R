################################################################################
# This script loads all the files and formats parameters for the rest of the run
################################################################################

##### Load Functions ###########################################################
source(here("scripts", "convert_parameters", "convert_parameters_functions.R"))

##### Initial file checks ######################################################
# make a list of all the inputs that must exist
input_paths = list(ml$path$center_line,
                   ml$path$top_marker,
                   ml$path$cover,
                   ml$path$daily,
                   ml$path$fish_pop,
                   ml$path$fish_parms,
                   ml$path$predator,
                   ml$path$hab,
                   ml$path$interaction)

# Check if they exist
walk(input_paths, ~check_file_exists(.x))
rm(input_paths)

##### Read in the files ########################################################
ml$df$cover = st_read(ml$path$cover, quiet = TRUE)
ml$var$crs = st_crs(ml$df$cover)
ml$df$center_line = st_read(ml$path$center_line, quiet = TRUE) %>% 
  st_zm() %>% 
  st_transform(ml$var$crs)
ml$df$top_marker = st_read(ml$path$top_marker, quiet = TRUE) %>% 
  st_zm() %>% 
  st_transform(ml$var$crs)
ml$df$daily = load_text_file(ml$path$daily)
ml$df$fish_pop = read.csv(file = ml$path$fish_pop, sep = ",", header = TRUE) %>%
  mutate(date = mdy(date))
fish_parm_temp = read_csv(file = ml$path$fish_parms,
                          col_types = cols(.default = "d", species = "c"),
                          progress = FALSE)
pred_parm_temp = read_csv(file = ml$path$predator,
                          col_types = cols(.default = "d", species = "c"),
                          progress = FALSE) %>%
  rename(term = species) %>%
  mutate(term = str_remove(term, "pred_glm_"))
hab_parm_temp = load_text_file(ml$path$hab)
int_parm_temp = load_text_file(ml$path$interaction)

# load and reporject the AOI
if (!ml$path$aoi == "no_aoi") {
  ml$df$aoi <- st_read(ml$path$aoi, quiet = TRUE) %>% 
    st_zm() %>% 
    st_transform(ml$var$crs)
}

##### Check and format shape files #############################################
# Check that these are the same crs
if (ml$path$canopy == "no_canopy"){
  if (!compareCRS(ml$df$center_line, ml$df$top_marker) |
      !compareCRS(ml$df$cover, ml$df$top_marker)){
    stop('The CRSs of some shape files are not the same.')
    }
} else {
  ml$df$canopy = st_read(ml$path$canopy, quiet = TRUE)
  if (!compareCRS(ml$df$center_line, ml$df$top_marker) |
      !compareCRS(ml$df$canopy, ml$df$top_marker) |
      !compareCRS(ml$df$canopy, ml$df$cover)){
    stop('The CRSs of some shape files are not the same.')
    }

}

# Check the the center line is one object
if (NROW(ml$df$center_line) != 1)
  stop('The river center line shape file is a multipart object.\n
       It must be a single part object.')

##### Replace the wild card values #############################################
if("wildcard" %in% ml$df$cover$class){
  
  # Check to see if the file exists
  tryCatch(check_file_exists(ml$path$wild),
           error = function(e){
             message(paste0("\n!!!!!!!!!!!\n",
                            "!!!ERROR!!! Wildcards present in cover file but no wildcard file provided.\n",
                            "!!!!!!!!!!!\n"))})
  
  # make a function to replace the values
  replace_cover = function(df, variable){
    df_out = df %>% 
      mutate(across(any_of(variable), ~ wild_values[,variable][[1]]))
  }

  # replace the values
  wild_values = read_csv(ml$path$wild, show_col_types = FALSE)
  wild_shape = ml$df$cover %>% 
    filter(class == "wildcard") 
  wild_shape_new = names(wild_values) %>% 
    reduce(~replace_cover(df = .x, variable = .y),
           .init = wild_shape)
  ml$df$cover = ml$df$cover %>% 
    filter(class != "wildcard") %>% 
    bind_rows(wild_shape_new)
  rm(wild_values, wild_shape, wild_shape_new)
}

##### Convert into usable formats ##############################################
# Fish Parameters: to named list with species as index
ml$df$fish_parms = fish_parm_temp %>%
  # select species used in the run
  # the 1 ensures the names are kept
  select(1,any_of(c(unique(ml$df$fish_pop$species)))) %>%
  rename(species_temp = species) %>%
  pivot_longer(cols=c(-species_temp), names_to="specie")%>%
  pivot_wider(names_from=c(species_temp)) %>%
  as.list() %>%
  calculate_adult_parameters() %>%
  append(get_swim_speed_parameters_for_all_species(.))
rm(fish_parm_temp)

# Tree Growth Parameters: pivot longer and wider to format
if(!(ml$path$tree_growth == "no_growth")){
  ml$df$tree_growth_parms = read.csv(file = ml$path$tree_growth, sep = ",", header = TRUE) %>%
    pivot_longer(cols = !starts_with("species"), names_to = c ("item")) %>%
    pivot_wider(names_from = "species") %>%
    rename(species = item) %>%
    mutate(species = str_replace(species, "[.]", " "),
           d_max = as.numeric(d_max),
           h_max = as.numeric(h_max),
           g = as.numeric(g),
           a = as.numeric(a),
           b = as.numeric(b),
           c = as.numeric(c),
           d = as.numeric(d))
}

# Habitat Parameters: convert logistic parameters to slope and intercept
turbidity_params <- convert_logistic_parameters(
  int_parm_temp["turbidity cover 10", ],
  int_parm_temp["turbidity cover 90", ])
dis_to_cover_params <- convert_logistic_parameters(
  int_parm_temp["distance to cover 10", ],
  int_parm_temp["distance to cover 90", ])

# make habitat df
ml$df$habitat_parms <- tibble(
  # from the habitat file
  hab_bentic_ene = hab_parm_temp["benthic food energy density", ],
  hab_drift_ene = hab_parm_temp["drift food energy density", ],
  hab_benthic_hab = hab_parm_temp["benthic food habitat", ],
  cover_hab = hab_parm_temp["cover habitat", ],
  small_cover_hab = hab_parm_temp["small cover habitat", ],
  hab_drift_con = hab_parm_temp["drift food density", ],
  hab_bentic_con = hab_parm_temp["benthic food density", ],
  vel_cutoff = hab_parm_temp["velocity cutoff", ],
  dep_cutoff = hab_parm_temp["depth cutoff", ],
  resolution = hab_parm_temp["resolution", ],
  buffer = hab_parm_temp["buffer", ],
  pred_per_area = hab_parm_temp["predators per area", ],
  veg_growth_years = hab_parm_temp["vegetation growth years", ],
  # from the interaction file
  shelter_frac = int_parm_temp["cover velocity fraction", ],
  reaction_distance = int_parm_temp["temperature predator area baseline", ],
  t_area_effect = int_parm_temp["temperature predator area effect", ],
  int_pct_cover = int_parm_temp["percent cover intercept", ],
  sqrt_pct_cover = int_parm_temp["percent cover root", ],
  pct_cover = int_parm_temp["percent cover slope", ],
  sqrt_pct_cover_x_pct_cover = int_parm_temp["percent cover 3-2 root", ],
  dis_to_cover_m = dis_to_cover_params$log_b,
  dis_to_cover_int = dis_to_cover_params$log_a,
  turbidity_int = turbidity_params$log_a,
  turbidity_slope = turbidity_params$log_b,
  d84_size = int_parm_temp["d84 size", ],
  superind_ratio = int_parm_temp["superindividual ratio", ],
  ben_vel_height = int_parm_temp["benthic velocity height", ]) %>%
  # make everything which is a number a doubble
  mutate(across(!c(hab_benthic_hab, cover_hab, small_cover_hab), ~as.numeric(.)))  %>%
  # Do a calculation for the law of the wall
  # all the following hard coded constants from the
  # relationship for the law of the wall
  mutate(base_wall_factor = 0.07/0.41*log((ben_vel_height/d84_size)*(30/3.5))) %>% 
  mutate(
    across(
      .cols = matches(c("hab_benthic_hab", "cover_hab", "small_cover_hab")),
      .fns = ~str_replace_all(., "-", ",")))
rm(hab_parm_temp, int_parm_temp, turbidity_params, dis_to_cover_params)

# Predator Parameters
# convert the logistic parameters form 10 and 90% to solpes and intercepts
ml$df$pred_params = pred_parm_temp %>%
  filter(term %in% c("area_pred_10", "area_pred_90")) %>% 
  pivot_longer(cols = -term, names_to = "species") %>%
  pivot_wider(names_from = term) %>% 
  mutate(area_pred_a = convert_logistic_parameters(area_pred_10,
                                                   area_pred_90)[[1]],
         area_pred_b = convert_logistic_parameters(area_pred_10,
                                                   area_pred_90)[[2]]) %>% 
  select(-area_pred_10, -area_pred_90) %>% 
  pivot_longer(cols = c(area_pred_a, area_pred_b), names_to = "term") %>% 
  pivot_wider(names_from = species) %>% 
  bind_rows(pred_parm_temp) %>% 
  filter(!term %in% c("area_pred_10", "area_pred_90"))
rm(pred_parm_temp)

##### Write the files for NetLogo ##############################################
# Write the habitat parameters
write_csv(ml$df$habitat_parms %>%
            mutate(across(where(is.numeric), as.character)) %>%
            pivot_longer(cols = everything()),
          file = here(ml$path$output_temp_folder, "habitat.csv"),
          progress = FALSE)
write_csv(ml$df$pred_params,
          file = here(here(ml$path$output_temp_folder,
                           basename(ml$path$predator))),
          progress = FALSE)

################################################################################
# End
################################################################################