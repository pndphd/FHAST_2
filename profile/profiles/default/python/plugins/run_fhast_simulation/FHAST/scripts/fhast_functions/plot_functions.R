################################################################################
# Sets up Some functions for plotting a plotting default items
################################################################################

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

################################################################################
# End
################################################################################


