########################################
# Run the initialization
########################################

##### Set the main input folders
input_folder <- file.path(here(), "default_input")

# Check if doing multi run. If not just function normally
if(exists("wild_card_file_name")){
  fhast_config_file <- wild_card_file_name
}else{
  fhast_config_file <- "input_file.txt"
}

# Turn on printing plots
print_plots <<- FALSE

if (isAbsolutePath(fhast_config_file)) {
  file_path <- fhast_config_file
} else {
  file_path <- here(input_folder, fhast_config_file)
}
# initialize_fhast sets up all the directory paths for future scripts.
initialize_fhast(file_path)

# Setup furrr
pick_num_cores <- function(ratio = 0.75){
  total_cores <- parallel::detectCores()
  cores_to_use <- floor(total_cores * ratio)
  if(cores_to_use <= 1){
    return(total_cores)
  } else {
    return(cores_to_use)
  }
}
num_cores <- pick_num_cores()



future::plan(
  strategy = multisession,
  workers = num_cores
)

future.seed <- FALSE
