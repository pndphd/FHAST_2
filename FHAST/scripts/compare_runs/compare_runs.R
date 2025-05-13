################################################################################
# This script takes two FHAST runs an makes a report of the differences
################################################################################

##### Developer options ########################################################
# Uncomment for development to pick a specific file and run from IDE

if (!exists("pass_arguments")){
  pass_arguments = NULL
  pass_arguments[2] = "C:/Users/pndph/Desktop/Temp/small_dist_chinook_outputs"
  pass_arguments[3] = "C:/Users/pndph/Desktop/Temp/small_dist_chinook_2_outputs"
  pass_arguments[1] = "C:/Users/pndph/Desktop/Temp/compare"
}

################################################################################

##### Run setup ################################################################

# install and load the here package if necessary
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
source(here("scripts","compare_runs","compare_runs_functions.R"))
source(here("scripts", "make_habitat_summary", "habitat_summary_plot_functions.R"))
source(here("scripts", "make_habitat_summary", "habitat_summary_functions.R"))

# get the input and output folders
run_a = pass_arguments[2]
run_b = pass_arguments[3]
ml$path$output_folder = pass_arguments[1]
ml$path$output_temp_folder = ml$path$output_folder

##### Read in data #############################################################
message("Read Output 1.\n")
ml_a = readRDS(here(run_a, "master_data_list.rds"))
message("Read Output 1: Done.\n")
message("Read Output 2.\n")
ml_b = readRDS(here(run_b, "master_data_list.rds"))
message("Read Output 2: Done.\n")

##### Check if these can be compared ###########################################
message("Checking if comparable.\n")
source(here("scripts","compare_runs","check_runs.R"))
message("Checking if comparable: Done.\n")

##### Calculate differences ####################################################

message("Format Datasets.\n")
# Combine input files
file_names = c("daily_input.txt",
               "interactions_input.txt",
               "population_input.txt",
               "fish_input.txt",
               "habitat_input.txt",
               "predator_input.txt")

walk(file_names,
      ~merge_inputs(ml_a$path$output_temp_folder,
                  ml_b$path$output_temp_folder,
                  ml$path$output_folder,
                  file_name = .x))

merge_inputs(ml_a$path$output_folder,
             ml_b$path$output_folder,
             ml$path$output_folder,
             file_name = "input_file.txt")

# Just need one habitat parameter to get cutoffs
ml$df$habitat_parm = ml_a$df$habitat_parm
ml$df$fish_parms = ml_a$df$fish_parms
ml$df$palette = ml_a$df$palette
ml$df$habitat_parms = ml_a$df$habitat_parms
ml$df$fish_combos$species = ml_a$df$fish_combos$species
ml$var = ml_a$var
ml$path$output_temp_folder = ml_a$path$output_temp_folder

# Merge data
ml$table = map2(ml_a$table, ml_b$table, ~subtract_dfs(.x, .y))
ml$df$cover = subtract_dfs(ml_a$df$cover, ml_b$df$cover)  
ml$df$daily = subtract_dfs(ml_a$df$daily, ml_b$df$daily)
ml$df$daily_input = subtract_dfs(ml_a$df$daily_input, ml_b$df$daily_input)
ml$df$full_grid = subtract_group_data(ml_a$df$full_grid,
                                      ml_b$df$full_grid,
                                      groups = c("geometry"))
ml$df$full_habitat = subtract_group_data(ml_a$df$full_habitat,
                                         ml_b$df$full_habitat,
                                         groups = c("date", "geometry"))

ml$sum = map2(ml_a$sum, ml_b$sum, ~map2(.x, .y, ~subtract_sum(.x, .y)))

# it adults are present
if (ml$var$adult_run == 1){
  ml_a$df$adult_migration_map_data$geometry = NULL
  ml_b$df$adult_migration_map_data$geometry = NULL
  ml$df$adult_migration_map_data = map2(ml_a$df$adult_migration_map_data,
                                        ml_b$df$adult_migration_map_data,
                                        ~subtract_group_data(.x,
                                                             .y,
                                                             groups = c("geometry", "species")))
  ml$df$adult_migration_energy_data = merge_adult_energy(ml_a$df$adult_migration_energy_data,
                                                         ml_b$df$adult_migration_energy_data)
}

# if juveniules are present 
if (ml$var$juvenile_run == 1){
  ml$df$detailed_data = subtract_group_data(ml_a$df$detailed_data,
                                           ml_b$df$detailed_data,
                                           groups = c("date", "Species"))
  ml$df$mortality_breakdown = subtract_dfs(ml_a$df$mortality_breakdown,
                                           ml_b$df$mortality_breakdown)
  ml$df$detailed_data_list = map2(ml_a$df$detailed_data_list,
                                  ml_b$df$detailed_data_list,
                                  ~subtract_group_data(.x, .y,
                                                      groups = c("date", "Species")))
}

message("Format Datasets: Done.\n")

##### Run the scripts to make the reports ######################################
# A run the script to make the habitat report data
message("Combine Habitat Datasets.\n")
source(here("scripts","compare_runs","compare_habitat.R"))
message("Combine Habitat Datasets: Done.\n")

# A run the script to make the juvenile report data
if (ml$var$juvenile_run == TRUE){
  message("Combine Juvenile Datasets.\n")
  source(here("scripts","compare_runs","compare_juvenile.R"))
  message("Combine Juvenile Datasets: Done.\n")
}

# A run the script to make the adult report data
if (ml$var$adult_run == TRUE){
  message("Combine Adult Datasets.\n")
  source(here("scripts","compare_runs","compare_adults.R"))
  message("Combine Adult Datasets: Done.\n")
}

##### Print the reports ######################################
# make the html doc
message("Make Habitat Report.\n")
rmarkdown::render(input = here("scripts", "make_habitat_summary", "make_general_summary.Rmd"),
                  output_format = "html_document",
                  output_file = here(ml$path$output_folder, "report_general.html"),
                  quiet = TRUE)
message("Make Habitat Report: Done.\n")

if (ml$var$juvenile_run == TRUE){
  message("Make Juvenile Report.\n")
  rmarkdown::render(input = here("scripts", "make_habitat_summary", "make_juvenile_summary.Rmd"),
                    output_format = "html_document",
                    output_file = here(ml$path$output_folder, "report_juvenile_rearing.html"),
                    quiet = TRUE)
  message("Make Juvenile Report: Done.\n")
}

if (ml$var$adult_run == TRUE){
  message("Make Adult Report.\n")
  rmarkdown::render(input = here("scripts", "make_habitat_summary", "make_adult_summary.Rmd"),
                    output_format = "html_document",
                    output_file = here(ml$path$output_folder, "report_adult_migration.html"),
                    quiet = TRUE)
  message("Make Adult Report: Done.\n")
}

message("!!! REPORT COMPARE COMPLETE !!!\n")

################################################################################
# End
################################################################################