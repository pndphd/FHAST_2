################################################################################
# Run the initialization scripts which load libraries functions and set
# up the basic file structure 
################################################################################

# install and load the here package if necessary
if(!require(c("here"), character.only = T)){install.packages(package)}

# Load Libraries
source(here("scripts","main","load_libraries.R"))

# Load some common functions used in running FHAST
message("Loading functions.\n")
# Load some file handling functions
source(here("scripts", "fhast_functions", "file_functions.R"))
# Load some file basic math functions
source(here("scripts", "fhast_functions", "math_functions.R"))
# Load some file basic biology functions
source(here("scripts", "fhast_functions", "biology_functions.R"))
# Load some plotting functions
source(here("scripts", "fhast_functions", "plot_functions.R"))

# Run the initialization 
source(here("scripts","main","initialize.R"))
message("Loading functions: Done.\n")

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

################################################################################
# End
################################################################################