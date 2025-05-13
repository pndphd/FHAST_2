################################################################################
# This script makes the functions form compare runs
################################################################################

# Check if both runs contain juveniles
if(ml_a$var$juvenile_run != ml_b$var$juvenile_run){
  message(paste0("!!!!!!!!!!!\n",
                 "!!!ERROR!!! One run contains juveniles an the other does not.\n",
                 "!!!!!!!!!!!\n"))
  stop()
}

# Check if both runs contain adults
if(ml_a$var$adult_run != ml_b$var$adult_run){
  message(paste0("!!!!!!!!!!!\n",
                 "!!!ERROR!!! One run contains adults an the other does not.\n",
                 "!!!!!!!!!!!\n"))
  stop()
}

# Check if the grids are the same
if(!(identical(ml_a$df$top_marker, ml_b$df$top_marker) &
     identical(ml_a$df$center_line, ml_b$df$center_line) &
     ml_a$df$habitat_parms$resolution == ml_b$df$habitat_parms$resolution &
     ml_a$df$habitat_parms$buffer == ml_b$df$habitat_parms$buffer)){
  message(paste0("!!!!!!!!!!!\n",
                 "!!!ERROR!!! The core grids are different between runs.\n",
                 "!!!!!!!!!!!\n"))
  stop()
}

# Check if start and end dates are the same
if(!(max(ml_a$df$daily_input$date) == max(ml_b$df$daily_input$date) &
     min(ml_a$df$daily_input$date) == min(ml_b$df$daily_input$date))){
  message(paste0("!!!!!!!!!!!\n",
                 "!!!ERROR!!! The start or end dates are different between runs.\n",
                 "!!!!!!!!!!!\n"))
  stop()
}


################################################################################
# End
################################################################################