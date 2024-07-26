########################################
# Runs all the scripts for FHAST calculations
#
# This assumes you've run load_libraries and default_initializaiton
# (and possibly re-initialized to other inputs).
########################################

# Make the grid 
message("Making model grid.\n")
source(here("scripts","make_grid","make_grid.R"))
message("Making model grid: Done.\n")

# Calculate shade
message("Making shade file.\n")
shadeError <<- FALSE
tryCatch(suppressWarnings(source(here("scripts","make_shade","make_shade.R"))),
         error = function(e) {
           print(e)
           shadeError <<- TRUE
         })
if (shadeError) {
  stop('Error while generating shade, check canopy shape file, cover shape file, and wildcard file.')
}
message("Making shade file: Done.\n")

# Sample the flow rasters onto the grid
message("Sampling rasters.\n")
source(here("scripts","sample_rasters","sample_rasters.R"))
message("Sampling rasters: Done.\n")

# Sample the cover shapes onto the grid
message("Sampling shape files.\n")
source(here("scripts","sample_shapes","sample_shapes.R"))
message("Sampling shape files: Done.\n")
message("Starting NetLogo run.\n")


