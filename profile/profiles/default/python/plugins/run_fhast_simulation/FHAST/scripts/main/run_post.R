########################################
# Runs all the scripts for FHAST data post processing
########################################

# Make the habitat summary file
message("NetLogo run finished.\n")
message("Running post-processing.\n")
source(here("scripts", "make_habitat_summary", "make_habitat_summary.R")) 

if (juvenile_run == TRUE){
  # Make the ABM summary file
  source(here("scripts", "make_abm_summary", "make_abm_summary.R"))
}

# make the html doc
rmarkdown::render(input = here("scripts", "make_habitat_summary", "make_general_summary.Rmd"),
                  output_format = "html_document",
                  output_file = here(output_folder, "report_general.html"))

if (juvenile_run == TRUE){
  rmarkdown::render(input = here("scripts", "make_habitat_summary", "make_juvenile_summary.Rmd"),
                   output_format = "html_document",
                   output_file = here(output_folder, "report_juvenile_rearing.html") )
}

if (adult_run == TRUE){
  rmarkdown::render(input = here("scripts", "make_habitat_summary", "make_adult_summary.Rmd"),
                    output_format = "html_document",
                    output_file = here(output_folder, "report_adult_migration.html") )
}

message("!!! FHAST RUN COMPLETE !!!\n")
################
# RUN COMPLETE #
################
