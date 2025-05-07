################################################################################
# This just loads the spatial input data and makes a map to preview
################################################################################

# load the functions 
source(here("scripts","make_preview_map","make_preview_map_functions.R"))

# make the plot
ml$plot$map_plot = make_map_plot()

# display the map plot
display_plot(map_plot, 15, 15, preview_flag)

################################################################################
# End
################################################################################