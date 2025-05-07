################################################################################
# This is a set of functions communally used in FHAST for file manupi
################################################################################

# Make a directory if it's missing for a file path
make_dir_if_missing <- function(file_path) {
  directory <- dirname(file_path)
  if (!dir.exists(directory)) {
    parent <- dirname(directory)
    if (!dir.exists(parent)) {
      make_dir_if_missing(directory)
    }
    dir.create(directory)
  }
}

# Check if something is an absolute path and get the path
get_path <- function(base_folder, input_path) {
  path <- ifelse(isAbsolutePath(input_path),
                 input_path,
                 getAbsolutePath(input_path, workDirectory=base_folder))
  return(path)
}

# Check to see if the file exists
check_file_exists = function(file_path){
  if (!file.exists(file_path)) {
    stop(paste0("\nThe input file\n", file_path, "\ndoes not exist."))
  }
}

# Load the text files with equals in them 
load_text_file <- function(file_path) {
  file_path <- get_path(ml$path$base_folder, file_path)
  if (!file.exists(file_path) || dir.exists(file_path)) {
    return(NULL)
  }
  file_data <- read.csv(
    file = file_path,
    sep = ",",
    row.names = 1,
    header = FALSE) %>%
    # Trim off white spaces form values
    rename(value = 1) %>%
    mutate(value = str_trim(value, side = c("both")))
  
  return(file_data)
}

# Save a text file
save_text_file <- function(file_path, obj) {
  file_path <- get_path(ml$path$base_folder, file_path)
  make_dir_if_missing(file_path)
  fwrite(obj,
         file = file_path,
         sep = ",",
         row.names = FALSE,
         col.names = FALSE)
}

# Store the hashes fromn the last run
store_last_run_hashes <- function(file_path, files) {
  obj <- data.frame(
    files = files,
    hashes = sapply(files, md5sum))
  save_text_file(file_path, obj)
}

# Compare the hashes from the last run
compare_last_run_hashes <- function(file_path, files) {
  if (!file.exists(file_path)) {
    return(FALSE)
  }
  # Load the hash values from the last run
  obj <- load_text_file(file_path)
  if (length(row.names(obj)) != length(files)) {
    return(FALSE)
  }
  # NA is written to disk as empty string.
  files = replace_na(files, '')
  # Verify files match
  if (!all(mapply(identical, row.names(obj), files))) {
    return(FALSE)
  }
  hashes = as.vector(md5sum(files))
  hashes = replace_na(hashes, '')
  # verify md5 matches
  return(all(mapply(identical, hashes, obj[,1])))
}

################################################################################
# End
################################################################################
