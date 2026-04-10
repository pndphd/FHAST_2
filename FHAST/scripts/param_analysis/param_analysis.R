################################################################################
# This script takes two shape files (OHWM and project foot print) and gets
# overlap
################################################################################

##### Developer options ########################################################
# Uncomment for development to pick a specific file and run from IDE

if (!exists("pass_arguments")){
  pass_arguments = NULL
  pass_arguments[1] = "C:/Users/pndph/Desktop/temp/beta_sigmoid.csv"
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


if(NCOL(parameter_data) == 1){
  x_lab = names(parameter_data)[1]
  y_lab = NULL
  parameter_data = parameter_data %>% 
    rename(x = 1) 
} else {
  x_lab = names(parameter_data)[1]
  y_lab = names(parameter_data)[2]
  parameter_data = parameter_data %>% 
    rename(x = 1, y = 2) 
}


message("Read Data: Done./n")

##### Fit the data #############################################################
message("Fit Data./n")
print(pass_arguments[2])
switch(pass_arguments[2], 
       ##### Beta Sigmoid #####
       Beta_Sigmoid={
         
         # Get initial guess and some plotting values
         guess_A = mean(parameter_data$x)
         guess_B = guess_A/2
         
         # Fit the data
         model_fit = nlsLM(y ~ 1*(1+(A-(x))/(A-B))*((x)/A)^(A/(A-B)),
                         data = parameter_data,
                         start = list(A = guess_A, B = guess_B))
         bs_A_set = model_fit$m$getPars()["A"]
         bs_B_set = model_fit$m$getPars()["B"]
         
         # Make the tabluar output
        table_output = data.frame(Parameter = c("A", "B"),
                                  Estimate = c(bs_A_set, bs_B_set))
         
         # Make the fitted data set for plotting
         fit_predict = data.frame(x = seq(min(c(parameter_data$x,0)),
                                         max(parameter_data$x),
                                         length.out = 100)) %>%
           mutate(predict = predict(model_fit,
                                    newdata = .))
         
         # Make a display object for the model
         display = summary(model_fit)
   
       },
       ##### Linear #####
       Linear={
         
         # Get initial guess and some plotting values

         # Fit the data
         model_fit = lm(y ~ x, data = parameter_data)
         lin_A_set = model_fit$coefficients[1]
         lin_B_set = model_fit$coefficients[2]
         
         # Make the tabluar output
         table_output = data.frame(Parameter = c("Intercept", "Slope"),
                                   Estimate = c(lin_A_set, lin_B_set))
         
         # Make the fitted data set for plotting
         fit_predict = data.frame(x = seq(min(c(parameter_data$x,0)),
                                          max(parameter_data$x),
                                          length.out = 100)) %>%
           mutate(predict = predict(model_fit,
                                    newdata = .))
         
         # Make a display object for the model
         display = summary(model_fit)
         
       },
       ##### Log-Normal #####
       Log_Normal={
         
         # Fit the data
         model_fit = fitdistr(parameter_data$x, "lognormal")
         ln_mean = model_fit$estimate["meanlog"]
         ln_sd = model_fit$estimate["sdlog"]
         
         # Make the tabluar output
         table_output = data.frame(Parameter = c("Mean", "SD"),
                                   Estimate = c(ln_mean, ln_sd))
         
         # Make the fitted data set for plotting
         fit_predict = data.frame(x = seq(min(c(parameter_data$x,0)),
                                          max(parameter_data$x),
                                          length.out = 100)) %>%
           mutate(predict = dlnorm(x, meanlog = ln_mean, sdlog = ln_sd),
                  predict = predict/max(predict))
           
         
         # change the data for plotting
         parameter_data = parameter_data %>% 
           mutate(bin = cut(x, seq(min(x), max(x), length.out = 15), right = FALSE)) %>% 
           group_by(bin) %>% 
           summarise(y = n()) %>% 
           ungroup() %>%
           mutate(char = as.character(bin), 
                  low = as.numeric(str_match(char, "\\[\\s*(.*?)\\s*\\,")[,2]),
                  high = as.numeric(str_match(char, "\\,\\s*(.*?)\\s*\\)")[,2]),
                  x = (low + high)/2,
                  y = y/max(y)) %>% 
           select(x, y)
         
         # Make a display object for the model
         display = print(model_fit)
         
       },
       ##### Inverse #####
       Inverse={
         
         # Get initial guess and some plotting values
         guess_A = max(parameter_data$y) 
         guess_B = min(parameter_data$y)
         
         # Fit the data
         model_fit = nlsLM(y ~ (A/x) + B,
                        data = parameter_data,
                        start = list(A = guess_A, B = guess_B))
         i_A_set = model_fit$m$getPars()["A"]
         i_B_set = model_fit$m$getPars()["B"]
         
         # Make the tabluar output
         table_output = data.frame(Parameter = c("A", "B"),
                                   Estimate = c(i_A_set, i_B_set))
         
         # Make the fitted data set for plotting
         fit_predict = data.frame(x = seq(min(parameter_data$x),
                                          max(parameter_data$x),
                                          length.out = 100)) %>%
           mutate(predict = predict(model_fit,
                                    newdata = .))
         
         # Make a display object for the model
         display = summary(model_fit)
       },
       ##### Power #####
       Power={
         
         # Get initial guess and some plotting values
         guess_A = 1 
         guess_B = 1
         
         # Fit the data
         model_fit = nlsLM(y ~ A*x^B,
                       data = parameter_data,
                       start = list(A = guess_A, B = guess_B))
         i_A_set = model_fit$m$getPars()["A"]
         i_B_set = model_fit$m$getPars()["B"]
         
         # Make the tabluar output
         table_output = data.frame(Parameter = c("A", "B"),
                                   Estimate = c(i_A_set, i_B_set))
         
         # Make the fitted data set for plotting
         fit_predict = data.frame(x = seq(min(parameter_data$x),
                                          max(parameter_data$x),
                                          length.out = 100)) %>%
           mutate(predict = predict(model_fit,
                                    newdata = .))
         
         # Make a display object for the model
         display = summary(model_fit)
         
       },
       ##### Logistic #####
       Logistic={
         
         # arrange the data for a good plot
         parameter_data = arrange(parameter_data, x)
         
         # Fit the data
         model_fit = glm(parameter_data$y ~ parameter_data$x,
                            family=quasibinomial(logit),
                            data=parameter_data)
         l_A_set = model_fit$coefficients[1]
         l_B_set = model_fit$coefficients[2]
         
         l_10_set = -(log(1/0.1-1)+model_fit[[1]][1])/model_fit[[1]][2]
         l_90_set = -(log(1/0.9-1)+model_fit[[1]][1])/model_fit[[1]][2]
         
         # Make the tabluar output
         table_output = data.frame(Parameter = c("A", "B", "X10", "X90"),
                                   Estimate = c(l_A_set, l_B_set, l_10_set, l_90_set),
                                   Type = c( "Classic", "Calssic", "Model Input", "Model Input"))
         
         # Add in predictions for plotting
         fit_predict = parameter_data %>%  
           mutate(y = predict.glm(model_fit,
                                  type = "response")) %>% 
           rename(predict = y)
         
         # Make a display object for the model
         display = summary(model_fit)

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

file.remove(here(pass_arguments[3], "fhast_parameter_fit.png"))
message("Make Parameter report: Done./n")

message("!!! PARAMETER ESTIMATION COMPLETE !!!\n")

################################################################################
# End
################################################################################
