################################################################################
# Runs the scripts for FHAST preview generation
################################################################################

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

################################################################################
# End
################################################################################