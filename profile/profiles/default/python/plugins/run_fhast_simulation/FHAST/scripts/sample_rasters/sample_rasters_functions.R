# This folder contains the functions for sample_raster.R

##### get_type_letter #####
# this function translates the type word into the letter
get_type_letter = function(type = NULL){
  if(type == "depth"){
    type_letter = "D"
  } else if (type == "velocity"){
    type_letter = "V"
  } else {
    stop("Invalid type of raster. Choose 'depth' or 'velocity'.")
  }
  
  return(type_letter)
}

##### load_rasters #####
# This function loads 
load_rasters = function(type = NULL,
                        folder = NULL,
                        clip_mask = NULL){

    # Get the extent of the grid
  extent = ext(clip_mask)

  # Get the letter type
  type_letter = get_type_letter(type)

  # Find the files that match the type.
  files = list.files(folder, paste0(type_letter, "\\d+.tif"), full.names=TRUE)
  # Sort the files so they are in flow order of low to high.
  files_sorted = files[order(strtoi(str_extract(str_extract(files, paste0(type_letter, "\\d+.tif")), "\\d+")))]
  # make the raster stack and crop it
  stack = rast(map(files_sorted, ~rast(.x))) 

  if(type_letter == "D"){
    # Use terrain to calculate the slope and the correction for area
    original_raster = rast(tail(files_sorted, n=1))
    slope_raster = original_raster %>% 
      terra::crop(extent) %>% 
      terrain(v="slope", neighbors = 4, unit = "radians")  %>%
      app(fun = function(x){1/cos(x)}) %>% 
      terra::extend(original_raster)
    # Give the value a name
    names(slope_raster) = "correction_factor"

    stack = stack %>%
      c(slope_raster)

  }

  return(stack)
}

# function to calculate the proportion of the area that has depth > 0 for each flow tiff
get_wetted_area <- function(df, ...){
  df %>%
    # selects all the depth or velocity columns
    summarize(across(-c("correction_factor", "coverage_fraction"), 
                     .fns = ~ sum(coverage_fraction[.x > 0]) / sum(coverage_fraction),
                     .names = "wetd.{.col}"))
  
}


##### sample_grid #####
# This function samples the raster stack using the river grid
# if depth is selected it also gets the bottom area
sample_grid = function(stack = NULL,
                       grid = NULL,
                       flows = NULL,
                       type = NULL){

  type_letter = get_type_letter(type)

  samples = stack %>% 
    #take mean excluding NAs
    exact_extract(grid,
                  fun = 'mean',
                  progress = FALSE) %>%  
    data.frame() %>% 
    # bind it back to the polygons
    cbind(data.frame(grid)) %>% 
    # set left and right bank correctly
    # mutate(lat_dist = ifelse(lat_dist>0,ifelse(left_or_right>0, lat_dist, -lat_dist),0)) %>% 
    # Convert to simple feature then a df and remove uncessary rows
    data.frame() %>% 
    dplyr::select(all_of(paste0("mean.", type_letter, flows)),
                  lat_dist,
                  # if velocity the correction factor is not inside 
                  contains("mean.correction_factor"),
                  distance,
                  area) 
  

  if(type_letter == "D"){
    
    wetter_area = stack %>%
      exact_extract(river_grid,
                    fun = NULL,
                    progress = FALSE,
                    default_value = 0) %>%
      future_map_dfr(get_wetted_area) %>%
      as_tibble()
    
    samples = samples %>% 
      mutate(bottom_area = ifelse(is.na(mean.correction_factor), area, area*(mean.correction_factor))) %>% 
      bind_cols(wetter_area)
  }
  
  return(samples)
}