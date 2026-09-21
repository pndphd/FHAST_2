################################################################################
# The script which setups the nlrx model run
################################################################################

# Gets the results from running the NetLogo model.
run_netlogo_model <- function(run_folder_path) {
  modelpath <- here("scripts","NetLogo","FHAST.nlogo")

  netLogoParams = load_text_file(here("NetLogoConfig.txt"))

  # Initialize NetLogo with the model
  nl <- nlrx::nl(nlversion = netLogoParams["Version", ],
                 nlpath = here(netLogoParams["NetLogoPath", ]),
                 modelpath = modelpath,
                 jvmmem = 2048)

  nl@experiment <- experiment(expname="modelrun",
                              outpath="",
                              repetition=1,
                              tickmetrics="false",
                              idsetup="setup",
                              idgo="go",
                              runtime=NA_integer_,
                              idfinal=NA_character_,
                              idrunnum=NA_character_,
                              variables = list(),
                              constants = list(run_folder = deparse(run_folder_path),
                                               "draw_fish_movements?" = "FALSE"),
                              metrics = c("count turtles"))
  nl@simdesign <- simdesign_simple(nl=nl,
                                   nseeds=1)
  # Evaluate nl object:
  nlrx::eval_variables_constants(nl)
  
  # Run all simulations (loop over all siminputrows and simseeds)
  results <- nlrx::run_nl_one(nl,
                              seed = 1,
                              siminputrow = 1)
}

################################################################################
# End
################################################################################