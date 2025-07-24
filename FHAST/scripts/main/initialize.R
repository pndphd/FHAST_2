################################################################################
# Run the initialization
################################################################################

##### Variable structure #####
# Make the master list of data and put in the few variable we have so far
ml = list(var = list(),
          df = list(),
          plot = list(),
          path = list(),
          string = list(),
          sum = list(),
          table = list())
ml$var$plot_width = plot_width
ml$var$print_plots = print_plots 
ml$path$config_file = config_file_name
rm(plot_width, print_plots, config_file_name)

##### Set some plotting defaults #####
# Load a color blind friendly pallet
ml$df$palette = c("#999999", "#0072B2", "#D55E00",
                  "#F0E442", "#56B4E9", "#E69F00",
                  "#0072B2", "#009E73", "#CC79A7")

##### Set folder for config file #####
# Set the main input folders
ml$path$base_folder = dirname(ml$path$config_file)

##### Read in config file and variables #####
# Read in the main input file file to get cores used
ml$df$config_data = load_text_file(ml$path$config_file)

# Get the run name
ml$var$run_name = ifelse(is.na(ml$df$config_data["run name", ]),
                         str_replace_all(paste0("none_given_", Sys.time()), ":", "-"),
                         ml$df$config_data["run name", ])

# Get the path to the output folder and make the folders
ml$path$output_folder = here(get_path(ml$path$base_folder,
                                      ml$df$config_data["output path",]),
                             paste0(ml$var$run_name, "_outputs"))

# Get the path to the notes file
ml$path$notes = get_path(ml$path$base_folder, ml$df$config_data["notes file",])

# Get the name of the input file
ml$path$fish_pop = get_path(ml$path$base_folder, ml$df$config_data["fish population", ])
ml$path$daily = get_path(ml$path$base_folder, ml$df$config_data["daily conditions", ])

# Get the name of the input file
ml$path$fish_parms = get_path(ml$path$base_folder, ml$df$config_data["fish parameters", ])

# Get the paths for the files
ml$path$center_line = get_path(ml$path$base_folder, ml$df$config_data["grid centerline", ])
ml$path$top_marker = get_path(ml$path$base_folder, ml$df$config_data["grid top point", ])
ml$path$cover = get_path(ml$path$base_folder, ml$df$config_data["cover", ])
ml$path$canopy = get_path(ml$path$base_folder, ml$df$config_data["canopy", ])
ml$path$tree_growth = get_path(ml$path$base_folder, ml$df$config_data["tree growth", ])
ml$path$hab = get_path(ml$path$base_folder, ml$df$config_data["habitat parameters", ])
ml$path$interaction = get_path(ml$path$base_folder, ml$df$config_data["interaction parameters", ])
ml$path$predator = get_path(ml$path$base_folder, ml$df$config_data["predator parameters", ])

# Location of rasters
ml$path$raster_folder = get_path(ml$path$base_folder, ml$df$config_data["raster folder", ])

# Get to the aoi path
ml$string$aoi = ml$df$config_data["aoi", ]
# Checking length is not sufficient (ml$string$aoi can be an array containing a
# single empty string), so the nzchar check is also needed.
if (!is.na(ml$string$aoi) && length(ml$string$aoi) > 0 && nzchar(ml$string$aoi)) {
  ml$path$aoi = get_path(ml$path$base_folder, ml$string$aoi)
} else {
  ml$path$aoi = NA
}

# Get the wildcard path
ml$string$wild = ml$df$config_data["wildcard", ]
# Checking length is not sufficient (ml$string$aoi can be an array containing a
# single empty string), so the nzchar check is also needed.
if (!is.na(ml$string$wild) && length(ml$string$wild) > 0 && nzchar(ml$string$wild)) {
  ml$path$wild = get_path(ml$path$base_folder, ml$string$wild)
} else {
  ml$path$wild = NA
}

# Get the canopy path
ml$string$canopy = ml$df$config_data["canopy", ]
if (!is.na(ml$string$canopy) && length(ml$string$canopy) > 0 && nzchar(ml$string$canopy)) {
  ml$path$canopy = get_path(ml$path$base_folder, ml$string$canopy)
} else {
  ml$path$canopy = NA
}

# Get the tree growth path
ml$string$tree_growth <- ml$df$config_data["tree growth", ]
if (!is.na(ml$string$tree_growth) && length(ml$string$tree_growth) > 0 && nzchar(ml$string$tree_growth)) {
  ml$path$tree_growth = get_path(ml$path$base_folder, ml$string$tree_growth)
} else {
  ml$path$tree_growth = NA
}

##### CPU handling #####
# Set the plan for furrr (number of cores and type)
pick_num_cores <- function(ratio = 0.75){
  total_cores <- parallel::detectCores()
  cores_to_use <- floor(total_cores * ratio)
  if(cores_to_use <= 1){
    return(total_cores)
  } else {
    return(cores_to_use)
  }
}

future::plan(
  strategy = multisession,
  workers = pick_num_cores()
)

future.seed <- FALSE

################################################################################
# End
################################################################################
