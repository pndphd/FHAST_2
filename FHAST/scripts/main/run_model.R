################################################################################
# Runs all the scripts for FHAST calculations
################################################################################

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
# Remove variable no longer needed
rm(preview_flag)

# Make the grid 
message("Making model grid.\n")
source(here("scripts","make_grid","make_grid.R"))
message("Making model grid: Done.\n")

# Calculate shade
message("Making shade file.\n")
shade_error = FALSE
tryCatch(suppressWarnings(source(here("scripts","make_shade","make_shade.R"))),
         error = function(e) {
           print(e)
           shade_error = TRUE
         })
if (shade_error) {
  stop('Error while generating shade, check canopy shape file, cover shape file, and wildcard file.')
}
rm(shade_error)
message("Making shade file: Done.\n")

# Sample the flow rasters onto the grid
message("Sampling rasters.\n")
source(here("scripts","sample_rasters","sample_rasters.R"))
message("Sampling rasters: Done.\n")

# Sample the cover shapes onto the grid
message("Sampling shape files.\n")
source(here("scripts","sample_shapes","sample_shapes.R"))
message("Sampling shape files: Done.\n")

# Clean up memory
gc()

################################################################################
# End
################################################################################
