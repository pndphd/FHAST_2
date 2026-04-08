################################################################################
# This script takes two shape files (OHWM and project foot print) and gets
# overlap
################################################################################

##### Developer options ########################################################
# Uncomment for development to pick a specific file and run from IDE

if (!exists("pass_arguments")){
  pass_arguments = NULL
  pass_arguments[1] = "C:/Users/pndph/Desktop/temp/cmax.csv"
  pass_arguments[2] = "Beta Sigmoid"
}

################################################################################

##### Run setup ################################################################

# # install and load the here package if necessary
if(!require(c("here"), character.only = T)){install.packages(package)}

# Load Libraries
source(here("scripts","main","load_libraries.R"))
 
# Make blank list
ml = list(var = list(),
          df = list(),
          plot = list(),
          path = list(),
          string = list(),
          sum = list(),
          table = list())

# Load Functions





##### Read in data #############################################################
message("Read Data./n")
# Read in the data to fit
data = read.csv(pass_arguments[1])
message("Read Data: Done./n")

##### Fit the data #############################################################
message("Fit Data./n")
print(pass_arguments[2])
switch(pass_arguments[2], 
       Beta_Sigmoid={
         
         # Get initial guess and some plotting values
         guess_A = max(data$x)
         guess_B = guess_A/2
         
         # Fit the data
         bs_fit = nlsLM(value ~ 1*(1+(A-(temperature))/(A-B))*((temperature)/A)^(A/(A-B)),
                         data = green_sturgeon_data,
                         start = list(A = guess_A, B = guess_B))
         gs_A_set = gs_fit$m$getPars()["A"]
         gs_B_set = gs_fit$m$getPars()["B"]
         
         gs_predict <- data.frame(temperature = seq(0,35,1)) %>%
           mutate(predict = predict(gs_fit,
                                    newdata = .))
         
         plotName = ggplot(green_sturgeon_data, aes(x = temperature)) +
           theme_classic(base_size = 25) +
           theme(legend.title = element_blank())+
           labs(y = "Fraction of Cmax", x = "Temperature (\u00B0C)") +
           scale_x_continuous(limits = c(0, 30)) +
           geom_path(data = gs_predict, aes(y = predict, x = temperature),
                     color = "black", linewidth = 0.5) +
           coord_cartesian(ylim = c(0,1.0))+
           geom_point(aes(y = value, color = note),
                      shape = 1,
                      stroke = 1.5,
                      size = 5) +
           scale_color_manual(values = cbPalette,
                              labels = c("CTM", "cmax"))

       },
       Linear={
   
       },
       {
         message(paste0("!!!!!!!!!!!\n",
                        "!!!ERROR!!! Model type not recognized.\n",
                        "!!!!!!!!!!!\n"))
         stop()
         
       }
)

message("Fit Data: Done./n")


# # make feature lookup table
# ml$df$lookup_table = ml$df$footprint %>% 
#   select(Feature, Type, Started, Completed) %>% 
#   st_drop_geometry() %>% 
#   distinct() 
# 
# message("Calculate Summaries./n")
# 
# ml$df$footprint_in = ml$df$footprint %>% 
#   st_intersection(ml$df$ohwm) %>% 
#   mutate(OHWM = TRUE)
# 
# ml$df$footprint_out = ml$df$footprint %>% 
#   st_difference(ml$df$ohwm)
# 
# ml$df$footprint_out_dis = st_union(ml$df$footprint_out)
# 
# ml$df$footprint_in_dis = st_union(ml$df$footprint_in)
# 
# ml$df$footprint_processed = ml$df$footprint_out %>%  
#   bind_rows(ml$df$footprint_in) %>% 
#   mutate(area = st_area(.))
# 
# ##### Make table and summary stats #############################################
# 
# # Make a summary tabel
# ml$table$summary = ml$df$footprint_processed %>% 
#   st_drop_geometry() %>% 
#   group_by(Feature, Project, OHWM, Type, Started, Completed) %>% 
#   summarise(Area = as.numeric(round(sum(area),2))) %>% 
#   filter(Area != 0) %>% 
#   left_join(ml$df$lookup_table, by = c("Feature", "Type", "Started", "Completed")) %>% 
#   mutate(Feature = str_to_title(Feature),
#          Type = str_to_title(Type),
#          OHWM = ifelse(OHWM, "Inside", "Outside"))
# 
# # get the percent of total footprint in the ohwm
# ml$var$percent_in = ml$table$summary %>% 
#   group_by(OHWM) %>% 
#   summarise(area = sum(Area)) %>% 
#   mutate(total = sum(area),
#          percent = area*100/total) %>% 
#   filter(OHWM == TRUE) %>% 
#   .$percent %>% 
#   round(1)
# 
# # Get the total area  
# ml$var$total_area = sum(ml$table$summary$Area)
# 
# # get the units
# ml$var$measure_units = st_crs(ml$df$footprint_out_dis) %>%
#     .$units
# 
# message("Calculate Summaries: Done./n")
# 
# ##### Make plot ################################################################
# 
# message("Make Plots./n")
# 
# plot_data = ml$df$footprint_in %>%
#   left_join(ml$df$lookup_table, by = c("Feature", "Type")) %>%
#   rowwise() %>%
#   mutate(Feature = ifelse(str_length(Feature) > 45,
#                           paste0(str_sub(Feature, 1, 45), "..."),
#                           Feature))
# 
# ml$plot$output_map = ggplot(plot_data) +
#   theme_classic(base_size = 20) +
#   theme(axis.text.x = element_text(angle = 90),
#         legend.position = "top",
#         legend.direction ='vertical') +
#   geom_sf(aes(fill = factor(Feature)), color = "black") +
#   geom_sf(data = ml$df$footprint_out_dis, fill = "white") +
#   facet_wrap(.~ Type, ncol = 1)
#   labs(color = "test")
# 
# if (NROW(ml$df$footprint_in) > 12){
#   ml$plot$output_map = ml$plot$output_map +
#     scale_fill_viridis_d(name = "Feature") 
# } else {
#   ml$plot$output_map = ml$plot$output_map +
#     scale_fill_manual(name = "Feature",
#                       values = c("#88CCEE", "#CC6677", "#DDCC77",
#                                  "#117733", "#332288", "#AA4499",
#                                  "#44AA99", "#999933", "#882255",
#                                  "#661100", "#6699CC", "#888888"))
# }
# 
# ggsave(here(ml$path$output_folder, "ohwm_map.png"),
#        ml$plot$output_map,
#        height = 7 * length(unique(ml$df$footprint_in$Type)) + length(unique(ml$df$footprint_in$Feature))/12,
#        width = 7,
#        units = "in",
#        device = "png")
# 
# message("Make Plots: Done./n")
# 
# ##### Write Reports ############################################################
# 
# # make the html doc
# message("Make OHWM report./n")
# rmarkdown::render(input = here("scripts", "ohwm_analysis", "ohwm_report.Rmd"),
#                   output_format = "html_document",
#                   output_file = here(ml$path$output_folder, "ohwm_report.html"),
#                   quiet = TRUE)
# 
# message("Make OHWM report: Done./n")
# 
# ################################################################################
# # End
# ################################################################################
