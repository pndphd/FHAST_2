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
#  nl@experiment <- experiment(expname="wolf-sheep-GenSA1",
#                              outpath=outpath,
#                              repetition=1,
#                              tickmetrics="false",
#                              idsetup="setup",
#                              idgo="go",
#                              runtime=50,
#                              metrics=c("(1 / count wolves)"),
#                              variables = list('initial-number-sheep' = list(min=50, max=150, qfun="qunif"),
#                                               'initial-number-wolves' = list(min=50, max=150, qfun="qunif")),
#                              constants = list("model-version" = "\"sheep-wolves-grass\"",
#                                               "grass-regrowth-time" = 30,
#                                               "sheep-gain-from-food" = 4,
#                                               "wolf-gain-from-food" = 20,
#                                               "sheep-reproduce" = 4,
#                                               "wolf-reproduce" = 5,
#                                               "show-energy?" = "false"))
#  

## ----eval=FALSE---------------------------------------------------------------
#  nl@simdesign <- simdesign_GenSA(nl,
#                                  evalcrit = 1,
#                                  nseeds = 1,
#                                  control=list(maxit = 20))

## ----eval=FALSE---------------------------------------------------------------
#  results <- run_nl_dyn(nl, seed = nl@simdesign@simseeds[1])

## ----eval=FALSE---------------------------------------------------------------
#  results

## ----eval=FALSE---------------------------------------------------------------
#  setsim(nl, "simoutput") <- tibble::enframe(results)
#  saveRDS(nl, file.path(nl@experiment@outpath, "genSA_1.rds"))
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
#  nl@experiment <- experiment(expname="wolf-sheep-GenSA2",
#                              outpath=outpath,
#                              repetition=1,
#                              tickmetrics="false",
#                              idsetup="setup",
#                              idgo="go",
#                              runtime=50,
#                              metrics.patches = c("pxcor", "pycor", "pcolor"),
#                              variables = list('initial-number-sheep' = list(min=50, max=150),
#                                               'initial-number-wolves' = list(min=50, max=150)),
#                              constants = list("model-version" = "\"sheep-wolves-grass\"",
#                                               "grass-regrowth-time" = 30,
#                                               "sheep-gain-from-food" = 4,
#                                               "wolf-gain-from-food" = 20,
#                                               "sheep-reproduce" = 4,
#                                               "wolf-reproduce" = 5,
#                                               "show-energy?" = "false"))
#  

## ----eval=FALSE---------------------------------------------------------------
#  critfun <- function(nl) {
#    library(landscapemetrics)
#    res_spat <- nl_to_raster(nl)
#    res_spat_raster <- res_spat$spatial.raster[[1]]
#    lsm <- lsm_l_ed(res_spat_raster)
#    crit <- lsm$value
#    return(crit)
#  }

## ----eval=FALSE---------------------------------------------------------------
#  nl@simdesign <- simdesign_GenSA(nl,
#                                  evalcrit = critfun,
#                                  nseeds = 1,
#                                  control=list(maxit = 20))

## ----eval=FALSE---------------------------------------------------------------
#  results <- run_nl_dyn(nl, seed = nl@simdesign@simseeds[1])

## ----eval=FALSE---------------------------------------------------------------
#  results

## ----eval=FALSE---------------------------------------------------------------
#  setsim(nl, "simoutput") <- tibble::enframe(results)
#  saveRDS(nl, file.path(nl@experiment@outpath, "genSA_2.rds"))
#  

