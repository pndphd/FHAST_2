########################################
# This script loads all the files and formats parameters fo rthe rest of the run
########################################

##### Load Functions #####
source(here("scripts", "convert_parameters", "convert_parameters_functions.R"))

##### Initial file checks ######
# make a list of all the inputs that must exist
input_paths = list(ml$path$center_line,
                   ml$path$top_marker,
                   ml$path$canopy,
                   ml$path$tree_growth,
                   ml$path$cover,
                   ml$path$daily,
                   ml$path$fish_pop,
                   ml$path$fish_parms,
                   ml$path$predator,
                   ml$path$hab,
                   ml$path$interaction)

# Check if they exist
walk(input_paths, ~check_file_exists(.x))

##### Copy over some to be printed in reports #####


file.copy(ml$path$daily, here(output_temp_folder, "daily_input.txt"), overwrite = TRUE)
file.copy(ml$path$interaction, here(output_temp_folder, "interactions_input.txt"), overwrite = TRUE)
file.copy(ml$path$fish_pop, here(output_temp_folder, "population_input.txt"), overwrite = TRUE)
file.copy(ml$path$fish_parms, here(output_temp_folder, "fish_input.txt"), overwrite = TRUE)
file.copy(ml$path$hab, here(output_temp_folder, "habitat_input.txt"), overwrite = TRUE)
file.copy(ml$path$predator, here(output_temp_folder, "predator_input.txt"), overwrite = TRUE)
file.copy(ml$path$notes, here(output_temp_folder, "notes.txt"), overwrite = TRUE)

##### Read in the files #####
cover_shape <- st_read(ml$path$cover, quiet = TRUE)
base_crs <- st_crs(cover_shape)
grid_center_line <- st_read(ml$path$center_line, quiet = TRUE) %>% 
  st_zm() %>% 
  st_transform(base_crs)
grid_top_marker <- st_read(ml$path$top_marker, quiet = TRUE) %>% 
  st_zm() %>% 
  st_transform(base_crs)
canopy_shape <- st_read(ml$path$canopy, quiet = TRUE)
tree_growth_parms_in <- read.csv(file = ml$path$tree_growth, sep = ",", header = TRUE)
daily_inputs <- load_text_file(ml$path$daily)
fish_daily_inputs <- read.csv(file = ml$path$fish_pop, sep = ",", header = TRUE) %>%
  mutate(date = mdy(date))
fish_parm_temp <- read_csv(file = ml$path$fish_parms,
                           col_types = cols(.default = "d", species = "c"),
                           progress = FALSE)
pred_parm_temp <- read_csv(file = ml$path$predator,
                           col_types = cols(.default = "d", species = "c"),
                           progress = FALSE) %>%
  rename(term = species) %>%
  mutate(term = str_remove(term, "pred_glm_"))
hab_parm_temp <- load_text_file(ml$path$hab)
int_parm_temp <- load_text_file(ml$path$interaction)

if (!is.na(ml$path$aoi)) {
  aoi_shape <- st_read(ml$path$aoi, quiet = TRUE) %>% 
    st_zm() %>% 
    st_transform(base_crs)
}

##### Check and format shape files #####
# Check that these are the same crs
if (!compareCRS(grid_center_line, grid_top_marker) |
    !compareCRS(canopy_shape, grid_top_marker) |
    !compareCRS(canopy_shape, cover_shape)){
  stop('The CRSs of aome shape files are not the same.')
}

# Check the the center line is one object
if (NROW(grid_center_line) != 1)
  stop('The river center line shape file is a multipart object.\n
       It must be a single part object.')

# replace the wild card values 
if("wildcard" %in% cover_shape$class){

  wildError <<- FALSE
  tryCatch(check_file_exists(ml$path$wild),
           error = function(e) {
             print(e)
             wildError <<- TRUE
           })
  if (wildError) {
    message(paste0("\n!!!!!!!!!!!\n",
                "!!!ERROR!!! Wildcards present in cover file but no wildcard file provided. \n",
                "!!!!!!!!!!!\n"))
  }

  wild_values = read_csv(ml$path$wild, show_col_types = FALSE)
  wild_shape = cover_shape %>% 
    filter(class == "wildcard") 

  replace_cover = function(df, variable){
    df_out = df %>% 
      mutate(across(any_of(variable), ~ wild_values[,variable][[1]]))
  }
  
  wild_shape_new = names(wild_values) %>% 
    reduce(~replace_cover(df = .x, variable = .y),
           .init = wild_shape)
  cover_shape = cover_shape %>% 
    filter(class != "wildcard") %>% 
    bind_rows(wild_shape_new)
}


##### Convert into usable formats #####
# fish parameters to named list with species as index
# get the species used in the run
species_used = c(unique(fish_daily_inputs$species))
fish_parm <- fish_parm_temp %>%
  # the 1 ensures the names are kept
  select(1,any_of(species_used)) %>%
  rename(species_temp = species) %>%
  pivot_longer(cols=c(-species_temp), names_to="specie")%>%
  pivot_wider(names_from=c(species_temp)) %>%
  as.list() %>%
  calculate_adult_parameters() %>%
  append(get_swim_speed_parameters_for_all_species(.))

# tree growth parameters pivot longer and wider to format
tree_growth_parms <- tree_growth_parms_in %>%
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
         d = as.numeric(d),)

