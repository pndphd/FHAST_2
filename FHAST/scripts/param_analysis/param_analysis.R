################################################################################
# This script takes two shape files (OHWM and project foot print) and gets
# overlap
################################################################################

##### Developer options ########################################################
# Uncomment for development to pick a specific file and run from IDE

if (!exists("pass_arguments")){
  pass_arguments = NULL
  pass_arguments[1] = "C:/Users/pndph/Desktop/temp/metabolic.csv"
  pass_arguments[2] = "Metabolic"
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
} else if(NCOL(parameter_data) == 2) {
  x_lab = names(parameter_data)[1]
  y_lab = names(parameter_data)[2]
  parameter_data = parameter_data %>% 
    rename(x = 1, y = 2) 
} else if(NCOL(parameter_data) == 4) {
  e_lab = names(parameter_data)[1]
  m_lab = names(parameter_data)[2]
  t_lab = names(parameter_data)[2]
  v_lab = names(parameter_data)[2]
  parameter_data = parameter_data %>% 
    rename(e = 1, m = 2, t = 3, v = 4) 
} else if(NCOL(parameter_data) == 7) {
  parameter_data = parameter_data %>% 
    rename(presence_absence = 1,
           depth = 2,
           velocity = 3,
           vegetation = 4,
           woody_debris = 5,
           substrate = 6,
           shade = 7) 
} else {
  message(paste0("!!!!!!!!!!!\n",
                 "!!!ERROR!!! Incorect Data Structure.\n",
                 "!!!!!!!!!!!\n"))
  stop()
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
         model_fit = glm(y ~ x,
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
       ##### Metabolic #####
       Metabolic={
         

         # Fit the data
         model_1_fit = glm(log(e) ~ 
                             log(m) +
                             log(t) +
                             v +
                             I(log(m) * log(t)),
                           data=parameter_data)
         model_2_fit = glm(log(e) ~ 
                             log(m) +
                             t +
                             v +
                             I(log(m) * log(t)),
                           data=parameter_data)
         model_3_fit = glm(log(e) ~ 
                             log(m) +
                             log(t) +
                             sqrt(v)+
                             I(log(m) * log(t)),
                           data=parameter_data)
         model_4_fit = glm(log(e) ~ 
                             log(m) +
                             log(t) +
                             v +
                             I(log(m) * t),
                           data=parameter_data)
         model_5_fit = glm(log(e) ~ 
                             log(m) +
                             t +
                             sqrt(v) +
                             I(log(m) * log(t)),
                           data=parameter_data)
         model_6_fit = glm(log(e) ~ 
                             log(m) +
                             t +
                             sqrt(v) +
                             I(log(m) * t),
                           data=parameter_data)
         model_7_fit = glm(log(e) ~ 
                             log(m) +
                             t +
                             v +
                             I(log(m) * t),
                           data=parameter_data)
         model_8_fit = glm(log(e) ~ 
                             log(m) +
                             log(t) +
                             sqrt(v) +
                             I(log(m) * t),
                           data=parameter_data)
         
         # put in a list to use a map call later
         model_fits = list(model_1_fit,
                           model_2_fit, 
                           model_3_fit,
                           model_4_fit,
                           model_5_fit,
                           model_6_fit,
                           model_7_fit,
                           model_8_fit)
         
         # Get RMSPE
         ape = map_df(model_fits,
                        ~data.frame(ape = 100 * mean(abs(parameter_data$e - exp(predict(.x)))/parameter_data$e)))
         
         # Make the tabluar output
         table_output = model_fits %>% 
           map2_df(seq(1,8),~ data.frame(Values = .x$coefficients,
                            Model = paste("Model", .y),
                            Parameter = names(.x$coefficients))) %>%
           mutate(Values = round(Values, 3)) %>%
           pivot_wider(names_from = Parameter, values_from = Values) %>% 
           cbind(data.frame(AIC = map(model_fits, AIC) %>% unlist())) %>%
           bind_cols(ape) %>% 
           arrange(AIC) %>% 
           rename(intecept = "(Intercept)",
                  "log(m) * log(t)"="I(log(m) * log(t))",
                  "log(m) * t" = "I(log(m) * t)",
                  "absolute percent error" =  "ape") 
         
         # Make a display object for the model
         display = list(summary(model_1_fit),
                        summary(model_2_fit),
                        summary(model_3_fit),
                        summary(model_4_fit),
                        summary(model_5_fit),
                        summary(model_6_fit),
                        summary(model_7_fit),
                        summary(model_8_fit))
         
        display =  walk(display, ~print(.x))
         
         
       },
       
       ##### Predator #####
       Predator={

         # up sample to get same number of P/A
         parameter_data_max = parameter_data %>%
           group_by(presence_absence) %>%
           mutate(n = n()) %>%
           ungroup() %>%
           filter(n == max(n))

         parameter_data_sampeled = parameter_data %>%
           group_by(presence_absence) %>%
           mutate(n = n()) %>%
           ungroup() %>%
           filter(n == min(n)) %>%
           sample_n(NROW(parameter_data_max), replace = TRUE) %>%
           bind_rows(parameter_data_max) %>% 
           select(-n)
         
         
         # Fit the data
         model_fit = glm(presence_absence ~
                           depth +
                           velocity +
                           vegetation +
                           woody_debris +
                           substrate +
                           shade,
                         family="binomial",
                         data=parameter_data_sampeled)
                         
         # Make the tabular output
         table_output = data.frame(Parameter = names(model_fit$coefficients),
                      Estimate = round(model_fit$coefficients, 3)) %>% 
             mutate(Parameter = str_replace(Parameter,"_", " ")) %>% 
             pivot_wider(names_from = Parameter, values_from = Estimate) %>% 
             rename(intecept = "(Intercept)") 
                         
         
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
if(pass_arguments[2] == "Metabolic" | pass_arguments[2] == "Predator"){
  plot_fit = NULL
  # Save the plot 
  ggsave(here(pass_arguments[3], "fhast_parameter_fit.png"),
         plot_fit,
         height = 0.1,
         width = 0.1,
         units = "in",
         device = "png",
         dpi = 300)
} else {
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
  # Save the plot 
  ggsave(here(pass_arguments[3], "fhast_parameter_fit.png"),
         plot_fit,
         height = 7,
         width = 7,
         units = "in",
         device = "png",
         dpi = 300)
}

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
