# make an output directory
output_folder = here(ml$path$output_folder, paste0(ml$var$run_name, "_outputs"))
output_shape_folder = here(output_folder, "shape_files")
output_temp_folder = here(output_folder, "temporary")
dir.create(output_folder)
dir.create(output_shape_folder)
dir.create(output_temp_folder)

# Copy the input file to the output folder
file.copy(ml$path$config_file, here(output_folder, "input_file.txt"))

# Write the file for the reports log
#file.copy(file_path, here(output_temp_folder, "config_file.txt"), overwrite = TRUE)
write.table(ml$path$config_file,
            file = here(output_temp_folder, "input_file_path.txt"),
            row.names = F,
            col.names = F)

# Make sure temp directories exist
temp_folder <- here(output_temp_folder)
make_dir_if_missing(here(temp_folder, "file.txt"))
