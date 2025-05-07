################################################################################
# Make the folder for run outputs 
################################################################################

# Make the output directories
ml$path$output_shape_folder = here(ml$path$output_folder, "shape_files")
ml$path$output_temp_folder = here(ml$path$output_folder, "temporary")
dir.create(ml$path$output_folder)
dir.create(ml$path$output_shape_folder)
dir.create(ml$path$output_temp_folder)

# Copy the input file to the output folder
file.copy(ml$path$config_file, here(ml$path$output_folder, "input_file.txt"))

# Copy over some to be printed in reports
file.copy(ml$path$daily, here(ml$path$output_temp_folder, "daily_input.txt"), overwrite = TRUE)
file.copy(ml$path$interaction, here(ml$path$output_temp_folder, "interactions_input.txt"), overwrite = TRUE)
file.copy(ml$path$fish_pop, here(ml$path$output_temp_folder, "population_input.txt"), overwrite = TRUE)
file.copy(ml$path$fish_parms, here(ml$path$output_temp_folder, "fish_input.txt"), overwrite = TRUE)
file.copy(ml$path$fish_parms, here(ml$path$output_temp_folder, "fish_params_input.csv"), overwrite = TRUE)
file.copy(ml$path$hab, here(ml$path$output_temp_folder, "habitat_input.txt"), overwrite = TRUE)
file.copy(ml$path$predator, here(ml$path$output_temp_folder, "predator_input.txt"), overwrite = TRUE)
file.copy(ml$path$notes, here(ml$path$output_temp_folder, "notes.txt"), overwrite = TRUE)

# Copy over some for NetLogo
file.copy(ml$path$fish_parms, here(ml$path$output_temp_folder, "fish_params_input.csv"), overwrite = TRUE)

################################################################################
# End 
################################################################################
