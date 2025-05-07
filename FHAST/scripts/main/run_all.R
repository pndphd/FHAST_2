################################################################################
# This is just a series or source calls of the scripts
# It will run the necessary files to initialize the FHAST program
# and then run the various FHAST scripts in order
################################################################################

##### Developer options ########################################################
# do you want to print plots
print_plots = FALSE
# what width do you want the default plots 
plot_width = 5
# Set the random seed
set.seed(6806665)

# Uncomment for development to pick a specific file and run from IDE
config_file_name = "C:/Users/pndph/Desktop/Temp/small_dist_chinook_outputs/config.txt"
################################################################################

##### Run the initialization scripts #####
# install and load the here package if necessary
if(!require(c("here"), character.only = T)){install.packages(package)}

# Get the path is running from the UI
preview_flag = FALSE
if (exists("pass_arguments")){
  config_file_name = pass_arguments[1]
  Sys.setenv(JAVA_HOME = here("jdk-11"))
  if (pass_arguments[2] == "1"){
    preview_flag = TRUE
  }
}

##### Run the setup scripts #####
source(here("scripts","main","run_setup.R"))

##### Run the calculation scripts #####
source(here("scripts","main","run_model.R"))

##### Run NetLogo #####
# Shut off futures for this
# and only run if juvenile are present
if(ml$var$juvenile_run == TRUE){
  message("Starting NetLogo run.\n")
  future::plan(strategy = sequential)
  source(here("scripts", "netlogo", "NetLogo_Controller.R"))
  run_netlogo_model(ml$path$output_temp_folder)
  future::plan(strategy = multisession,
               workers = pick_num_cores())
}

##### Run the post processing scripts #####
source(here("scripts","main","run_post.R"))

################################################################################
# End
################################################################################