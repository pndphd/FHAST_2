#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking "Run App" above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(shinyFiles)

input_tab <- tabPanel(
  "Configuration Directory",
  textInput("config_file", "Configuration File"),
  shinyFilesButton("picker_config_file", "Select Configuration File",
                     "Please select the Configuration File", FALSE),
  headerPanel(""),
  textInput("output_folder_path", "Output Folder"),
  shinyDirButton("picker_output_path", "Select Output Folder",
                 "Please select the Output Folder", FALSE),
)

input_file_tab <- tabPanel(
  "Input File",
  # Run name
  textInput("run_name", "Run Name"),

  # Notes
  textInput("notes_file", "Notes File"),
  shinyFilesButton("picker_notes_file", "Select Notes File",
                   "Please select the notes file", FALSE),
  textAreaInput("sim_ui_notes", "Simulation Notes", 
                width = "50%",
                height = "200px"),
  
  # Input folder
  textInput("raster_folder", "Depth and Velocity Raster Directory"),
  shinyDirButton("picker_raster_folder",
    "Select Depth and Velocity Raster Directory",
    "Please select the Depth and Velocity Raster Folder", FALSE),

  # Daily conditions
  textInput("daily_file", "Daily Conditions"),
  shinyFilesButton("picker_daily_file", "Select Daily Conditions",
    "Please select the Daily Conditions", FALSE),

  # Fish files
  textInput("fish_pop_file", "Fish Population"),
  shinyFilesButton("picker_fish_pop_file", "Select Fish Population",
    "Please select the Fish Population", FALSE),
  textInput("fish_params_file", "Fish Parameters"),
  shinyFilesButton("picker_fish_params_file", "Select Fish Parameters",
    "Please select the Fish Parameters", FALSE),
  # # Grid files
  textInput("grid_center_file", "Grid Center Line"),
  shinyFilesButton("picker_grid_center_file", "Select Grid Center Line",
    "Please select the Grid Center Line", FALSE),
  textInput("grid_top_file", "Grid Top Point"),
  shinyFilesButton("picker_grid_top_file", "Select Grid Top Point",
    "Please select the Grid Top Point", FALSE),
  textInput("interaction_file", "Interaction"),
  shinyFilesButton("picker_interaction_file", "Select Interaciton",
    "Please select the Interaction file", FALSE),
  # # Habitat input files
  textInput("cover_file", "Cover File"),
  shinyFilesButton("picker_cover_file", "Select Cover File",
    "Please select the Cover File", FALSE),
  textInput("canopy_cover_file", "Canopy Cover File"),
  shinyFilesButton("picker_canopy_cover_file", "Select Canopy Cover File",
    "Please select the Canopy Cover File", FALSE),
  textInput("hab_params_file", "Habitat Parameters"),
  shinyFilesButton("picker_hab_params_file", "Select Habitat Parameters",
    "Please select the Habitat Parameters", FALSE),
  # # Predator File
  textInput("predator_file", "Predator Parameters"),
  shinyFilesButton("picker_predator_file", "Select Predator Parameters",
    "Please select the Predator Parameters", FALSE),
  textInput("tree_growth_file", "Tree Growth"),
  shinyFilesButton("picker_tree_growth_file", "Select Tree Growth",
                   "Please select the Tree Growth", FALSE),
  # Optional area of interest
  textInput("aoi_file", "Optional Area of Interest"),
  shinyFilesButton("picker_aoi_file", "Select Area of Interest",
    "Please select the Area of Interest", FALSE),
  # Optional area of interest
  textInput("wild_file", "Optional Wildcard CSV"),
  shinyFilesButton("picker_wild_file", "Select Wildcard CSV",
                   "Please select the Wildcard CSV file", FALSE),
)

interaction_tab <- tabPanel(
  "Interactions",
  uiOutput("interactions_params_ui"),
)

fish_params_tab <- tabPanel(
  "Fish Parameters",
  uiOutput("fish_params_ui"),
)

habitat_params_tab <- tabPanel(
  "Habitat Parameters",
  uiOutput("habitat_params_ui"),
)

daily_con_hydrograph_tab <- tabPanel(
  "Hydrograph",
  value = "hydrograph",
  uiOutput("daily_hydro_ui"),
)

daily_con_link_tab <- tabPanel(
  "Link",
  value = "link",
  uiOutput("daily_link_ui"),
)

daily_con_distribution_tab <- tabPanel(
  "Distribution",
  value = "distribution",
  uiOutput("daily_dist_ui"),
)

daily_conditions_tab <- tabPanel(
  "Daily Conditions",
  tabsetPanel(
              id = "daily_type",
              type = "tabs",
              daily_con_hydrograph_tab,
              daily_con_link_tab,
              daily_con_distribution_tab,
              ),
)

predator_params_tab <- tabPanel(
  "Predator Parameters",
  uiOutput("pred_params_ui"),
)

# No tab for fish population, it"s a large spreadsheet and would be better
# edited in a spreadsheet program

output_tab <- tabPanel(
  "Output",
  plotOutput("daily_timeseries", height = "800px"),
  plotOutput("daily_histogram", height = "500px"),
  plotOutput("fish_timeseries"),
  plotOutput("map_preview"),
)


# Define UI for application that draws a histogram
shinyUI(fluidPage(
  tags$head(tags$style(type="text/css", "
                       body {padding-top: 420px;}
                       @media (min-width: 767px) { body{ padding-top: 160px;} }
                       @media (min-width: 1040px) { body{ padding-top: 120px;} }
                       @media (min-width: 1114px) { body{ padding-top: 70px;} }"
                       )),
  includeScript(path = "ui.js"),
  navbarPage("FHAST",
            input_tab,
            input_file_tab,
            interaction_tab,
            fish_params_tab,
            habitat_params_tab,
            daily_conditions_tab,
            predator_params_tab,
            output_tab,
            position="fixed-top",
            id="main_tabs",
            footer=tagList(
                hr(),
                actionButton("save", "Save"),
                uiOutput("validation_errors"),
                hr(),
                actionButton("graphs", "Save and Generate Graphs"),
                hr(),
                actionButton("html", "Save and Generate Report"),
              )
            )
))
