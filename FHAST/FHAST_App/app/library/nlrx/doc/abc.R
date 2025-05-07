## ----setup, include = FALSE---------------------------------------------------
knitr::opts_chunk$set(
  collapse = TRUE,
  comment = "#>"
)

## ----eval=FALSE---------------------------------------------------------------
#  library(nlrx)
#  # Windows default NetLogo installation path (adjust to your needs!):
#  netlogopath <- file.path("C:/Program Files/NetLogo 6.0.3")
#  modelpath <- file.path(netlogopath, "app/models/Sample Models/Biology/Wolf Sheep Predation.nlogo")
#  outpath <- file.path("C:/out")
#  # Unix default NetLogo installation path (adjust to your needs!):
#  netlogopath <- file.path("/home/NetLogo 6.0.3")
#  modelpath <- file.path(netlogopath, "app/models/Sample Models/Biology/Wolf Sheep Predation.nlogo")
#  outpath <- file.path("/home/out")
#  
#  nl <- nl(nlversion = "6.0.3",
#           nlpath = netlogopath,
#           modelpath = modelpath,
#           jvmmem = 1024)

## ----eval=FALSE---------------------------------------------------------------
#  nl@experiment <- experiment(expname="wolf-sheep",
#                              outpath=outpath,
#                              repetition=1,
#                              tickmetrics="false",
#                              idsetup="setup",
#                              idgo="go",
#                              runtime=100,
#                              metrics=c("count sheep", "count wolves"),
#                              variables = list("sheep-gain-from-food" = list(min=2, max=6, qfun="qunif"),
#                                               "wolf-gain-from-food" = list(min=10, max=30, qfun="qunif")),
#                              constants = list('initial-number-sheep' = 100,
#                                               'initial-number-wolves' = 50,
#                                               "grass-regrowth-time" = 30,
#                                               "sheep-reproduce" = 4,
#                                               "wolf-reproduce" = 5,
#                                               "model-version" = "\"sheep-wolves-grass\"",
#                                               "show-energy?" = "false"))
#  

## ----eval=FALSE---------------------------------------------------------------
#  nl@simdesign <- simdesign_ABCmcmc_Marjoram(nl=nl,
#                                             summary_stat_target = c(100, 80),
#                                             n_rec = 100,
#                                             n_calibration=200,
#                                             use_seed = TRUE,
#                                             progress_bar = TRUE,
#                                             nseeds = 1)

## ----eval=FALSE---------------------------------------------------------------
#  post <- function(nl){
#    res <- getsim(nl, "simoutput") %>%
#      dplyr::select(getexp(nl, "metrics")) %>%
#      dplyr::summarise_each(list(max=max))
#    return(as.numeric(res))
#  }
#  
#  nl@simdesign <- simdesign_ABCmcmc_Marjoram(nl=nl,
#                                             postpro_function = post,
#                                             summary_stat_target = c(100, 80),
#                                             n_rec = 100,
#                                             n_calibration=200,
#                                             use_seed = TRUE,
#                                             progress_bar = TRUE,
#                                             nseeds = 1)

## ----eval=FALSE---------------------------------------------------------------
#  results <- run_nl_dyn(nl, seed = nl@simdesign@simseeds[1])

## ----eval=FALSE---------------------------------------------------------------
#  setsim(nl, "simoutput") <- results
#  saveRDS(nl, file.path(nl@experiment@outpath, "ABCmcmc.rds"))
#  
#  ## Calculate descriptive statistics
#  getsim(nl, "simoutput") %>% # get simulation results from nl object
#    dplyr::select(param) %>% # select param column
#    tidyr::unnest(cols=param) %>%  # unnest param column
#    dplyr::summarise_each(list(min=min, max=max, mean=mean, median=median)) %>% # calculate statistics
#    tidyr::gather(parameter, value) %>% # convert to long format
#    tidyr::separate(parameter, into = c("parameter", "stat"), sep = "_") %>% # seperate parameter name and statistic
#    tidyr::spread(stat, value) # convert back to wide format
#  
#  ## Plot histogram of parameter sampling distribution:
#  getsim(nl, "simoutput") %>% # get simulation results from nl object
#    dplyr::select(param) %>% # select param column
#    tidyr::unnest(cols=param) %>%  # unnest param column
#    tidyr::gather(parameter, value) %>% # convert to long format
#    ggplot2::ggplot() + # plot histogram with a facet for each parameter
#    ggplot2::facet_wrap(~parameter, scales="free") +
#    ggplot2::geom_histogram(ggplot2::aes(x=value), bins = 40)
#  
#  ## Plot density of parameter sampling distribution:
#  getsim(nl, "simoutput") %>% # get simulation results from nl object
#    dplyr::select(param) %>% # select param column
#    tidyr::unnest(cols=param) %>% # unnest param column
#    tidyr::gather(parameter, value) %>% # convert to long format
#    ggplot2::ggplot() + # plot density with a facet for each parameter
#    ggplot2::facet_wrap(~parameter, scales="free") +
#    ggplot2::geom_density(ggplot2::aes(x=value, fill=parameter))
#  
#  ## Get best parameter combinations and corresponding function values
#  getsim(nl, "simoutput") %>%  # get simulation results from nl object
#    dplyr::select(dist,epsilon) %>%  # select dist and epsilon columns
#    tidyr::unnest(cols=c(dist,epsilon)) %>%  # unnest dist and epsilon columns
#    dplyr::mutate(runID=dplyr::row_number()) %>% # add row ID column
#    dplyr::filter(dist == epsilon) %>% # only keep runs with dist=epsilon
#    dplyr::left_join(getsim(nl, "simoutput") %>% # join parameter values of best runs
#                       dplyr::select(param) %>%
#                       tidyr::unnest(cols=param) %>%
#                       dplyr::mutate(runID=dplyr::row_number())) %>%
#    dplyr::left_join(getsim(nl, "simoutput") %>% # join output values best runs
#                       dplyr::select(stats) %>%
#                       tidyr::unnest(cols=stats) %>%
#                       dplyr::mutate(runID=dplyr::row_number())) %>%
#    dplyr::select(runID, dist, epsilon, dplyr::everything()) # update order of columns
#  
#  ## Analyse mcmc using coda summary and plot functions:
#  summary(coda::as.mcmc(getsim(nl, "simoutput") %>%
#                          dplyr::select(param) %>%
#                          tidyr::unnest(cols=param)), quantiles =c(0.05,0.95,0.5))
#  
#  plot(coda::as.mcmc(getsim(nl, "simoutput") %>%
#                          dplyr::select(param) %>%
#                          tidyr::unnest(cols=param)))
#  

