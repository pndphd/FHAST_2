################################################################################
# This script checks for all necessary libraries (packages) to 
# run the R parts of FHAST. If not installed it installs them.
# It then loads the libraries 
################################################################################

# Make a function to insatll packages/libraries
install_all = function(package){
  if(!require(package, character.only = T)){
    install.packages(package)
    library(package, character.only = T)
  }
}

# This is a list of packages to check for and install any missing ones
packages = c(
  # Control Libraries
  "readr",
  "tictoc",
  "fs",
  "knitr",
  "R.utils",
  
  # Data manipulate libraries
  "tibble",
  "dplyr",
  "tidyr",
  "forcats",
  "stringr",
  "lubridate",
  "data.table",
  
  # Programming and processing
  "purrr",
  "future",
  "furrr",
  "parallel",
  "igraph", # for adult pathfinding algorithm
  
  # GIS libraries
  "sf",
  "lutz", # used to get time zones
  "shadow",
  "suntools",
  "smoothr",
  "exactextractr",
  "raster",
  "terra",
  
  # Data viz libraries 
  "ggplot2",
  "viridis",
  "patchwork",
  "leaflet",
  
  # Netlogo control library
  "nlrx"
)

# install any missing packages and load all packages
lapply(X = packages, FUN = function(x) install_all(x))
rm(packages)

# Load the tools package this is not installed automatically
library(tools)

# make sure select is the dplyr call not the raster package call
select = dplyr::select


################################################################################
# End
################################################################################
