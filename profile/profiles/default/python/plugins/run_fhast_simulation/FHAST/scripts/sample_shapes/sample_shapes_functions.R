# This function takes a shape file and a grid and samples a specified column form
# the shape file on the grid. It then returns the grid with a new column of the
# values

##### sample_shape_with_grid #####
sample_shape_with_grid <- function(grid, shape_file, column_name, output_name) {
  column_name <- enquo(column_name)
  # fix up the grid file
  grid <- grid %>%
    select(distance, area, l_or_r, geometry, lat_dist) %>%
    rowid_to_column("ID")

  # This suppresses a warning about attributes
  st_agr(grid) <- "constant"
  st_agr(shape_file) <- "constant"

  # First intersect the shape file and grid and only save the unique IDs of each
  # resulting shape
  
  grid_samples_check <- shape_file %>%
    st_intersection(grid) 
  
  if(NROW(grid_samples_check)==0){
    stop(paste0("The ", output_name, " shape does not overlap the grid.\nPlease ensure overlap of all shape files and the grid."))
  }
    
  grid_samples = grid_samples_check %>% 
    # there are duplicates
    distinct() %>%
    mutate(sample_area = as.numeric(st_area(.))) %>%
    as_tibble() %>%
    select(sample_area, !!column_name, ID)

  # Now take all those shapes and used a weighted average to get the average
  # (including areas without values as 0s) value over each grid cell
  new_grid <- grid %>%
    as_tibble() %>%
    select(ID, area) %>%
    full_join(grid_samples, by = "ID") %>%
    replace(is.na(.), 0) %>%
    mutate(across(!!column_name, .fns = ~ (. * sample_area), .names = "weights")) %>%
    group_by(ID) %>%
    summarize(
      value = sum(weights),
      total_area = sum(area) / n()
    ) %>%
    ungroup() %>%
    mutate(!!column_name := round(value / total_area, 2)) %>%
    select(!!column_name, ID) %>%
    full_join(grid, by = "ID") %>%
    rename({{ output_name }} := !!column_name)

  return(new_grid)
}

##### sample_all_shapes #####
sample_all_shapes <- function(grid = NULL,
                              shape_file = NULL,
                              column_name = NULL,
                              output_name = NULL) {
  output <- future_pmap(
    .l = list(shape_files, column_name, output_name),
    .f = ~ sample_shape_with_grid(grid, ...),
    .options = furrr_options(seed = TRUE)
  ) %>%
    # Join the data frames together
    reduce(~ left_join(.x, .y, by = c("ID", "distance", "area", "l_or_r", "geometry", "lat_dist"))) %>%
    # Make it a shape file
    st_as_sf(sf_column_name = "geometry")

  return(output)
}

##### sampled_to_csv #####
sampled_to_csv <- function(sampled_shapes = NULL) {
  shapes_csv <- sampled_shapes %>%
    as_tibble() %>%
    select(-geometry, -l_or_r, -ID)
  return(shapes_csv)
}
