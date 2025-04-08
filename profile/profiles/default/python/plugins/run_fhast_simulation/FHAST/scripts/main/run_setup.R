################################################################################
# Run the initialization scripts which load libraries functions and set
# up the basic file structure 
################################################################################

# install and load the here package if necessary
if(!require(c("here"), character.only = T)){install.packages(package)}

# Load Libraries
source(here("scripts","main","load_libraries.R"))

# Load some common functions used in running FHAST
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

################################################################################
# End
################################################################################
