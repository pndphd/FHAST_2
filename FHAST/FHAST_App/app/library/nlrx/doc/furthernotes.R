## ----setup, include = FALSE---------------------------------------------------
knitr::opts_chunk$set(
  collapse = TRUE,
  comment = "#>"
)

## ----progress, eval=FALSE-----------------------------------------------------
#  progressr::handlers("progress")
#  results <- progressr::with_progress(run_nl_all(nl))

## ----eval=FALSE---------------------------------------------------------------
#  install.packages('unixtools', repos = 'http://www.rforge.net/')
#  unixtools::set.tempdir("<path-to-temp-dir>")

## ----eval=FALSE---------------------------------------------------------------
#  to-report green.patches
#    report count patches with [pcolor = green]
#  end

## ----eval=FALSE---------------------------------------------------------------
#  library(future)
#  plan(multiprocess)
#  results <- run_nl_all(nl = nl)

## ----eval=FALSE---------------------------------------------------------------
#  library(future)
#  plan(list(sequential, multiprocess))
#  results %<-% run_nl_all(nl = nl)

## ----eval=FALSE---------------------------------------------------------------
#  library(future)
#  plan(multisession)
#  results <- run_nl_all(nl = nl, split = 4)

## ----eval=FALSE---------------------------------------------------------------
#  # Load required packages
#  library(future)
#  library(future.batchtools)
#  library(debugme)
#  Sys.setenv(DEBUGME='batchtools')
#  library(batchtools)
#  
#  # Define the path to the ssh key for your machine:
#  options(future.makeNodePSOCK.rshopts = c("-i", "/patch/to/id_rsa"))
#  # Define server and your login credentials for the remote HPC:
#  login <- tweak(remote, workers="server.HPC.de", user="username")
#  
#  # Define plan for future environment:
#  bsub <- tweak(batchtools_slurm, template = "slurm.tmpl", # define name of slurm tmeplate on HPC filesystem
#                resources = list(job.name = "jobname", # define jobname
#                                 log.file = "jobname.log", # define logfile name
#                                 queue = "medium",  # define HPC queue
#                                 service = "normal", # define HPC service
#                                 walltime = "00:30", # define walltime
#                                 n_jobs = "1",   # define number of processes per job
#                                 mem_cpu = "4000") # define memory per cpu
#  
#  # Load HPC plan:
#  plan(list(login,
#            bsub,
#            multisession))
#  
#  # Execute simulations
#  results <- run_nl_all(nl = nl)

## ----eval=FALSE---------------------------------------------------------------
#  library(clustermq)
#  
#  # First, we set the total number of jobs for the HPC
#  # In this example we run each simulation as an individual job (recommended).
#  # Thus to calculate the number of jobs we just multiply the number of parameterizations of the simdesign with the number of random seeds.
#  # If you want to group several runs into the same job you can adjust this line and choose a lower number.
#  # However, the number must be chosen that nrow(nl@simdesign@siminput)/njobs results in an integer value
#  njobs <- nrow(nl@simdesign@siminput) * length(nl@simdesign@simseeds)
#  
#  # Second, we generate vectors for looping trough model runs.
#  # We generate a vector for simpinputrows by repeating the sequence of parameterisations for each seed.
#  # Then, we generate a vector of random-seeds by repeating each seed for n times, where n is the number of siminputrows.
#  siminputrows <- rep(seq(1:nrow(nl@simdesign@siminput)), length(nl@simdesign@simseeds))
#  rndseeds <- rep(nl@simdesign@simseeds, each=nrow(nl@simdesign@siminput))
#  
#  # Third, we define our simulation function
#  # Please adjust the path to the temporary file directory
#  simfun <- function(nl, siminputrow, rndseed, writeRDS=FALSE)
#  {
#    unixtools::set.tempdir("/hpath/to/temp/dir")
#    library(nlrx)
#    res <- run_nl_one(nl = nl, siminputrow = siminputrow, seed = rndseed, writeRDS = TRUE)
#    return(res)
#  }
#  
#  # Fourth, use the Q function from the clustermq package to run the jobs on the HPC:
#  # The q function loops through our siminputrows and rndseeds vectors.
#  # The function creates njobs jobs and distributes corresponding chunks of the input vectors to these jobs for executing the simulation function simfun.
#  # As constants we provide our nl object and the function parameter writeRDS.
#  # If write RDS is true, an *.rds file will be written on the HPC after each jobs has finished.
#  # This can be useful to gain results from completed runs after a crash has occured.
#  results <- clustermq::Q(fun = simfun,
#                          siminputrow = siminputrows,
#                          rndseed = rndseeds,
#                          const = list(nl = nl,
#                                       writeRDS = TRUE),
#                          export = list(),
#                          seed = 42,
#                          n_jobs = njobs,
#                          template = list(job_name = "jobname", # define jobname
#                                          log.file = "jobname.log", # define logfile name
#                                          queue = "medium",  # define HPC queue
#                                          service = "normal", # define HPC service
#                                          walltime = "00:30:00", # define walltime
#                                          mem_cpu = "4000")) # define memory per cpu
#  
#  # The Q function reports the individual results of each job as a list
#  # Thus, we convert the list results to tibble format:
#  results <- dplyr::bind_rows(results)

