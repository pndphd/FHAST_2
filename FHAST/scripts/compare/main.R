#############################################################
# This is the script to take data form 2 
# completed runs and make reports that compare them
#############################################################

##### Run the initialization scripts #####
# install and load the here package if necessary
if(!require(c("here"), character.only = T)){install.packages(package)}

# Get the path is running from the UI
if (exists("pass_arguments")){
  run_1_folder = pass_arguments[1]
  run_2_folder = pass_arguments[2]
  new_folder = pass_arguments[3]
}

new_folder = "C:/Users/pndph/Desktop/Temp/out2"

##### Run the setup scripts #####
source(here("scripts","main","load_libraries.R"))

##### Capy over all the data #####
source(here("scripts","compare","copy_data.R"))