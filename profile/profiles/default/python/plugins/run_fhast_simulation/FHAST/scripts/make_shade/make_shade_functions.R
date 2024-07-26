# Make a function to make the shade file
make_shade_shape = function(shape_file_in,
                            time_in){

  # Get the location for the center of the shape and put it in EPSG 4326
  # to allow the solar calculator to work
  location = shape_file_in %>% 
    summarize(geometry = st_union(geometry)) %>% 
    st_centroid() %>% 
    st_transform(st_crs("EPSG:4326"))
  
  # Get the time and time zone based on location
  time = as.POSIXct(
    x = time_in,
    tz = tz_lookup(location, method = "accurate")
  )
  
  # get the sunset time
  set = sunriset(
    crds = st_coordinates(location),
    dateTime = time,
    proj4string=CRS(st_crs(location)$proj4string),
    direction="sunset",
    POSIXct.out=TRUE
  )
  
  # get the sunrise time
  rise = sunriset(
    crds = st_coordinates(location),
    dateTime = time,
    proj4string=CRS(st_crs(location)$proj4string),
    direction="sunrise",
    POSIXct.out=TRUE
  )
  
  # Get a set number of times in between rise and set and drop the 
  # rise and set times
  times_seq = seq(rise$time, set$time, length.out = 5)
  adjusted_times = times_seq[-c(1,length(times_seq))]
  
  make_1_day_shade = function(time_in, location_in, shape_in){

    # calculate the solar angel
    solar_pos = solarpos(
      crds = st_coordinates(location_in),
      dateTime = time_in,
      proj4string=CRS(st_crs(location_in)$proj4string)
    )
    
    # calculate the foot print of the shade
    # the height attribute needs to be in the same units as the crs
    footprint = shadowFootprint(
      obstacles = as(shape_in, "Spatial"),
      obstacles_height_field = "height",
      solar_pos = solar_pos) %>% 
      st_as_sf() %>% 
      mutate(id = 1:n()) %>% 
      select(geometry, id) %>% 
      mutate(shade = 1,
             month = month(time_in),
             hour = hour(time_in))
    
    return(footprint)
  }

  output = map_dfr(adjusted_times,
                   ~make_1_day_shade(.x, location, shape_file_in))
  
  return(output)
}

