################################################################################
# Runs all the scripts for FHAST data post processing
################################################################################

# Make the habitat summary file
message("NetLogo run finished.\n")
message("Running post-processing.\n")
source(here("scripts", "make_habitat_summary", "make_habitat_summary.R")) 
source(here("scripts", "make_habitat_summary", "make_habitat_plots.R"))
source(here("scripts", "make_habitat_summary", "save_habitat_summary.R"))


if (ml$var$juvenile_run == TRUE){
  # Make the ABM summary file
  source(here("scripts", "make_abm_summary", "make_abm_summary.R"))
}

# Write the main data file
saveRDS(ml, here(ml$path$output_folder, "master_data_list.rds"))

# make the html doc
rmarkdown::render(input = here("scripts", "make_habitat_summary", "make_general_summary.Rmd"),
                  output_format = "html_document",
                  output_file = here(ml$path$output_folder, "report_general.html"),
                  quiet = TRUE)

message("Habitat report finished.\n")

if (ml$var$juvenile_run == TRUE){
  rmarkdown::render(input = here("scripts", "make_habitat_summary", "make_juvenile_summary.Rmd"),
                   output_format = "html_document",
                   output_file = here(ml$path$output_folder, "report_juvenile_rearing.html"),
                   quiet = TRUE)
  message("Juvenile report finished.\n")
}

if (ml$var$adult_run == TRUE){
  rmarkdown::render(input = here("scripts", "make_habitat_summary", "make_adult_summary.Rmd"),
                    output_format = "html_document",
                    output_file = here(ml$path$output_folder, "report_adult_migration.html"),
                    quiet = TRUE)
  message("Adult report finished.\n")
}

message("!!! FHAST RUN COMPLETE !!!\n")

################################################################################
# RUN COMPLETE
# End
################################################################################