# Convert some logistic parameters to slope and intercept
# habitat and interaction parameters
turbidity_params <- convert_logistic_parameters(
  int_parm_temp["turbidity cover 10", ],
  int_parm_temp["turbidity cover 90", ]
)
dis_to_cover_params <- convert_logistic_parameters(
  int_parm_temp["distance to cover 10", ],
  int_parm_temp["distance to cover 90", ]
)

habitat_parm <- tibble(
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


# Predator parameters
# make lists of parameters per file, so the dataframe can be separated appropriately
log_model_par_names <- c("int", "shade", "veg",
                         "wood", "depth", "velocity", "substrate")
temp_model_par_names <- c("area_pred_10", "area_pred_90")
gape_par_names <- c("gape_a", "gape_b")
length_dist_par_names <- c("pred_length_mean", "pred_length_sd")

# combined all parameter lists into a list of lists to use with map
par_lol <- list(log_model_par_names,
                temp_model_par_names,
                gape_par_names,
                length_dist_par_names)

# make a list of separate dataframes
models_separated <- map(par_lol, ~ pred_parm_temp %>%
                          filter(term %in% .x))

# reshape data depending on needs
longer <- map(
  list(
    models_separated[[1]],
    models_separated[[4]]
  ),
  params_pivot_longer
)
wider <- map(
  list(
    models_separated[[2]],
    models_separated[[3]]
  ),
  params_pivot_wider
)

# make a list of lists into a single list
df_list <- flatten(list(longer, wider))

# final reshape to the length distribution model params
df_list[[2]] <- df_list[[2]] %>%
  pivot_wider(names_from = "term", values_from = "estimate")

# variable names
pred_output_names <- list(
  "pred_model_params",
  "pred_length_data",
  "pred_temp_params",
  "gape_params"
)

# assign the variables
walk2(df_list, pred_output_names, make_variables)

# convert logistic parameters in the temperature model
converted_pred_temperature_par <- convert_logistic_parameters(
  pred_temp_params$area_pred_10,
  pred_temp_params$area_pred_90
)

pred_temp_params <- tibble(
  area_pred_a = converted_pred_temperature_par$log_a,
  area_pred_b = converted_pred_temperature_par$log_b
)

##### Make predator models for habitat summary #####
# for models related to cover, an lm() object is rebuilt
# using fake data and the model params

# make a dataframe with fake x values and predicted values
synth_cover_data <- tibble(
  pct_cover = seq(0.01, 0.99, 0.01),
  dis_to_cover_m = habitat_parm$int_pct_cover +
    habitat_parm$sqrt_pct_cover * sqrt(pct_cover) +
    habitat_parm$pct_cover * pct_cover +
    habitat_parm$sqrt_pct_cover_x_pct_cover * pct_cover ^ 1.5)

# build the model object
pct_cover_model <- lm(dis_to_cover_m ~ pct_cover * sqrt(pct_cover),
                      data = synth_cover_data)

# model params for the model converting distance to cover to safety from predation
synth_cover_benefit_data <- tibble(
  dis_to_cover_m = seq(0, 5, 0.1),
  unitless_y = 1 / (1 + exp(-1 * (dis_to_cover_m * habitat_parm$dis_to_cover_m +
                                    habitat_parm$dis_to_cover_int))))

cover_ben_model <- glm(unitless_y ~ dis_to_cover_m,
                       data = synth_cover_benefit_data,
                       family = stats::quasibinomial(logit))

##### Write the files for NetLogo #####
# Write the fish parameters
write_csv(fish_parm_temp,
          file = here(temp_folder, "fish_params_input.csv"),
          progress = FALSE)

# Write the habitat parameters
write_csv(habitat_parm %>%
            mutate(across(where(is.numeric), as.character)) %>%
            pivot_longer(cols = everything()),
          file = here(temp_folder, "habitat.csv"),
          progress = FALSE)

# Add the updated temperature model parameters to the predator params and save in Netlogo temp folder
pred_temp_params %>%
  map_dfr(rep, times = 2) %>%
  mutate(species = c("pikeminnow", "bass")) %>%
  pivot_longer(cols = area_pred_a:area_pred_b) %>%
  pivot_wider(names_from = species, values_from = value) %>%
  rename(term = name) %>%
  bind_rows(pred_parm_temp) %>%
  filter(!(term %in% temp_model_par_names)) %>%
  write_csv(here(temp_folder, basename(ml$path$predator)),
            progress = FALSE)

# Save the predation models
cover_models <- list(pct_cover_model, cover_ben_model)
cover_model_filenames <- list("pct_cov_convers_model.rds",
                              "dis_to_cov_model.rds")
walk2(cover_models, cover_model_filenames, write_rds_temp_folder)

##### Write RDS filed for the summary #####
saveRDS(unique(pred_model_params$species), file = here(output_temp_folder, "pred_list.rds"))
saveRDS(unique(fish_parm$specie), file = here(output_temp_folder, "fish_list.rds"))
saveRDS(habitat_parm, file = here(output_temp_folder, "habitat_parm.rds"))
saveRDS(fish_parm, file = here(output_temp_folder, "fish_parm.rds"))

