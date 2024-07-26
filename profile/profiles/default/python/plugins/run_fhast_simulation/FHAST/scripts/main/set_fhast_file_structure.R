########################################
# Sets up the file structure for FHAST run
########################################

initialize_fhast <- function(file_path) {

  # set the main input folders
  fhast_base_folder <<- dirname(file_path)
  if (!dir.exists(fhast_base_folder)) {
    # Directory doesn't exist
    return()
  }

  error_message = "!!! PROVIDE !!!"
  # Create default file if it doesn't exist
  if (!file.exists(file_path)) {
    # File doesn't exist, make with default values
    write_config_file(
      file_path,
      "Unnamed Scenario",
      error_message ,
      error_message ,
      error_message ,
      error_message ,
      error_message ,
      error_message ,
      error_message ,
      error_message ,
      error_message ,
      error_message ,
      error_message ,
      error_message ,
      error_message ,
      error_message ,
      paste0(error_message, "or delete message !!!"),
      paste0(error_message, "or delete message !!!")
    )
  }

  # This cleans any default file messages that might have been written as file names
  bad_file_list = list.files(path = dirname(file_path),
                             pattern = error_message ,
                             recursive = FALSE)
  walk(bad_file_list, ~file.remove(paste0(dirname(file_path), "/",.x)))
  
  # set a global variable for the UI
  config_file_path <<- file_path

  # Read in the main input file file to get cores used
  input_data <- load_text_file(file_path)
  
  # Get the run name
  run_name <<- ifelse(is.na(input_data["run name", ]),
                      str_replace_all(paste0("none_given_", Sys.time()), ":", "-"),
                      input_data["run name", ])

  # Get the path to the output folder
  output_folder_path <<- get_path(fhast_base_folder,
                          input_data["output path", ])

  # Get the path to the notes file
  notes_path <<- get_path(fhast_base_folder,
                          input_data["notes file", ])
  
  # Get the notes to the notes file
  if (file.exists(notes_path)){
    sim_notes <<- readLines(notes_path, warn = FALSE)
  } else {
    sim_notes <<- "Notes file not found."
  }
  
  # get the name of the input file
  fish_population_path <<- get_path(fhast_base_folder,
                                   input_data["fish population", ])
  daily_path <<- get_path(fhast_base_folder,
                              input_data["daily conditions", ])
  
  # get the name of the input file
  fish_parameters_path <<- get_path(fhast_base_folder,
                                   input_data["fish parameters", ])
  
  # get the paths for the files
  grid_center_line_path <<- get_path(fhast_base_folder,
                               input_data["grid centerline", ])
  grid_top_marker_path <<- get_path(fhast_base_folder,
                               input_data["grid top point", ])
  cover_path <<- get_path(fhast_base_folder, input_data["cover", ])
  canopy_path <<- get_path(fhast_base_folder, input_data["canopy", ])
  tree_growth_path <<- get_path(fhast_base_folder, input_data["tree growth", ])
  hab_path <<- get_path(fhast_base_folder, input_data["habitat parameters", ])
  interaction_path <<- get_path(fhast_base_folder,
                               input_data["interaction parameters", ])
  predator_path <<- get_path(fhast_base_folder,
                            input_data["predator parameters", ])

  # Location of rasters
  raster_folder <<- get_path(fhast_base_folder, input_data["raster folder", ])
  
  # get to the aoi path
  aoi_input <- input_data["aoi", ]
  # Checking length is not sufficient (aoi_input can be an array containing a
  # single empty string), so the nzchar check is also needed.
  if (!is.na(aoi_input) && length(aoi_input) > 0 && nzchar(aoi_input)) {
    aoi_path <<- get_path(fhast_base_folder, aoi_input)
  } else {
    aoi_path <<- NA
  }
  
  # get the wildcard path
  wild_input <- input_data["wildcard", ]
  # Checking length is not sufficient (aoi_input can be an array containing a
  # single empty string), so the nzchar check is also needed.
  if (!is.na(wild_input) && length(wild_input) > 0 && nzchar(wild_input)) {
    wild_path <<- get_path(fhast_base_folder, wild_input)
  } else {
    wild_path <<- NA
  }
  

  # Reset this stuff to be ready for a new run, the random seed in particular
  # should get set every time.

  # Set the random seed
  set.seed(6806665)
}

write_config_file <- function(file_path, name, output_folder_path,  notes, fish_pop, daily, fish_params, line,
                            point, cover, canopy, tree_growth, hab_params,
                            interaction_params, predator, raster, aoi, wild) {
  obj <- data.frame(
    names = c(
      "run name", "output path", "notes file", "fish population", "daily conditions",
      "fish parameters", "grid centerline", "grid top point",
      "cover", "canopy", "tree growth", "habitat parameters", "interaction parameters",
      "predator parameters", "raster folder", "aoi", "wildcard"
    ),
    paths = c(
      name, output_folder_path, notes, fish_pop, daily, fish_params, line, point,
      cover, canopy, tree_growth, hab_params, interaction_params, predator,
      raster, aoi, wild
    )
  )
  save_text_file(file_path, obj)


}


