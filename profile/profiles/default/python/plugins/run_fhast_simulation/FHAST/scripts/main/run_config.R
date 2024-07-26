
initial.options = commandArgs(trailingOnly=FALSE)

input_config_path = initial.options[which(initial.options == "--args") + 1]
initialWd = getwd()

file.arg.name <- "--file="
# Get the file name of the script we're running
script.name <- sub(file.arg.name, "", initial.options[grep(file.arg.name, initial.options)])
# Go up the path structure to the main FHAST base directory.
FHAST_base_dir <- dirname(dirname(dirname(script.name)))
# Set our working directory to the main FHAST directory so all of the source calls work.
setwd(FHAST_base_dir)
# Set the applibpath to the pre-downloaded packages
applibpath = file.path(getwd(), 'FHAST_app', 'app', 'library')
.libPaths(c(applibpath, .Library))

##### Run the initialization scripts #####
# install and load the here package if necessary
if(!require(c("here"), character.only = T)){
  install.packages(package)
}

# Load Libraries
source(here("scripts","main","load_libraries.R"))

# Load some common functions used in running FHAST
# Load some file handling functions
source(here("scripts", "fhast_functions", "fhast_file_functions.R"))
# Load some file basic math functions
source(here("scripts", "fhast_functions", "fhast_math_functions.R"))
# Load some file basic biology functions
source(here("scripts", "fhast_functions", "fhast_biology_functions.R"))
# Load some plotting functions
source(here("scripts", "fhast_functions", "fhast_plot_functions.R"))

# Sets up the file structure for FHAST run
source(here("scripts", "main", "set_fhast_file_structure.R"))

# Run the initialization 
source(here("scripts","main","initialize_fhast.R"))

# Get the path for the config file out of the arguments.
configFile = ifelse(isAbsolutePath(input_config_path),
                    input_config_path,
                    file.path(initialWd, input_config_path))


# Initialize fhast variables to the inputs in the UI.
initialize_fhast(configFile)

source(here("scripts","convert_parameters","convert_parameters.R"))

# Run the model
source(here("scripts", "main", "run_model.R"))

##### Run NetLogo #####
# Shut off futures for this
if(juvenile_run == TRUE){
  future::plan(strategy = sequential)
  source(here("scripts", "netlogo", "NetLogo_Controller.R"))
  results <- run_netlogo_model()
  future::plan(strategy = multisession,
               workers = num_cores)
}

##### Run the post processing scripts #####
source(here("scripts","main","run_post.R"))
