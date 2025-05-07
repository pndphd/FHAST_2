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
#  nl@experiment <- experiment(expname = "wolf-sheep-morris",
#                              outpath = outpath,
#                              repetition = 1,
#                              tickmetrics = "true",
#                              idsetup = "setup",
#                              idgo = "go",
#                              runtime = 500,
#                              evalticks = seq(300,500),
#                              metrics=c("count sheep", "count wolves", "count patches with [pcolor = green]"),
#                              variables = list("initial-number-sheep" = list(min=50, max=150, step=10, qfun="qunif"),
#                                               "initial-number-wolves" = list(min=50, max=150, step=10, qfun="qunif"),
#                                               "grass-regrowth-time" = list(min=0, max=100, step=10, qfun="qunif"),
#                                               "sheep-gain-from-food" = list(min=0, max=50, step=10, qfun="qunif"),
#                                               "wolf-gain-from-food" = list(min=0, max=100, step=10, qfun="qunif"),
#                                               "sheep-reproduce" = list(min=0, max=20, step=5, qfun="qunif"),
#                                               "wolf-reproduce" = list(min=0, max=20, step=5, qfun="qunif")),
#                              constants = list("model-version" = "\"sheep-wolves-grass\"",
#                                               "show-energy?" = "false"))

## ----eval=FALSE---------------------------------------------------------------
#  nl@simdesign <- simdesign_morris(nl=nl,
#                                   morristype="oat",
#                                   morrislevels=4,
#                                   morrisr=1000,
#                                   morrisgridjump=2,
#                                   nseeds=5)

## ----eval=FALSE---------------------------------------------------------------
#  library(future)
#  plan(multisession)
#  results <- run_nl_all(nl)

## ----eval=FALSE---------------------------------------------------------------
#  setsim(nl, "simoutput") <- results
#  saveRDS(nl, file.path(nl@experiment@outpath, "morris.rds"))

## ----eval=FALSE---------------------------------------------------------------
#  morris <- analyze_nl(nl)

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
#  nl@experiment <- experiment(expname = "wolf-sheep-morris",
#                              outpath = outpath,
#                              repetition = 1,
#                              tickmetrics = "true",
#                              idsetup = "setup",
#                              idgo = "go",
#                              runtime = 500,
#                              metrics=c("count sheep", "count wolves", "count patches with [pcolor = green]"),
#                              variables = list("initial-number-sheep" = list(min=50, max=150, step=10, qfun="qunif"),
#                                               "initial-number-wolves" = list(min=50, max=150, step=10, qfun="qunif"),
#                                               "grass-regrowth-time" = list(min=0, max=100, step=10, qfun="qunif"),
#                                               "sheep-gain-from-food" = list(min=0, max=50, step=10, qfun="qunif"),
#                                               "wolf-gain-from-food" = list(min=0, max=100, step=10, qfun="qunif"),
#                                               "sheep-reproduce" = list(min=0, max=20, step=5, qfun="qunif"),
#                                               "wolf-reproduce" = list(min=0, max=20, step=5, qfun="qunif")),
#                              constants = list("model-version" = "\"sheep-wolves-grass\"",
#                                               "show-energy?" = "false"))

## ----eval=FALSE---------------------------------------------------------------
#  nl@simdesign <- simdesign_lhs(nl, samples=500, nseeds=1, precision=3)

## ----eval=FALSE---------------------------------------------------------------
#  library(future)
#  plan(multisession)
#  results <- run_nl_all(nl, split=10)

## ----eval=FALSE---------------------------------------------------------------
#  setsim(nl, "simoutput") <- results
#  saveRDS(nl, file.path(nl@experiment@outpath, "lhs.rds"))

## ----eval=FALSE---------------------------------------------------------------
#  library(tidyverse)
#  input <- getsim(nl, "siminput") %>%    # Take input parameter matrix
#    dplyr::select(names(getexp(nl, "variables"))) %>%  # Select variable parameters only
#    dplyr::rename_all(~str_replace_all(., c("-" = "_", "\\s+" = "_"))) # Remove - and space characters.
#  
#  output <- getsim(nl, "simoutput") %>%   # Take simulation output
#    dplyr::group_by(`random-seed`, siminputrow) %>% # Group by random seed and siminputrow
#    dplyr::summarise_at(getexp(nl, "metrics"), list(mean=mean, sd=sd)) %>% # Aggregate output
#    dplyr::ungroup() %>%  # Ungroup
#    dplyr::select(-`random-seed`, -siminputrow) %>%  # Only select metrics
#    dplyr::rename_all(~str_replace_all(., c("-" = "_", "\\s+" = "_", "\\[" = "_", "\\]" = "_", "=" = ""))) # Remove - and space characters.
#  
#  # Perform pcc and src for each output separately (map)
#  pcc.result <- purrr::map(names(output), function(x) sensitivity::pcc(X=input, y=output[,x], nboot = 100, rank = FALSE))
#  src.result <- purrr::map(names(output), function(x) sensitivity::src(X=input, y=output[,x], nboot = 100, rank = FALSE))

## ----eval=FALSE---------------------------------------------------------------
#  plot(pcc.result[[1]])

## ----eval=FALSE---------------------------------------------------------------
#  pcc.result.tidy <- purrr::map_dfr(seq_along(pcc.result), function(x) {
#    pcc.result[[x]]$PCC %>%
#      tibble::rownames_to_column(var="parameter") %>%
#      dplyr::mutate(metric = names(output)[x])
#  })
#  
#  ggplot(pcc.result.tidy) +
#    coord_flip() +
#    facet_wrap(~metric) +
#    geom_point(aes(x=parameter, y=original, color=metric)) +
#    geom_errorbar(aes(x=parameter, ymin=`min. c.i.`, ymax=`max. c.i.`, color=metric), width=0.1)
#  
#  src.result.tidy <- purrr::map_dfr(seq_along(src.result), function(x) {
#    src.result[[x]]$SRC %>%
#      tibble::rownames_to_column(var="parameter") %>%
#      dplyr::mutate(metric = names(output)[x])
#  })
#  
#  ggplot(src.result.tidy) +
#    coord_flip() +
#    facet_wrap(~metric) +
#    geom_point(aes(x=parameter, y=original, color=metric)) +
#    geom_errorbar(aes(x=parameter, ymin=`min. c.i.`, ymax=`max. c.i.`, color=metric), width=0.1)

