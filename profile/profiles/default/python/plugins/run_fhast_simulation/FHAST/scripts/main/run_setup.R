########################################
# Run the initialization scripts which load libraries functions and set
# up the basic file structure 
########################################

# install and load the here package if necessary
if(!require(c("here"), character.only = T)){install.packages(package)}

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