## ----eval=FALSE---------------------------------------------------------------
#  library(nlrx)
#  # Windows default NetLogo installation path (adjust to your needs!):
#  netlogopath <- file.path("C:/Program Files/NetLogo 6.0.3")
#  modelpath <- file.path(netlogopath, "app/models/Sample Models/Biology/Wolf Sheep Predation.nlogo")
#  outpath <- file.path("C:/out")
#  # Unix default NetLogo installation path (adjust to your needs!):
#  netlogopath <- file.path("/home/NetLogo 6.0.3")
#  modelpath <- file.path(netlogopath, "app/models/Sample Models/Biology/Wolf Sheep Predation.nlogo")
#  outpath <- file.path("/home/out")
#  
#  nl <- nl(nlversion = "6.0.3",
#           nlpath = netlogopath,
#           modelpath = modelpath,
#           jvmmem = 1024)

## ----eval=FALSE---------------------------------------------------------------
#  nl@experiment <- experiment(expname="wolf-sheep",
#                              outpath=outpath,
#                              repetition=1,
#                              tickmetrics="false",
#                              idsetup="setup",
#                              idgo="go",
#                              runtime=100,
#                              metrics=c("count sheep", "count wolves"),
#                              variables = list("sheep-gain-from-food" = list(min=2, max=6, qfun="qunif"),
#                                               "wolf-gain-from-food" = list(min=10, max=30, qfun="qunif")),
#                              constants = list('initial-number-sheep' = 100,
#                                               'initial-number-wolves' = 50,
#                                               "grass-regrowth-time" = 30,
#                                               "sheep-reproduce" = 4,
#                                               "wolf-reproduce" = 5,
#                                               "model-version" = "\"sheep-wolves-grass\"",
#                                               "show-energy?" = "false"))
#  

## ----eval=FALSE---------------------------------------------------------------
#  nl@simdesign <- simdesign_lhs(nl,
#                                samples=500,
#                                nseeds=1,
#                                precision=3)

## ----eval=FALSE---------------------------------------------------------------
#  results <- run_nl_all(nl)

## ----eval=FALSE---------------------------------------------------------------
#  setsim(nl, "simoutput") <- results
#  saveRDS(nl, file.path(nl@experiment@outpath, "ABClhs.rds"))

## ----eval=FALSE---------------------------------------------------------------
#  input <- getsim(nl, "siminput") %>%
#    dplyr::select(names(getexp(nl, "variables")))
#  output <- getsim(nl, "simoutput") %>%
#    dplyr::select(getexp(nl, "metrics"))
#  target <- c("count sheep"=100, "count wolves"=80)

## ----eval=FALSE---------------------------------------------------------------
#  results.abc.reject <- abc::abc(target=target,
#                          param=input,
#                          sumstat=output,
#                          tol=0.3,
#                          method="rejection")
#  
#  results.abc.loclin <- abc::abc(target=target,
#                                 param=input,
#                                 sumstat=output,
#                                 tol=0.3,
#                                 method="loclinear")

## ----eval=FALSE---------------------------------------------------------------
#  results.abc.all <- tibble::as_tibble(results.abc.reject$unadj.values) %>% # results from rejection method
#    tidyr::gather(parameter, value) %>%
#    dplyr::mutate(method="rejection") %>%
#    dplyr::bind_rows(tibble::as_tibble(results.abc.loclin$adj.values) %>% # results from local linear regression method
#                       tidyr::gather(parameter, value) %>%
#                       dplyr::mutate(method="loclinear")) %>%
#    dplyr::bind_rows(input %>%                # initial parameter distribution (lhs)
#                       tidyr::gather(parameter, value) %>%
#                       dplyr::mutate(method="lhs"))
#  
#  ggplot2::ggplot(results.abc.all) +
#    ggplot2::facet_grid(method~parameter, scales="free") +
#    ggplot2::geom_histogram(ggplot2::aes(x=value))
#  
#  ggplot2::ggplot(results.abc.all) +
#    ggplot2::facet_wrap(~parameter, scales="free") +
#    ggplot2::geom_density(ggplot2::aes(x=value, fill=method), alpha=0.1)
#  

