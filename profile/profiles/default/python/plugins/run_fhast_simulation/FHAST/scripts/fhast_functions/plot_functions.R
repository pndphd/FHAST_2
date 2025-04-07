########################################
# Sets up Some functions for plotting a plotting default items
########################################

# Load a color blind friendly pallet
ml$df$palette = c("#999999", "#0072B2", "#D55E00",
                "#F0E442", "#56B4E9", "#E69F00",
                "#0072B2", "#009E73", "#CC79A7")



##### Functions #####
# Function to display plot which is overloaded
display_plot <- function(plot) {
  if (print_plots) {
    X11()
    print(plot)
  }
}

display_plot <- function(plot, height, width, display = FALSE) {
  if (display) {
    X11(height = height, width = width)
    print(plot)
  }
}


