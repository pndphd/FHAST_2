################################################################################
# This file has the functions used in river_grid_maker_run.R 
################################################################################

##### make_distances_list #####
# This Function makes the list of distances
make_distances_list = function(resolution = NULL,
                               buffer = NULL){
  distances = seq(resolution/2, buffer + resolution, resolution)
  return(distances)
}

##### make_buffers #####
make_buffers = function(distances = NULL,
                       line = NULL,
                       resolution = NULL){
  
  buffers = map(distances, ~buffer_lines(line, .x, resolution)) %>% 
    do.call(rbind, .) %>% 
    st_difference() %>% 
    filter(st_is(., c("POLYGON","MULTIPOLYGON"))) 
  
  return(buffers)
}

##### buffer_lines #####
# Make a function to make series of buffers that from the
# lateral part of the grid
buffer_lines = function(shape, distance, resolution){
  buffer = st_buffer(x = shape, dist = distance) %>%
    mutate(lat_dist = distance - resolution/2)   
  return (buffer)
}

##### make_large_buffer #####
# Make a function to get large buffers used to tell left from right
make_large_buffer = function(distances = NULL,
                                 line = NULL){
  large_buffer = c(-max(distances), max(distances)) %>% 
    map(~buffer_side(line, .x)) %>% 
    do.call(rbind, .) %>% 
    st_intersection() %>% 
    filter(st_is(., c("POLYGON","MULTIPOLYGON"))) %>% 
    # Select minimal columns
    select(geometry, left_or_right)
  
  return(large_buffer)
}

##### buffer_side #####
# Make a function to make two buffers that designate left or right side of center line
buffer_side = function(shape, distance){
  buffer = st_buffer(x = shape, dist = distance, singleSide = T) %>%
    # Multiply by to 10 exagerate the number
    mutate(left_or_right = distance*10)   
  
  return(buffer)
}

##### make_sample_points #####
make_sample_points = function(resolution = resolution,
                              line = shape_files$line){
  sample_points = st_line_sample(x = line, density = 1/resolution) %>%
    # Conver from a list to a simple feature
    st_sf() %>%
    # Break out into points
    st_cast("POINT") %>% 
    # Assign each one a distance
    mutate(distance = 1:n()*resolution)
  return(sample_points)
}

##### make_vor_cells #####
make_vor_cells = function(points = NULL,
                          top = NULL,
                          resolution = NULL){

  # set up a set of vornoi cells
  vor_cells_1 = st_voronoi(x = st_union(points)) %>%
    st_sf() %>%
    # Break up the geomerty collection to a polygon simple feature
    st_cast() %>% 
    # Join with the points to get the distance attribute form the sample_points layer
    st_join(points) 
  
  #Get to top most cell using the user input point
  top_vor_cell = top %>% 
    st_join(vor_cells_1) 

  vor_cells_2 = vor_cells_1 %>% 
    # If we flip the distances make a row of the new distances
    # also make a row column which will just be 0 if no flip is necessary
    # but will have a value of we need to
    arrange(-distance) %>% 
    mutate(altDist = 1:n()*resolution)
  
  # Check if th top most cell has the highest distance 
  # if not flip the distances
  # we are using distance up stream
  if(top_vor_cell$distance != max(vor_cells_1$distance)){
    vor_cells_2 = vor_cells_2 %>% 
      # use mutate_ because passing strings as col names
      mutate(distance = altDist)
  }
  
  # Remove the altDist column
  # vor_cells_2 = select(vor_cells_2, -altDist)
  return(vor_cells_2)
}

##### make_grid #####
make_grid = function(resolution = NULL,
                     cells = NULL,
                     buffers = NULL,
                     large_buffer = NULL){
  
  st_agr(cells) = "constant"
  st_agr(buffers) = "constant"
  
  grid = cells %>% 
    st_intersection(buffers) %>% 
    filter(st_is(., c("POLYGON","MULTIPOLYGON"))) %>% 
    # cast everyting as a multi polygon then as a polygon to break multi parts into single parts
    st_cast("MULTIPOLYGON") %>%
    st_cast("POLYGON", warn = FALSE) %>% 
    # Calculate the area of each
    mutate(area = as.numeric(st_area(.))) %>% 
    #filter out very small cells  
    filter(!area<resolution^2/100) %>%
    # Do a join with the large buffer to tell which side is left and right
    st_join(large_buffer) %>% 
    filter(!(lat_dist == 0 & left_or_right < 0)) %>% 
    # filter out the curved end caps
    filter(!(distance == max(distance) | distance == min(distance))) 
  
  return(grid)
}

################################################################################
# End
################################################################################