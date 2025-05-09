################################################################################
# This script takes two FHAST runs an makes a report of the differences
################################################################################

##### Developer options ########################################################
# Uncomment for development to pick a specific file and run from IDE
run_a = "C:/Users/pndph/Desktop/Temp/small_dist_chinook_outputs"
run_b = "C:/Users/pndph/Desktop/Temp/small_dist_chinook_2_outputs"
output_folder = "C:/Users/pndph/Desktop/Temp/compare"
################################################################################

##### Run setup ################################################################
# install and load the here package if necessary
if(!require(c("here"), character.only = T)){install.packages(package)}

# Get the path is running from the UI
# preview_flag = FALSE
# if (exists("pass_arguments")){
#   config_file_name = pass_arguments[1]
#   Sys.setenv(JAVA_HOME = here("jdk-11"))
#   if (pass_arguments[2] == "1"){
#     preview_flag = TRUE
#   }
# }

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

# Make the output folder
dir.create(output_folder)

##### Read in data #############################################################
ml_a = readRDS(here(run_a, "master_data_list.rds"))
ml_b = readRDS(here(run_b, "master_data_list.rds"))

##### Calculate differences ####################################################

# Just need one habitat parameter to get cutoffs
ml$df$habitat_parm = ml_a$df$habitat_parm
ml$df$fish_parms = ml_a$df$fish_parms
ml$df$palette = ml_a$df$palette
ml$var = ml_a$var

# Merge data
ml$table = map2(ml_a$table, ml_b$table, ~subtract_dfs(.x, .y))
ml$df$cover = subtract_dfs(ml_a$df$cover, ml_b$df$cover)  
ml$df$daily = subtract_dfs(ml_a$df$daily, ml_b$df$daily)
ml$df$daily_input = subtract_dfs(ml_a$df$daily_input, ml_b$df$daily_input)
ml$df$full_grid = subtract_dfs(ml_a$df$full_grid, ml_b$df$full_grid)
ml$df$full_habitat = subtract_dfs(ml_a$df$full_habitat, ml_b$df$full_habitat)
ml$df$adult_migration_energy_data = merge_adult_energy(ml_a$df$adult_migration_energy_data,
                                                       ml_b$df$adult_migration_energy_data)

ml$sum = map2(ml_a$sum, ml_b$sum, ~map2(.x, .y, ~subtract_dfs(.x, .y)))

# it adults are present
if (ml$var$adult_run == 1){
  ml$df$adult_migration_map_data = map2(ml_a$df$adult_migration_map_data,
                                        ml_b$df$adult_migration_map_data,
                                        ~subtract_dfs(.x, .y))
}

# if juveniules are present 
if (ml$var$juvenile_run == 1){
  ml$df$detailed_data = subtract_time_data(ml_a$df$detailed_data,
                                           ml_b$df$detailed_data,
                                           time_name = "date", "Species")
  ml$df$mortality_breakdown = subtract_dfs(ml_a$df$mortality_breakdown,
                                           ml_b$df$mortality_breakdown)
  ml$df$detailed_data_list = map2(ml_a$df$detailed_data_list,
                                  ml_b$df$detailed_data_list,
                                  ~subtract_time_data(.x, .y, "date", "Species"))
}

##### Run the scripts to make the reports ######################################
# A run the script to make the habitat report data
source(here("scripts","compare_runs","compare_habitat.R"))

# A run the script to make the juvenile report data
source(here("scripts","compare_runs","compare_juvenile.R"))

##### Print the reports ######################################

################################################################################
# End
################################################################################