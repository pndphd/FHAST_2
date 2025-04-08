########################################
# Runs all the scripts for FHAST preview calculations
#
# This assumes you've run load_libraries and default_initializaiton
# (and possibly re-initialized to other inputs).
########################################

# make output locations 
message("Making output folders.\n")
source(here("scripts","main","make_output_folder.R"))
message("Making output folders: Done.\n")

# load all the input files, make basic parameter files,
# also do some basic checking of files
message("Loading parameters.\n")
source(here("scripts","convert_parameters","convert_parameters.R"))
message("Loading parameters: Done.\n")

# Make the daily input file
message("Making daily environment file.\n")
source(here("scripts", "make_environ_daily_data","make_enviro_daily_data.R"))
message("Making daily environment file: Done.\n")

# Make the daily fish input file
message("Making daily fish file.\n")
source(here("scripts", "make_fish_daily_data","make_fish_daily_data.R"))
message("Making daily fish file: Done.\n")

# Make preview map
message("Making preview map.\n")
source(here("scripts","make_preview_map","make_preview_map.R"))
message("Making preview map: Done.\n")

# Stop run if we just want a preview
if (preview_flag){
  stop("PREVIEW RUN COMPLETE.\nThis is not an error.")  
}
# Remove variabel no longer needed
rm(preview_flag)

################################################################################
# End
################################################################################