#########################################################
# This script takes a list of files and reprojects them
#########################################################

##### Load Libraries #####
# library(sf)
# library(tidyverse)
# library(terra)
# library(here)


##### Get Inputs #####
# pass_arguments = list()
# pass_arguments[[1]] = list("default_input/testraster.tif",
#                       "default_input/test_vector.shp")
# pass_arguments[[2]] = c("default_input")
# pass_arguments[3] = "EPSG:2169"
print(pass_arguments)

# if (exists("pass_arguments")){
#   list_in = pass_arguments[1]
#   
#   crs = pass_arguments[3]
#   output_folder =pass_arguments[2]
#   # Sys.setenv(JAVA_HOME = here("jdk-11"))
# }
# print(list_in)
# print(crs)
# print(output_folder)
# 
# ##### Work #####
# # Filter out just rasters form list
# rasters = pass_arguments[[1]][grepl('.tif',pass_arguments[[1]])]
# # Filter out just vectors form the list
# vectors = pass_arguments[[1]][grepl('.shp',pass_arguments[[1]])]
# 
# # Make a functions to reproject the raster
# reproject_rasters = function(file, crs, output){
#   #load in the file
#   raster = rast(file)
#   # reproject it
#   new_raster = project(x = raster, y = crs[[1]])
#   # write the output using the same file name
#   writeRaster(new_raster, here(pass_arguments[[2]],
#                                str_sub(file, max(str_locate_all(file, "/")[[1]]) + 1)),
#               overwrite = TRUE) 
# }
# 
# # Make a functions to reproject the vectors
# reproject_vectors = function(file, crs, output){
#   # load in vector
#   vector = st_read(file)
#   # reproject raster
#   new_vector = st_transform(vector, crs[[1]])
#   # write the output using the same file name
#   st_write(new_vector, here(pass_arguments[[2]],
#                                str_sub(file, max(str_locate_all(file, "/")[[1]]) + 1)),
#               append = FALSE) 
# }
# 
# # use purr to process the functions
# walk(rasters, ~reproject_rasters(.x, pass_arguments[3], pass_arguments[[2]]))
# walk(vectors, ~reproject_vectors(.x, pass_arguments[3], pass_arguments[[2]]))

####################################################################
# end
####################################################################