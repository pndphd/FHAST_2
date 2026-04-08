################################################################################
# This script takes two shape files (OHWM and project foot print) and gets
# overlap
################################################################################

##### Developer options ########################################################
# Uncomment for development to pick a specific file and run from IDE

if (!exists("pass_arguments")){
  pass_arguments = NULL
  pass_arguments[1] = "C:/Users/pndph/Desktop/temp/cmax.csv"
  pass_arguments[2] = "Beta_Sigmoid"
  pass_arguments[3] = "C:/Users/pndph/Desktop/temp"
}

################################################################################

##### Run setup ################################################################

# # install and load the here package if necessary
if(!require(c("here"), character.only = T)){install.packages(package)}

# Load Libraries
source(here("scripts","main","load_libraries.R"))
# Library only this (not rest of FHAST) needs
library(minpack.lm)
 
# Make blank list
ml = list(var = list(),
          df = list(),
          plot = list(),
          path = list(),
          string = list(),
          sum = list(),
          table = list())

##### Read in data #############################################################
message("Read Data./n")
# Read in the data to fit
parameter_data = read.csv(pass_arguments[1])
x_lab = names(parameter_data)[1]
y_lab = names(parameter_data)[2]
parameter_data = parameter_data %>% 
  rename(x = 1, y = 2) 
message("Read Data: Done./n")

##### Fit the data #############################################################
message("Fit Data./n")
print(pass_arguments[2])
switch(pass_arguments[2], 
       Beta_Sigmoid={
         
         # Get initial guess and some plotting values
         guess_A = mean(parameter_data$x)
         guess_B = guess_A/2
         
         # Fit the data
         bs_fit = nlsLM(y ~ 1*(1+(A-(x))/(A-B))*((x)/A)^(A/(A-B)),
                         data = parameter_data,
                         start = list(A = guess_A, B = guess_B))
         bs_A_set = bs_fit$m$getPars()["A"]
         bs_B_set = bs_fit$m$getPars()["B"]
         
         # Make the tabluar output
        table_output = data.frame(Parameter = c("A", "B"),
                                  Estimate = c(bs_A_set, bs_B_set))
         
         # Make the fitted data set for plotting
         fit_predict = data.frame(x = seq(min(c(parameter_data$x,0)),
                                         max(parameter_data$x),
                                         length.out = 100)) %>%
           mutate(predict = predict(bs_fit,
                                    newdata = .))
   
       },
       Linear={
   
       },
       {
         # If no valid model type set stop program
         message(paste0("!!!!!!!!!!!\n",
                        "!!!ERROR!!! Model type not recognized.\n",
                        "!!!!!!!!!!!\n"))
         stop()
         
       }
)

message("Fit Data: Done./n")

##### Make plot ################################################################
message("Make Plot./n")

# Make the plot
plot_fit = ggplot(parameter_data, aes(x = x)) +
  theme_classic(base_size = 25) +
  theme(legend.title = element_blank())+
  labs(y = y_lab, x = x_lab) +
  geom_path(data = fit_predict, aes(y = predict, x = x),
            color = "black", linewidth = 0.5) +
  geom_point(aes(y = y),
             shape = 1,
             stroke = 1.5,
             size = 5) 
print(plot_fit)

# Save the plot 
ggsave(here(pass_arguments[3], "fhast_parameter_fit.png"),
       plot_fit,
       height = 7,
       width = 7,
       units = "in",
       device = "png",
       dpi = 300)

message("Make Plot: Done./n")

# Make the html doc
message("Make Parameter report./n")
rmarkdown::render(input = here("scripts", "param_analysis", "param_report.Rmd"),
                  output_format = "html_document",
                  output_file = here(pass_arguments[3], "fhast_parameter_report.html"),
                  quiet = TRUE)

message("Make Parameter report: Done./n")

################################################################################
# End
################################################################################
