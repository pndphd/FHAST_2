########################################
# This is just a series or source calls of the scripts
# It will run the necessary files to initialize the FHAST program
# and then run the various fast scripts in order
########################################

# Uncoment for development to pick a specific file and run from IDE
# need an extra up level ".." to compensate for being in the default input directory 
# wild_card_file_name = "C:/Users/pndph/Documents/Research/Projects/FHAST/Work/calibration/sacramento_above_ar_con/michel_2015_1.txt"

##### Run the initialization scripts #####
# install and load the here package if necessary
if(!require(c("here"), character.only = T)){install.packages(package)}

# Get the path is running from the UI
preview_flag = FALSE
if (exists("pass_arguments")){
  wild_card_file_name = pass_arguments[1]
  Sys.setenv(JAVA_HOME = here("jdk-11"))
  if (pass_arguments[2] == "1"){
    preview_flag = TRUE
  }
}

##### Run the setup scripts #####
source(here("scripts","main","run_setup.R"))

##### Run the preview scripts #####
source(here("scripts","main","run_preview.R"))

# Stop run if we just want a preview
if (preview_flag){
  stop("PREVIEW RUN COMPLETE.\nThis is not an error.")  
}

##### Run the calculation scripts #####
source(here("scripts","main","run_model.R"))

##### Run NetLogo #####
# Shut off futures for this
# and only run if juvenile are present

if(juvenile_run == TRUE){
  future::plan(strategy = sequential)
  source(here("scripts", "netlogo", "NetLogo_Controller.R"))
  results <- run_netlogo_model(output_temp_folder)
  future::plan(strategy = multisession,
               workers = num_cores)
}

##### Run the post processing scripts #####
source(here("scripts","main","run_post.R"))
