;; The FHAST program

;; Load Extensions
extensions [
  csv      ; The extenshion the allows for csv IO
  palette  ; Allows the use of more palets like ColorBrewer
  time     ; Use the LogoTime extenshion to tract dates/time
  table    ; Allows for use of tables instead of lists for speed reasons
  rnd      ; For random draws
  profiler ; includes primitives that measure how many times the procedures are called during a run and how long each call takes
]

;##### Define Variables #####################################################

;; Define global variables
globals [

  ;; General run setup variabels
  resolution          ; The grid resolution in meters
  resolution_file     ; the file that contaions the resolution and buffer information
  buffer              ; Set the buffer (only used to read in the files)
  resolution_factor   ; A factor used to control how large the display can get
  area_column         ; The location index for area of a cell read in from the flow CSV
  reach_start         ; The upper most reach distance
  reach_end           ; The bottom reach distance
  top_patches         ; The patches that are closest to the top and are wet


  ;; Internal parameter variables
  species_list         ; A list of species names
  fish_logistics_table ; A table of logistic functions for survival, by species

  ;; Time variables
  first_day           ; Pointless time variabel to initalize
  last_day            ; Time varible for the last day in the simulation
  tick_date           ; Variable to track date

  ;; Daily input variabels
  daily_input_csv          ; The daily flow and temperature data
  day                      ; The day of the simulation
  date                     ; A date value
  month                    ; The month (used for shade)
  flow_column              ; The location index for the flow from the daily CSV
  month_column             ; The location index for the months from the daily CSV
  daily_flow_values        ; The complete list of daily flow values
  month_values             ; A list of the months
  flow                     ; The daily flow value
  x_flow                   ; The location index for the x position of a cell read in from the flow CSV
  y_flow                   ; The location index for the y position of a cell read in from the flow CSV
  temp_column              ; The location index for the temperature from the daily CSV
  daily_temp_values        ; The complete list of daily temp values
  temperature              ; The daily temperature value
  turbidity_column         ; The column that gives the turbidity values
  daily_turbidity_values   ; The complete list of daily turbidity values
  turbidity                ; The daily turbidity
  photoperiod              ; daily photoperiod (day length) in hours
  daily_photoperiod_values ; The complete list of daily photoperiod values

  ;; Habitat and interaction params
  habitat_params_csv ; csv file with a variety of habitat params, including foods, predator density, resolution, buffer, etc.
  hab_drift_con      ; Availability of drift food in reach, (g/m^3)
  hab_ben_con        ; The econcentration of benthic food (g/m^2)
  hab_ben_ene        ; The energy density of the benthic food (J/g)
  hab_drift_ene      ; The energy density of the drift food (J/g)
  superind_ratio     ; how many fish each agent represents
  pred_per_area      ; The concentration of prerdators
  reaction_distance  ; The radius of the area covered by the predators
  t_area_effect      ; The extent to which temeprature can increase the predation effective ares
  d84_size           ; The grain size of the bed for the law of the wall calculation
  ben_vel_height     ; The height off the bed where the velocity is experienced by the benthic fish
  shelter_frac       ; Fraction of the cells velocity experienced by a fish in cover

  ; Percentt cover to distance to cover conversion
  int_pct_cover               ; the intercept of the percent cover to distance to cover relation
  sqrt_pct_cover              ; the sqrt root parameter of the percent cover to distance to cover relation
  pct_cover                   ; the the single poser parameter of the percent cover to distance to cover relation
  sqrt_pct_cover_x_pct_cover  ; the the 2/3 parameter of the percent cover to distance to cover relation

  ; Distance to cover to prey safety conversion
  dis_to_cover_par  ; the logistic parameter slop to convert distance to cover to survival benefit
  dis_to_cover_int  ; the logistic parameter intercept to convert distance to cover to survival benefit

  ; turbidity model params
  turb_int              ; the logistic parameter slope to convert turbidity to survival benefit
  turb_slope            ; the logistic parameter intercept to convert turbidity to survival benefit
  turb_survival_bonus   ; bonus to fish survival against preds due to turbidity updates dailys

  ;; Daily Fish input variables
  daily_fish_csv        ; The column that gives the number of fish per day
  fish_wo_dates         ; The info for the fish file with not date info
  paired_fish_list      ; The dates and lists paired
  fish_date_column      ; The column that gives the dates of fish entry
  number_column         ; The column that gives the number of fish
  species_column        ; The column the lists the species of fish
  lifestage_column      ; The column that lists the life stage
  length_column         ; The column the gives the fish lenght
  length_sd_column      ; The column that gives the fish lenght sd
  daily_number_values   ; The daily values for the fish counts
  daily_species_values  ; The daily values for the species
  daily_ls_values       ; The daily values for the lifestage
  daily_length_values   ; The daily values for the length
  daily_sd_values       ; The daily values for the sd of length
  fish_date_values      ; The values in the fish date columns
  fish_formated_dates   ; The values in the fish date columns formated as LogoTime

  ;; Variables used for drifter fish
  net_energy                       ; The net energy of the cells
  positive_energy_cell_count       ; A variable keeping track of whether a cell with positive net energy has been found
  all_net_energy                   ; A list of net energy values for the cells in the radius of the random drift cells
  closest_cell_with_pos_energy     ; The random drift cell closest to the agent that has positive net energy
  possible_wet_cells_in_radius     ; Cells in the radius of the random drift cells
  sorted_distance_cells            ; The random drift cells sorted in ascending order of distance to the agent
  no_cell_has_pos_energy           ; A boolean indicating whether any of the random drift cells have positive net energy

  ;; Flow raster variabels
  flow_input_csv      ; The variabel to hole the flow csv
  flow_values         ; The list of flow values for which we have rasters
  today_index         ; The flow index for each day
  wet_patches         ; A list of patches that have water in them each day
  max_depth           ; The max depth listed in any raster
  max_velocity        ; The max velcoity listed in any raster

  ;; Shape file variables
  shape_input_csv     ; The variabel to hole the shape csv
  x_shape             ; The location index for the x position of a cell read in from the shape CSV
  y_shape             ; The location index for the y position of a cell read in from the shape CSV
  wood_column         ; The column that has the information on percent wood
  cover_column        ; The column that has the cover fraction
  small_cover_column  ; The column that has the small cover fraction
  veg_column          ; The column that has the information on percent vegetation
  fine_column         ; The column that has the information on percent fine sediment
  gravel_column       ; The column that has the information on percent spawning gravel
  cobble_column       ; The column that has the information on percent large cobble
  rock_column         ; The column that has the information on percent rock or bedrock
  ben_food_column     ; The column that has the information on fraction of area that has benthic food
  canopy_column       ; The column that has the information on percent canopy cover
  photoperiod_column  ; The column that has the information on photoperiod

  ;; Display Variables
  max_cell_available_vel_shelter ; Max available area of velocity shelter from all cells (just used to color patches according to the available vel shelter)
  max_encounter_prob              ; Maximum encounter probability of predators for all cells (just used to color patches)

  ;; Fish variables
  fish_params_csv           ; A csv with the individual species parameters
  benthic_fish              ; Is the fish a benthic fish
  move_dist_a               ; Multiplier for maximum movement distance (unitless)
  move_dist_b               ; Exponent for maximum movement distance (unitless)
  length_mass_a             ; Site-specific length-weight relationship for fish in good condition
  length_mass_b             ; Site-specific length-weight relationship for fish in good condition
  territory_a               ; The intercept of the fish territory size equation
  territory_b               ; The slope of the fish territory size equation
  met_int                   ; intercept for metabolic rate equation
  met_lm                    ; log mass term for metabolic rate equation
  met_lt                    ; log temperature term for metabolic rate equation
  met_v                     ; log speed term for metabolic rate equation
  met_lm_lt                 ; log mass * log temperature term for metabolic rate equation
  met_t                     ; temperature term for metabolic rate equation
  met_lm_t                  ; log mass * temperature term for metabolic rate equation
  met_sqv                   ; the smolt flag factor for metabolic rate equation
  ;total_metab_rate          ; total metabolic rate
  cmax_a                    ; Allometric constant in cMax equation (unitless)
  cmax_b                    ; Allometric exponent in cMax equation (unitless)
  cmax_c                    ; First parameter for the cmax temperature relation (C)
  cmax_d                    ; Second parameter for the cmax temperature relation (C)
  feeding_speed             ; The feeding spped for benthic fish (bl/s)
  fish_detect_dist          ; Distance over which fish can see or attack (cm)
  react_dist_a              ; Intercept in equation for detection distance (cm) (CHANGED TO M)
  react_dist_b              ; Multiplier in equation for detection distance (unitless)
  turbid_threshold          ; Highest turbidity that causes no reduction in detection distance (NTU)
  turbid_min                ; Minimum value of the turbidity function (unitless)
  turbid_exp                ; Multiplier in exponential term for the turbidity function (unitless)
  fish_turbid_function      ; The value of the turbidity function changes each day
  capture_V1                ; Ratio of cell velocity to fish’s maximum swim speed at which capture success is 0.1 (unitless)
  capture_V9                ; Ratio of cell velocity to fish’s maximum swim speed at which capture success is 0.9 (unitless)
  energy_density            ; The ratio (J/g) between net energy intake and change in weight
  small_cover_length        ; The lenght below which fish can us small cover
  migration_max_dist        ; The maximum distance (in m) that a fish can migrate
  mort_condition_K1         ; Part of relationship between survival and condition (K); Fish condition factor K at which survival is 10 pct (unitless)
  mort_condition_K9         ; Part of relationship between survival and condition (K); Fish condition factor K at which survival is 90 pct (unitless)
  mort_high_temp_T1         ; Parameters for the logistic equation for high temp
  mort_high_temp_T9         ; Parameters for the logistic equation for high temp
  ucrit_a                   ; Parameters for max swimm speed vs lenght (this is the intercept)
  ucrit_b                   ; Parameters for max swimm speed vs lenght (this is the slope)
  ucrit_c                   ; Parameters for the max swimm speed temperature beta-sigmoid function (C)
  ucrit_d                   ; Parameters for the max swimm speed temperature beta-sigmoid function (C)
  smolt_P1                  ; Parameters for the logistic equation for the probability of smolting depending on photoperiod- Photoperiod where probability of being in the "smolting window" is 10 pct
  smolt_P9                  ; Parameters for the logistic equation for the probability of smolting depending on photoperiod- Photoperiod where probability of being in the "smolting window" is 90 pct
  smolt_max_L1              ; Parameters for the logistic equation for the probability of smolting depending on flength- Length in which probability of smolting is 10 pct
  smolt_max_L9              ; Parameters for the logistic equation for the probability of smolting depending on flegnth- Length in which probability of smolting is 90 pct
  outmigrate_V1             ; Parameters for the logistic equation for the probability of outmigrating depending on the increase in mean velocity from running average velocity -
  outmigrate_V9             ; Parameters for the logistic equation for the probability of outmigrating depending on the increase in mean velocity from running average velocity -

  ;; End of simulation outputs
  death_temp_table            ; A list of 1s representing deaths caused by temperature
  death_velocity_table        ; A list of 1s representing deaths caused by velocity
  death_stranding_table       ; A list of 1s representing deaths caused by stranding
  death_pred_table            ; A list of 1s representing deaths caused by predation
  death_condition_table       ; A list of 1s representing deaths caused by poor condition
  smolt_count_table           ; A list of 1s representing smolts that day
  ;smolt_length_list           ; A list of smolts' length that day
  ;smolt_mass_list             ; A list of smolts' mass that day
  ;smolt_condition_list        ; A list of smolts' condition that day
  nonmigrants_count_table        ; A list of 1s representing nonsmolts that day
  nonmigrants_length_list        ; A list of nonsmolts' length that day
  nonmigrants_mass_list          ; A list of nonsmolts' mass that day
  nonmigrants_condition_list     ; A list of nonsmolts' condition that day
  migrant_count_table         ; A list of 1s representing migrants that day
  migrant_length_list         ; A list of the migrants' length when it exits the river
  migrant_mass_list           ; A list of the migrants' mass when it exits the river
  migrant_condition_list      ; A list of the migrants' condition when it exits the river
  drifter_count_table         ; A list of 1s representing drifters that day
  drifter_length_list         ; A list of the drifters' length when it exits the river
  drifter_mass_list           ; A list of the drifters' mass when it exits the river
  drifter_condition_list      ; A list of the drifters' condition when it exits the river

  ;; Daily outputs
  dead_fish_count_table       ; A list of 1s representing all of the dead fish (includes smolts and nonsmolts) that day
  dead_migrants_count_table   ; A list of 1s representing all of the dead migrants that day
  ;dead_smolts_count_table     ; A list of 1s representing all of the dead smolts that day
  dead_nonmigrants_count_table  ; A list of 1s representing all of the dead nonsmolts that day
  dead_rearing_count_table    ; A list of 1s representing all of the dead nonsmolts with positive growth that day
  total_daily_juveniles       ; Total number of juveniles (smolts and nonsmolts) at any given timestep
  total_daily_dead_fish       ; Total number of dead fish (smolts and nonsmolts) at any given timestep
  total_daily_dead_migrants   ; Total number of dead migrants at any given timestep
  ;total_daily_dead_smolts     ; Total number of dead smolts at any given timestep
  total_daily_dead_nonmigrants  ; Total number of dead nonsmolts at any given timestep
  total_daily_migrants        ; Total number of migrants at any given timestep
  ;total_daily_smolts          ; Total number of fish smolting at any given timestep
  total_daily_nonmigrants       ; Total number of non smolting fish at any given timestep (not including migrating fish)
  total_daily_drifters        ; Total number of fish drifting at any given timestep

  ;; Other global variables/inernal data structures
  mortality_events_outfile_name     ; String with name of mortality events output file; set in build_output_files
  fish_events_outfile_name          ; String with name of fish events output file; set in build_output_files
  cell_info_outfile_name            ; String with name of cell info output file; set in build_output_files
  detailed_population_outfile_name  ; String with name of detailed population output file; set in build_output_files
  all_cell_outfile_name
  path_info_outfile_name
  cell_info_list                    ; List of all destination cell information (number of total fish alive in each destination, number of dead fish in each destination) per time step that can be written the the cell info outputs file
  fish_events_list                  ; List of all individual fish-related events (mortality, smolting, migrating) that can be written the the fish events outputs file
  detailed_population_list          ; List of all summary fish-related info per day (total migrating, total smolting) that can be written to the detailed population output file
  all_cell_attributes_list
  migrant_path_info_list
  next_output_time                  ; A LogoTime for when the next file output is scheduled.
  shade_variable                    ; Controls patch shading. Equal to "velocity", "depth", "light" or "off"
  all_cells
  destination_cells                 ; A list of all of the destination cells during a time step
  cmax_temp_func                    ; A list of cmax temperature functions for each species
  max_swim_temp_func                ; A list of cmax temperature functions for each species

  ;; Predator variables
  pred_input_file_csv          ; Input csv file with some default params for pred counts
  total_preds                  ; The total number of predators in the system

  ;; Predator model variables
  pred_species      ; A list of the species of predators
  num_pred_species  ; the number of predators

  ;; glm for habitat rating
  int_glm          ; A prameter for predatror intercept
  shade_glm        ; A prameter for how the predators react to shade
  veg_glm          ; A prameter for how the predators react to vegetation
  wood_glm         ; A prameter for how the predators react to wood
  depth_glm        ; A prameter for how the predators react to depth
  velocity_glm     ; A prameter for how the predators react to velocity
  substrate_glm    ; A prameter for how the predators react to substrate

  ; params for log-normal distribution
  meanlog     ; Parameter for fish lenght distributions
  sdlog       ; Parameters fo rfish lenght distribution

  ; gape limitation params
  a_gape     ; intercept fo the gape limitation of a predator
  B_gape     ; slope for the gape limitation of a predator

  ; temp vs pred activity params
  pred_temperature_activity  ; the temperature logistic function for predator space coverage slope
  int_temp                   ; the temperature logistic function for predator space coverage intercept

  ; pathfinding data holders
  pathfinding_dirty_patches      ; patch-set of patches that have pathfinding data that need to be cleared.
]

;; Define patch variables
patches-own [

  ;; Geometry variabels
  x_pos  ; equal to "lat_dist" in the flow and shapefile input files
  y_pos  ; equal to "distance" in the flow and shapefile input files

  ;; Flow releated variables
  area                ; The true area of the patch (not the area displayed here) (CHANGED TO M)
  wetted_fraction     ; the fraction of the area that is wetted
  wetted_fractions    ; the list of fraction of the area that is wetted
  wetted_area         ; the total area wetted (CHANGED TO M)
  depths              ; A list of all the depths at the set flows in the cell
  today_depth         ; The depth of the patch on this day (CHANGED TO M)
  yesterday_depth     ; The depth of the patch on the previous day. (CHANGED TO M)
  velocities          ; A list of all the velocities at the set flows in the cell
  today_velocity      ; The velocity of the patch on this day
  yesterday_velocity  ; The velocity of the patch on the previous day.

  ;; Shape file releated variables
  veg                 ; the fraction of the area that is covered with vegetation
  wood                ; the fraction of the area that is covered with wood
  fine                ; the fraction of the area that is covered with fine sediment
  gravel              ; the fraction of the area that is covered with gravel
  cobble              ; the fraction of the area that is cobble
  rock                ; the fraction of the area that is rock
  shades              ; All the shade values a call can have
  shade               ; The shade fraction of a cell
  ben_food_fra        ; The fraction of the cell area that has benthic food

  ;; Parameters for valid patch logic for fish
  has_visited?        ; Used to identify if the pathfinding has visited the patch
  path_to_here_cost   ; Used to store the cost to move to this patch for pathfinding
  path_survival       ; Used to store the predation risk along this path
  fish_survival       ; Survival for current fish in this path
  previous_patch      ; The previous patch in the path from pathfinding
  path_score          ; Score evaluating how good of a patch this is for the next step of the migration pathing

  frac_velocity_shelter     ; The fraction of a cell with velocity shelters (the wood + veg sum)

  cell_available_ben         ; Availability of denthic food in, g
  cell_available_vel_shelter ; Available area of velocity shelter in cell, (m^2)
  cell_available_wet_area    ; Available wetted area in cell, (m^2)

  ratio_vel_max_swim         ; Ratio of the cell velocity and the maximum swim speed sustained by a fish
  capture_area               ; The area over which fish can capture food
  swim_speed                 ; (m/s)
  capture_success            ; The fraction of food items passing through the capture area that are actually caught
  feed_time                  ; Number of house spend feeding per day (set at 12)

  distance_to_drifter           ; Distance a patch is to a drifting fish
  closest_random_cell           ; When the fish disperses downstream, it selects the closest random cell from "random_drift_downstream_cells" - used for drifters
  all_downstream_cells          ; All of the valid downstream cells of a drifter fish
  random_drift_downstream_cells ; the random cells selected for drif
  open_cells_for_dispersal      ; All of the wet cells within the new area that the fish (a drifter) can disperse to

  active_metab_rate
  passive_metab_rate
  total_metab_rate           ; total metabolic rate
  daily_intake               ; Drift intake (g/d), limited by cmax, drift availability etc
  daily_energy_intake        ; Drift intake in J energy
  daily_net_energy           ; Drift intake - total respiration (J/d)
  total_net_energy_in_cell   ; Total net energy in the cell (g) (basically equal to the daily net energy, can be negative)
  total_mort_risk_for_cell   ; Total probability of surviving all of the mortality risks in the cell (total_mort_risk_for_cell/total_net_energy_in_cell)
  ratio_net_energy_risk      ; Ratio of total mortality risk to the net energy in the cell
  consider_path_risk         ; Path survival multiplied by the ratio net energy to risk. Used by fish when selecting desination cells while taking into account path risk

  fish_death_hightemp_prob          ; Probability of a fish surviving high temperature
  ratio_swim_speed_max_swim_speed   ; Ratio of swim speed to the max swim speed that can be sustained by fish
  fish_death_aq_pred_prob           ; Probability of a fish surviving predation by other fish

  count_fish_destination                 ; Total number of fish alive in a cell at the end of a timestep

  avg_weight_fish_in_destination         ; Average weight of live fish in a cell at the end of a timestep
  avg_length_fish_in_destination         ; Average length of live fish in a cell at the end of a timestep
  avg_condition_fish_in_destination      ; Average condition of live fish in a cell at the end of a timestp

  running_average_velocity              ; The mean velocity that the fish has experienced over the last 5 time steps
  migrant_patch                         ; Identifies the patch as having a migrant juvenile in it at any given timestep

  ;; Predator-related parameters
  substrate                             ; A binary value used by the predator model
  hab_rating                            ; Rating of habitat quality for predators
  partial_hab_rating                    ; Part of the hab rating calc is done at set up to save time
  adj_hab_rating                        ; hab_rating weighted by the amount of wetted area in a patch
  num_preds                             ; Number of predators in a patch
  pred_length                           ; Mean length of predators in a cell
  max_prey_length                       ; Largest prey size that a given predator can consume based on its length
  encounter_prob                        ; Probability of encountering a predator in a cell
  cover                                 ; Total cover available to prey for predator avoidance
  small_cover                           ; Total cover available to small prey for predator avoidance
  distance_to_cover                     ; Average distance a fish needs to travel to reach cover in a patch
  distance_to_small_cover               ; Average distance a small fish needs to travel to reach cover in a patch
  cover_bonus                           ; The "bonus" to survival in a predator-prey encounter provided by cover
  small_cover_bonus                     ; The "bonus" to survival in a predator-prey encounter provided by small cover
  survival_prob                         ; The probability a prey fish survives an encounter based on the cover bonus and pred success rate
  small_survival_prob                   ; The probability a small prey fish survives an encounter based on the cover bonus and pred success rate
]

;; Define agent variables
turtles-own [

  ;; Species
  species_id   ; The assigned number for this species
  species      ; The species name

  ;; Physological parameters
  mass                 ; Mass
  start_mass           ; Mass at beginning of time step
  f_length             ; Fork length
  start_length         ; Fork length at beginning of time step
  change_length        ; Change in fork length
  healthy_mass         ; Mass for a healthy condition factor
  percent_daily_growth ; Percent that the daily growth is of its mass

  fish_sex             ; Sex of fish
  fish_condition       ; Condition factor K (values 0 - 1, fish condition)
  previous_condition   ; Condition before the fish grows (condition at the beginning of timestep that drives habitat selection)
  daily_growth         ; Growth per day (g)
  max_swim_speed       ; Maximum sustainable swim speed for a fish
  new_length           ; Used in "grow" procedure - equal to previous length + change in length
  new_mass             ; Used in "grow" procedure - equal to previous mass + growth
  new_condition        ; Used in "grow" procedure
  desired_length       ; Length for a healthy individual of weight
  cmax                 ; Maximum daily consumption rate as limited by its physiology (g/d)
  energy_intake        ; J/d

  exit_status          ; If the fish is exiting this turn
  strand_status        ; If the fish is getting stranded this turn

  patch_radius              ; Radius (in cells) representing where the fish can move in one time step
  territory_size            ; The fish territory size
  fish_in_radius            ; Count of number of fish in the radius before the fish decides its destination cell
  dispersal_distance        ; If the fish is a drifter, this is the max area it can dirft to
  destination               ; The cell that the fish moves to by the end of the time step
  wet_cells_in_radius       ; The cells that are in a fish's radius

  mean_velocity_in_radius   ; The mean velocity that the fish experiences in its radius

  reachable_patches         ; Patches the agent can migrate to
  min_pycor_reachable_patches ; The pycor of the patch at the very edge of the the max movement radius. Will usually be reach_end
  downstream_patches        ; Patches downstream of a juvenile

  fish_death_starv_survival_prob  ; Probability of suriviving starvation from poor condition
  fish_smolting_prob_photoperiod  ; Probability of being in the "smolting window"
  fish_smolting_prob_flength      ; Probability of smolting based on length
  overall_smolting_prob           ; Product of prob of smolting based on photoperiod and prob of smolting based on flength
  fish_outmigration_prob_velocity ; Probability of outmigrating due to velocity
  overall_outmigration_prob       ; Overall probability of outmigrating due to changes in velocity, length, and photoperiod
  velocity_experience_list        ; List of mean radius cell velocity fish experience each day
  path_survival_list              ; ; A list of path survival probabilities for drifter fish (should only have max two elements inside)

  is_in_shelter                   ; If the fish is using shelter
  is_smolt                        ; If the fish has undergone smoltification (depending on photoperiod and size)
  is_migrant                      ; If the fish has decided to migrate (depending on change in flow)
  is_alive                        ; If the fish is alive
  is_drifter                      ; A boolean for whether fish is drifting downstream due to crappy habitat
  starving?                       ; A booleam for whether the fish is starving (true if random number greater than prob of starving)
  drifter_history                 ; string showing whether drifter was only a drifter for one timestep

  ;; Intermediate variables to reduce calcs.,
  fish_resp_std_wt_term           ; resp-A * wt ^ resp-B
  fish_max_speed_len_term         ; max-swim-A * L + max-swim-B
  fish_cmax_wt_term               ; cmax-A * wt ^ (1+cmax-B)
  max_swim_l_term                 ; speed-A * l ^ (speed-B)

  fish_logistic_table             ; Table holding the logistic functions

  fallback_migration_patch                ; A patch that the fish can reach within the max move distance of a call to find drift destinations
  fallback_migration_patch_path_survival  ; Path survival of the fallback_migration_patch

  pathfinding_list_x
  pathfinding_list_y
]

;##### Setup Breeds ########################################################
breed [adults adult]
breed [spawners spawner]
breed [eggs egg]
breed [juveniles juvenile]
breed [migrants migrant]

;##### Define Repeated Use Functions #######################################
;; Make a tabel for the CSV fish params inputs
to-report make_table_from_csv [#csv_file]

  let parameter_names (map [n -> item 0 n ] #csv_file)
  let parameter_values  (map [n -> but-first n] #csv_file)
  ; Combine the last to to make a paired list then a table
  let paired_param_list (map [ [ a b ] -> ( list a b ) ] parameter_names parameter_values)

  report table:from-list paired_param_list
end

;; A reporter to evalulate the logistic function
to-report evaluate_logistic [ a_logistic_name a_species an_input ]
  ; An observer reporter to report the value of a survival logistic

  let the_table (table:get (table:get fish_logistics_table a_species) a_logistic_name)
  let Z (table:get the_table "logistic_a") + ((table:get the_table "logistic_b") * an_input)
  ; Defensive programming to avoid over/underflow runtime errors
  if Z < -200 [ report 0.0 ]
  if Z >   35 [ report 1.0 ]

  report (exp Z) / (1.0 + exp Z)   ; Calculating exp(Z) twice does not slow execution

end

;##### Setup Actions #######################################################
;; Run the setup actions whe setup button is presed
to setup


 ; Basic reset procedure
  clear-all                           ; Clear the entire space
  reset-ticks                         ; Reset time ticks
  set-default-shape turtles "dot"     ; Set the default turtel shape to dot

  ; Read in files and set resolution
  set habitat_params_csv csv:from-file word run_folder "/habitat.csv"                  ; Read in general habitat params
  set_habitat_params                                                                  ; Sets numerous values including resolution and buffer
  set resolution_factor 600                                                           ; Set the resolution factor
  set daily_input_csv csv:from-file word run_folder "/daily_input_file.csv"            ; Read in the daily flow and temperature
  set flow_input_csv csv:from-file
    (word run_folder "/Depth_Velocity_Data_Input.csv")                            ; Read in the depth CSV
  set shape_input_csv csv:from-file
    (word run_folder "/Shape_Data_Input.csv")                                     ; Read in the shape file
  set daily_fish_csv csv:from-file word run_folder "/daily_fish_input.csv"             ; Read in the daily fish csv
  set fish_params_csv csv:from-file word run_folder "/fish_params_input.csv"           ; Read in the daily fish csv
  set pred_input_file_csv csv:from-file word run_folder "/predator_params_input.csv"   ; Read in the predator input csv

  ;; Get the indexes for the columns in each file
  set day (position "day" (item 0 daily_input_csv))
  set date (position "date" (item 0 daily_input_csv))
  set flow_column (position "flow_cms" (item 0 daily_input_csv))
  set month_column (position "month" (item 0 daily_input_csv))
  set temp_column (position "temp_c" (item 0 daily_input_csv))
  set turbidity_column (position "turb_ntu" (item 0 daily_input_csv))
  set photoperiod_column (position "photoperiod" (item 0 daily_input_csv))

  ; Set the initial and end time
  set first_day time:create-with-format item date (item 1 daily_input_csv) "MM/dd/yyyy"
  ; Get a zero day so ticaks line up with the first day
  let zero_day time:plus first_day -1.0 "days"
  set last_day time:create-with-format item date (item (length daily_input_csv - 1) daily_input_csv) "MM/dd/yyyy"
  set tick_date (time:anchor-to-ticks zero_day 1 "days")

  ;; For the fish parameters
  set species_list but-first (item 0 fish_params_csv)

  ;; From the fish daily input file
  set number_column (position "number" (item 0 daily_fish_csv))
  set species_column (position "species" (item 0 daily_fish_csv))
  set fish_date_column (position "date" (item 0 daily_fish_csv))
  set length_column (position "length" (item 0 daily_fish_csv))
  set length_sd_column (position "length_sd" (item 0 daily_fish_csv))
  set lifestage_column (position "lifestage" (item 0 daily_fish_csv))

  ;; From the flow inputs
  set x_flow (position "lat_dist" (item 0 flow_input_csv)) ;shows which column lat_dist is in csv, and then which element is first in the column
  set y_flow (position "distance" (item 0 flow_input_csv))
  set area_column (position "area" (item 0 flow_input_csv))

  ;; From the shape input file
  set x_shape (position "lat_dist" (item 0 shape_input_csv))
  set y_shape (position "distance" (item 0 shape_input_csv))
  set canopy_column (position "height" (item 0 shape_input_csv))
  set wood_column (position "wood" (item 0 shape_input_csv))
  set cover_column (position "cover_fra" (item 0 shape_input_csv))
  set small_cover_column (position "small_cover_fra" (item 0 shape_input_csv))
  set veg_column (position "veg" (item 0 shape_input_csv))
  set fine_column (position "fine" (item 0 shape_input_csv))
  set rock_column (position "rock" (item 0 shape_input_csv))
  set cobble_column (position "cobble" (item 0 shape_input_csv))
  set gravel_column (position "gravel" (item 0 shape_input_csv))
  set ben_food_column (position "ben_food_fra" (item 0 shape_input_csv))

  ; Initialize the cmax_tempfunction with an empty list
  set cmax_temp_func n-values length species_list [1]

  ; Initialize the cmax_tempfunction with an empty list
  set max_swim_temp_func n-values length species_list [1]

  ;; Set the size of the world
  set_world_size

  ;; Initialize patch data for pathfinding
  ask patches  [
    set has_visited? false
    set previous_patch nobody
    set path_to_here_cost -1
    set path_survival -1
    set fish_survival -1
    set path_score -1
  ]

  ;; Initalize some global lists
  set_lists

  ;; Get all the flow values that we have input rasters for
  set_temp_turbidity_flow_photoperiod

  ;; Get the daily values from the fishh input
  set_daily_fish_counts

  ;; Set the fish parameters
  set_fish_parameters

  ;; Set each patch flow values
  set_patch_flow_values

  ;; Set each patch shade values
  set_patch_shade_values

  ;; Set each patches values from the shape file
  set_patch_habitat_values

  ;; Set the count tables for the print out
  set_count_tabels

  ;; Set substrate values to patches for predators
  set_substrate_values

  ;; Build the logistic functions for the fish
  build_logistic_functions

  ;; Load in model parameters for predators
  set_pred_params

  ;; Habitat rating pre-calculations
  set_partial_hab_rating

  set pathfinding_dirty_patches no-patches

end

;; Set the size of the world
to set_world_size

  ; Get necessary information to set up world size
  let x_values (map [n -> item x_flow n ] flow_input_csv)  ; Read in all the x positions
  let y_values (map [n -> item y_flow n ] flow_input_csv)  ; Read in all the y positions
  let x_max max x_values                                   ; Get the max x value
  let x_min min x_values                                   ; Get the min x value
  let y_max max y_values                                   ; Get the max y value

  ; Resize the world and patchs
  resize-world (x_min / (resolution)) (x_max / (resolution)) 0 (y_max / (resolution))
  ; Set the patch size to be 1 or larger (if reasonable)
  set-patch-size max (list 1 ((resolution / y_max) * resolution_factor))

end

;; Setup habitat parameters
to set_habitat_params
  let paired_param_table make_table_from_csv habitat_params_csv

  ; feeding params
  set hab_drift_con item 0 (table:get paired_param_table "hab_drift_con")
  set hab_ben_con item 0 (table:get paired_param_table "hab_bentic_con")
  set hab_ben_ene item 0 (table:get paired_param_table "hab_bentic_ene")
  set hab_drift_ene item 0 (table:get paired_param_table "hab_drift_ene")
  set superind_ratio item 0 (table:get paired_param_table "superind_ratio")

  ; reach params
  set resolution item 0 (table:get paired_param_table "resolution")
  set buffer item 0 (table:get paired_param_table "buffer")
  set pred_per_area item 0 (table:get paired_param_table "pred_per_area")
  set shelter_frac item 0 (table:get paired_param_table "shelter_frac")
  set reaction_distance item 0 (table:get paired_param_table "reaction_distance")
  set t_area_effect item 0 (table:get paired_param_table "t_area_effect")

  ; pct cover to distance to cover conversion
  set int_pct_cover item 0 (table:get paired_param_table "int_pct_cover")
  set sqrt_pct_cover item 0 (table:get paired_param_table "sqrt_pct_cover")
  set pct_cover item 0 (table:get paired_param_table "pct_cover")
  set sqrt_pct_cover_x_pct_cover item 0 (table:get paired_param_table "sqrt_pct_cover_x_pct_cover")

  ; dis to cover to prey safety conversion
  set dis_to_cover_par item 0 (table:get paired_param_table "dis_to_cover_m")
  set dis_to_cover_int item 0 (table:get paired_param_table "dis_to_cover_int")

  ; turbidity survival bonus params
  set turb_int item 0 (table:get paired_param_table "turbidity_int")
  set turb_slope item 0 (table:get paired_param_table "turbidity_slope")

  ; benthic velocity reduction parameters
  set ben_vel_height item 0 (table:get paired_param_table "ben_vel_height")
  set d84_size item 0 (table:get paired_param_table "d84_size")

end

;; Initialize some global lists
to set_lists

  ; Observer procedure that initializes global variables.
  set detailed_population_outfile_name "d-p-o-n" ; String with temporary name of detailed population output file; reset in build_output_file
  set fish_events_outfile_name "f-e-o-n" ; String with temporary name of fish events output file; reset in build_output_file
  set cell_info_outfile_name "c-i-o-n"   ; String with temporary name of destination cell info output file; reset in build_output_file
  set all_cell_outfile_name "a-c-o-n" ; String with temporary name of all cell info output file; reset in build_output_file

  ; Set up lists to track events
  set fish_events_list (list)    ; List keeping track of individual fish-related events including whether the fish died, smolted, migrated etc
  set cell_info_list (list)    ; List keeping track of destination cell-related info including the number of fish in a destination cell at every time step, number of dead fish at a destination cell at every time step etc
  set detailed_population_list (list) ; List keeping track of summary fish-related info per day including the total number of fish that died per day, total alive, total migrating, etc
  set all_cell_attributes_list (list) ; ; List keeping track of all cell info per day (for mapping and testing purposes)

end

;; Set the world values that are the same for every cell
to set_temp_turbidity_flow_photoperiod

  ; Get the temperature, turbidity, and photoperiod values from the daily input
  set daily_temp_values but-first (map [n -> item temp_column n ] daily_input_csv)
  set daily_turbidity_values  but-first (map [n -> item turbidity_column n ] daily_input_csv)
  set daily_photoperiod_values but-first (map [n -> item photoperiod_column n ] daily_input_csv)

  ; Get the flow values from the daily input
  set daily_flow_values but-first (map [n -> item flow_column n ] daily_input_csv)  ; Read in all the x positions
  let flow_header item 0 flow_input_csv

  ; Get the first row of the CSV
  let flow_columns filter [ s -> member? "mean.D" s ] flow_header    ; Get only column headders with mean in the name
  let flow_values_str map [ s -> remove "mean.D" s ] flow_columns    ; Take out the prefix
  set flow_values map [ s -> read-from-string s ] flow_values_str    ; Covnert the strings to number values
  set flow_values insert-item 0 flow_values 0.0                      ; Add zero to the start

end

;; Set up the number of fish that get added to the model every day
to set_daily_fish_counts

  set fish_date_values but-first (map [n -> item fish_date_column n ] daily_fish_csv)
  ; Get all things in the fish input file except date
  ; This is to make a table later on
  set fish_wo_dates but-first (map [n -> but-first n] daily_fish_csv)
  ; Combine the last to to make a paired list then a table
  set paired_fish_list (map [ [ a b ] -> ( list a b ) ] fish_date_values fish_wo_dates)
  set daily_number_values but-first (map [n -> item number_column n ] daily_fish_csv)
  set daily_species_values but-first (map [n -> item species_column n ] daily_fish_csv)
  set daily_ls_values but-first (map [n -> item lifestage_column n ] daily_fish_csv)
  set daily_length_values but-first (map [n -> item length_column n ] daily_fish_csv)
  set daily_sd_values but-first (map [n -> item length_sd_column n ] daily_fish_csv)
  set fish_formated_dates (map [n -> (time:create-with-format n "MM/dd/yyy")] fish_date_values)

  ; take off fish that arive before sim window
  loop [
    ; check if the list is empty
    ifelse empty? paired_fish_list = false [
      ; get teh first on the list in the correct format
      let check_day time:create-with-format item 0 (item 0 paired_fish_list) "MM/dd/yyyy"
      ; compare to the first day and if defore remove it
      ifelse time:is-before? check_day first_day [

        print (word "Fish set to arrive early. Removed day " check_day)
        set paired_fish_list but-first paired_fish_list][stop]
    ][stop]
  ]

end

;; Set up the parameter values for the fish
to set_fish_parameters

  let paired_param_table make_table_from_csv fish_params_csv

  set benthic_fish (table:get paired_param_table "benthic_fish")
  set cmax_a (table:get paired_param_table "cmax_a")
  set cmax_b (table:get paired_param_table "cmax_b")
  set cmax_c (table:get paired_param_table "cmax_c")
  set cmax_d (table:get paired_param_table "cmax_d")
  set feeding_speed (table:get paired_param_table "feeding_speed")
  set react_dist_a (table:get paired_param_table "react_dist_a")
  set react_dist_b (table:get paired_param_table "react_dist_b")
  set turbid_threshold (table:get paired_param_table "turbid_threshold")
  set turbid_min (table:get paired_param_table "turbid_min")
  set turbid_exp (table:get paired_param_table "turbid_exp")
  set energy_density (table:get paired_param_table "energy_density")
  set territory_a (table:get paired_param_table "territory_a")
  set territory_b (table:get paired_param_table "territory_b")
  set length_mass_a (table:get paired_param_table "length_mass_a")
  set length_mass_b (table:get paired_param_table "length_mass_b")
  set capture_V1 (table:get paired_param_table "capture_V1")
  set capture_V9 (table:get paired_param_table "capture_V9")
  set met_int (table:get paired_param_table "met_int")
  set met_lm (table:get paired_param_table "met_lm")
  set met_lt (table:get paired_param_table "met_lt")
  set met_v (table:get paired_param_table "met_v")
  set met_lm_lt (table:get paired_param_table "met_lm_lt")
  set met_t (table:get paired_param_table "met_t")
  set met_lm_t (table:get paired_param_table "met_lm_t")
  set met_sqv (table:get paired_param_table "met_sqv")
  set turbid_threshold (table:get paired_param_table "turbid_threshold")
  set turbid_min (table:get paired_param_table "turbid_min")
  set turbid_exp (table:get paired_param_table "turbid_exp")
  set ucrit_a (table:get paired_param_table "ucrit_a")
  set ucrit_b (table:get paired_param_table "ucrit_b")
  set ucrit_c (table:get paired_param_table "ucrit_c")
  set ucrit_d (table:get paired_param_table "ucrit_d")
  set move_dist_a (table:get paired_param_table "move_dist_a")
  set move_dist_b (table:get paired_param_table "move_dist_b")
  set mort_high_temp_T1 (table:get paired_param_table "mort_high_temp_T1")
  set mort_high_temp_T9 (table:get paired_param_table "mort_high_temp_T9")
  set mort_condition_K1 (table:get paired_param_table "mort_condition_K1")
  set mort_condition_K9 (table:get paired_param_table "mort_condition_K9")
  set smolt_P1 (table:get paired_param_table "smolt_P1")
  set smolt_P9 (table:get paired_param_table "smolt_P9")
  set smolt_max_L1 (table:get paired_param_table "smolt_max_L1")
  set smolt_max_L9 (table:get paired_param_table "smolt_max_L9")
  set outmigrate_V1 (table:get paired_param_table "outmigrate_V1")
  set outmigrate_V9 (table:get paired_param_table "outmigrate_V9")
  set small_cover_length (table:get paired_param_table "small_cover_length")
  set migration_max_dist (table:get paired_param_table "migration_max_dist")

end

;; Assign each of the cells all its flow values
to set_patch_flow_values

  ;; Assign all the patches list of depths to have -9999 to rep no data
  ask patches [
    set depths (map [n -> 0] flow_values)
    set velocities (map [n -> 0] flow_values)
    set wetted_fractions (map [n -> 0] flow_values)
  ]

  ;; Populate each patch with depth data
  ;; Take each line in the csv
  foreach (but-first flow_input_csv) [n ->
    ; Move over each patch using its location and value
    ask patch ((item x_flow n) / (resolution)) ((item y_flow n) / (resolution)) [
      ; Set its x and y position, so that a map can later be made in R
      set x_pos (item x_flow n)
      set y_pos (item y_flow n)
      ; Set the area value
      set area (item area_column n)  ; area is in m2
      let counter 0
      ; Assign all the flow values and an index for them
      foreach but-first flow_values [m ->
        ; Use the flow values combined with the data type to get the depth values
        let m_column (position (word "mean.D" m) (item 0 flow_input_csv)) ; Gives the row (position) of meanD1,2,3... of the first item of flow_input
        let depth_input (item m_column n)
        set depths (replace-item counter depths max list depth_input 0) ; Replace the depth place holder with the actual or depth zero if - depth
        set max_depth max (list depth_input max_depth)       ; Check to see if this is a new max depth
        ; Use the flow values combined with the data type to get the velocity values
        let p_column (position (word "mean.V" m) (item 0 flow_input_csv))
        let velocity_input (item p_column n)
        set velocities (replace-item counter velocities max list velocity_input 0) ; Replace the depth place holder with the actual or depth zero if - depth
        set max_velocity max (list velocity_input max_velocity)       ; Check to see if this is a new max depth
        ; Use the flow values combined with the data type to get the wetted fraction
        let q_column (position (word "wetd.D" m) (item 0 flow_input_csv))
        let wetted_input (item q_column n)
        set wetted_fractions (replace-item counter wetted_fractions max list wetted_input 0) ; replace the depth place holder with the actual or depth zero if - depth
        set counter counter + 1
      ]
      set depths insert-item 0 depths 0.0  ; Add zero to the start
      set velocities insert-item 0 velocities 0.0  ; Add zero to the start
    ]
  ]

  set today_index floor (length flow_values / 2)     ; "floor" finds largest number less than or equal to the length of "flow_values/2"; Set the index to a starting value

end

;; Assign each of the cells all its shade values
to set_patch_shade_values

  set month_values but-first (map [n -> item month_column n ] daily_input_csv)  ; Read in all the x positions
  ;; Assign all the patches list of depths to have -9999 to rep no data
  ask patches [
    set shades (map [n -> 0] (range 1 13))
  ]
  ;; Populate each patch with depth data
  ;; Take each line in the csv
  foreach (but-first shape_input_csv) [n ->
    ; Move over each patch using its location and value
    ask patch ((item x_shape n) / (resolution)) ((item y_shape n) / (resolution)) [
      ; Set the area value
      let counter 0
      ; Assign all the flow values and an index for them
      foreach (range 1 13) [m ->
        ; Use the flow values combined with the data type to get the depth values
        let m_column (position (word "shade_" m) (item 0 shape_input_csv))
        let shade_input (item m_column n)
        set shades (replace-item counter shades max list shade_input 0) ; Replace the depth place holder with the actual or depth zero if - depth
        set counter counter + 1
      ]
    ]
  ]

end

;; Assign each of the cells all of the values associated with shapefiles (also in this section, the lists for mortality count and visit counts are initialized), and set whether they have a migrant in them to 'false'
to set_patch_habitat_values

  ;; Now do the same but for the shapes
  foreach (but-first shape_input_csv) [n ->
    ask patch ((item x_shape n) / (resolution)) ((item y_shape n) / (resolution)) [
      set wood (item wood_column n) ; Used for relief for predation
      set cover (item cover_column n)
      set small_cover (item small_cover_column n)
      set gravel (item gravel_column n)
      set veg (item veg_column n) ; Used for cover relief for predation
      set fine (item fine_column n)
      set rock (item rock_column n)
      set cobble (item cobble_column n)
      set ben_food_fra (item ben_food_column n)
    ]
  ]

end

;; set up the tabels to track counts of types of fish
to set_count_tabels
  ; update list of daily fish counts for detailed population output
  set death_temp_table table:make
  set death_velocity_table table:make
  set death_stranding_table table:make
  set death_pred_table table:make
  set death_condition_table table:make

  ; List of various fish variables recorded per day
  ;set smolt_count_table table:make
  set nonmigrants_count_table table:make
  set migrant_count_table table:make
  set drifter_count_table table:make

  set dead_fish_count_table table:make
  set dead_migrants_count_table table:make
  ;set dead_smolts_count_table table:make
  set dead_nonmigrants_count_table table:make
  set dead_rearing_count_table table:make
end

;; To set substrate values to patches for predators
to set_substrate_values

  ask patches [
    set substrate (gravel + cobble + rock)
    ifelse (substrate >= fine and substrate > 0) [
      set substrate 1
    ][
      set substrate 0
    ]
  ]

end

;; Bulid the logistic function
to build_logistic_functions

  ; An observer procedure to create logistic functions used in survival and other fish functions.
  ; Logistic functions are stored in a table; they can differ among species.
  ; Create the table.
  set fish_logistics_table table:make

  ; Build a table of functions for each species.
  foreach species_list [ next_species ->
    let the_species_table table:make
    let the_spp_index position next_species species_list

    ; Poor condition
    create_logistic_with_table_and_params the_species_table
    "poor_condition" (item the_spp_index mort_condition_K1) 0.1 (item the_spp_index mort_condition_K9) 0.9

    ; Capture success for drift feeding
    create_logistic_with_table_and_params the_species_table
    "capture_success" (item the_spp_index capture_V1) 0.1 (item the_spp_index capture_V9) 0.9

    ; High temperature
    create_logistic_with_table_and_params the_species_table
    "high_temperature" (item the_spp_index mort_high_temp_T1) 0.1 (item the_spp_index mort_high_temp_T9) 0.9

    ; Probability of smolting depending on fork length
    create_logistic_with_table_and_params the_species_table
    "smolt_flength" (item the_spp_index smolt_max_L1) 0.1 (item the_spp_index smolt_max_L9) 0.9

    ; Probability of being in the "smolting window" depending on photoperiod
    create_logistic_with_table_and_params the_species_table
    "smolt_photoperiod" (item the_spp_index smolt_P1) 0.1 (item the_spp_index smolt_P9) 0.9

    ; Probability of outmigrating given the percent increase in mean velocity of the search radius from the mean running average velocity of search radius throughout the last 5 days
    create_logistic_with_table_and_params the_species_table
    "outmigrate_velocity" (item the_spp_index outmigrate_V1) 0.1 (item the_spp_index outmigrate_V9) 0.9

    table:put fish_logistics_table next_species the_species_table
  ]

end

;; Make the logistic table
to create_logistic_with_table_and_params [a_table a_name x1 p1 x2 p2]
  ; An observer reporter to initialize a logistic function.
  ; p1 and p2 are the probabilities associated with inputs x1 and x2

  ; For convenience in test output, make sure X1 is less than X2
  ; This flips both relative to eachother and dose not change relatioships
  if x1 > x2 [
    let a_num x2
    set x2 x1
    set x1 a_num
    set a_num p2
    set p2 p1
    set p1 a_num
  ]

  ; Calculate the internal parameters
  let C ln (p1 / (1 - p1))
  let D ln (p2 / (1 - p2))
  let logistic_b (C - D) / (x1 - x2)
  let logistic_a C - (logistic_b * x1)

  let a_subtable table:make
  table:put a_subtable "logistic_b" logistic_b
  table:put a_subtable "logistic_a" logistic_a

  table:put a_table a_name a_subtable

end

;; set the predation parameters
to set_pred_params
  let paired_param_table make_table_from_csv pred_input_file_csv

  set pred_species (table:get paired_param_table "term")
  set num_pred_species length pred_species

  ; glm for habitat rating
  set int_glm (table:get paired_param_table "int")
  set shade_glm (table:get paired_param_table "shade")
  set veg_glm (table:get paired_param_table "veg")
  set wood_glm (table:get paired_param_table "wood")
  set depth_glm (table:get paired_param_table "depth")
  set velocity_glm (table:get paired_param_table "velocity")
  set substrate_glm (table:get paired_param_table "substrate")

  ; params for log-normal distribution
  set meanlog (table:get paired_param_table "pred_length_mean")
  set sdlog (table:get paired_param_table "pred_length_sd")

  ; gape limitation params
  set a_gape (table:get paired_param_table "gape_a")
  set B_gape (table:get paired_param_table "gape_b")

  ; temp vs pred activity params
  set pred_temperature_activity (table:get paired_param_table "area_pred_b")
  set int_temp (table:get paired_param_table "area_pred_a")

end

;; Does part of the habitat rating calculation for variables that do not change during the time steps
to set_partial_hab_rating

  ask patches [
    set partial_hab_rating []
    foreach range length pred_species [n ->
      set partial_hab_rating lput (item n int_glm + item n wood_glm * wood + item n veg_glm * veg + item n substrate_glm * substrate) partial_hab_rating
    ]
  ]

end

;##### Run Actions #######################################################
to go
  ; Setup anc chack model time
  tick

  if ticks = 1 [ reset-timer ]
  ; Check if the simulation is over
  if time:is-equal? tick_date last_day = TRUE [
    show (word "Simulation finished in " timer " seconds.")
    update_output
    stop
  ]
  print tick_date

  ; Clear the display
  clear-drawing

  ; Set up patches
	update_habitat
  set_boundaries
  set_shade
  set_dist_to_cover_values
  set_cover_bonus
  set_survival_prob
  place_predators

  ; Color Patches
  color_patches

  ; Do fish actions
  hatch_fish
  rear_fish

  ; Save output info
  save_destination_cell_info
  save_detailed_population_info
  save_all_cell_info

end

;; Updates variables that change daily (flow, depth, velocity, temperature, turbidity, food predator-related variables  in each cell)
to update_habitat

  ; Set today's reach temperature
  set temperature (item ticks daily_temp_values)

  ; Set today's reach turbidity
  set turbidity (item ticks daily_turbidity_values)

  ; Set today's photoperiod
  set photoperiod ((item ticks daily_photoperiod_values)) * 24  ; photoperiod in hours

  ; Caclulate and set today's flow values for the reach (depth and velocity)
  set flow (item ticks daily_flow_values)
  if flow > max flow_values [
  ; Check if it is outside the range of flows
    user-message "The daily flow value is greater than the raster input files.\nThe program will halt."
  ]
  if flow <= 0 [
  ; Check if it is outside the range of flows
    user-message "There is no flow in the system.\nAll your fish are dead.\nThe program will halt."
  ]
  let high_flow min filter [i -> i >= flow] flow_values     ; Find the closest flow in flow_values which is greater than or equal to the current daily value
  let low_flow  max filter [i -> i < flow]  flow_values     ; Find the closest flow in flow_values which is less than the current daily value
  let flow_fraction (flow - low_flow) / (high_flow - low_flow)  ; Calculate the fraction of distance the flow is form the low flow
  set today_index position low_flow flow_values

  ; Color the patches based on user selection
  ask patches [
    set pcolor black
    ifelse ticks = 1 [
      set yesterday_depth 1
    ][
      set yesterday_depth today_depth
    ]
    let low_depth  (item today_index depths)
    let high_depth (item (today_index + 1) depths)
    set today_depth (low_depth * (1 - flow_fraction) + high_depth * (flow_fraction))    ; Depth is in meters
    if today_depth <= 0 [set today_depth 0]
    ; Do the same for velotity
    set yesterday_velocity today_velocity
    let low_velocity  (item today_index velocities)
    let high_velocity (item (today_index + 1) velocities)
    set today_velocity (low_velocity * (1 - flow_fraction) + high_velocity * (flow_fraction))       ; Velocity is in m/s
    ; Do the same for wetted fraction
    let low_wetted  (item today_index wetted_fractions)
    let high_wetted (item (today_index + 1) wetted_fractions)
    set wetted_fraction (low_wetted * (1 - flow_fraction) + high_wetted * (flow_fraction))
    set wetted_area area * wetted_fraction
    ; if today_velocity <= 0 [set today_velocity 0]
  ]

  set wet_patches patches with [today_depth > 0]         ; Select patches with water

    ; Ask patches to update their depleted variables (velocity shelter availability, available hiding places, and drift)
  ask wet_patches [
    set frac_velocity_shelter veg + wood  ; the fraction of the cell that has velocity shelter is the sum of the fraction covered by vegetation and wood
    set cell_available_vel_shelter (wetted_area * frac_velocity_shelter)   ; available velocity shelter per cell (m^2)
    set cell_available_wet_area wetted_area   ; available velocity shelter per cell (m^2)
    set cell_available_ben  wetted_area * hab_ben_con * ben_food_fra ; available drift food in g/m3
  ]

  foreach species_list [ next_species ->
    ; update list of daily fish counts for detailed population output
    table:put death_temp_table next_species 0
    table:put death_velocity_table next_species 0
    table:put death_stranding_table next_species 0
    table:put death_pred_table next_species 0
    table:put death_condition_table next_species 0

    ; List of various fish variables recorded per day
    ;table:put smolt_count_table next_species 0
    table:put nonmigrants_count_table next_species 0
    table:put migrant_count_table next_species 0
    table:put drifter_count_table next_species 0

    table:put dead_fish_count_table next_species 0
    table:put dead_migrants_count_table next_species 0
    ;table:put dead_smolts_count_table next_species 0
    table:put dead_nonmigrants_count_table next_species 0
    table:put dead_rearing_count_table next_species 0
  ]

  ; Update intermediate variables that depend on temperature
  set turb_survival_bonus set_turb_bonus turb_int turb_slope turbidity

  ; Update the temperature cmax ans swimm speed fuinction for each fish species
  foreach species_list [ next_species ->
    let index (position next_species species_list)
    let c_par item index (cmax_c)
    let d_par item index (cmax_d)
    ; Use the beta sigmoid function for cmax temp
    set cmax_temp_func replace-item index cmax_temp_func ((1 + (c_par - temperature) / (c_par - d_par)) * (temperature / c_par) ^ (c_par / (c_par - d_par)))

    let e_par item index (ucrit_c)
    let f_par item index (ucrit_d)
    ; Use the beta sigmoid function for cmax temp
    set max_swim_temp_func replace-item index max_swim_temp_func ((1 + (e_par - temperature) / (e_par - f_par)) * (temperature / e_par) ^ (e_par / (e_par - f_par)))
  ]

end

;; Calculate the turbidity bonous of each cell
to-report set_turb_bonus [#turb_int #turb_slope #turbidity]

  let exponent -1 * (#turb_int + #turb_slope * #turbidity)
  report 1 / (1 + exp exponent )

end

;; This will set some boundaries of the reach based on flow
to set_boundaries

  ;set wet_patches patches with [today_depth > 0]         ; Select patches with water
  set reach_start max [pycor] of wet_patches             ; Get the highest patch distance value
  set reach_end min [pycor] of wet_patches               ; Get the lowest patch distance value
  set top_patches wet_patches with [pycor = reach_start] ; Get the highest patchs that are wet

end

;; Set the shade value of each cell
to set_shade

  ; get todays month value
  set month (item ticks month_values)
  ask wet_patches [
    set pcolor black
    set shade item (month - 1) shades
  ]

end

;; Calculate distance to cover based on percent cover
to set_dist_to_cover_values

  ask wet_patches [
    let patch_width sqrt wetted_area
    set distance_to_cover (int_pct_cover + sqrt_pct_cover * (sqrt cover) + pct_cover * cover + sqrt_pct_cover_x_pct_cover * (cover ^ 1.5)) * patch_width
    set distance_to_small_cover (int_pct_cover + sqrt_pct_cover * (sqrt small_cover) + pct_cover * small_cover + sqrt_pct_cover_x_pct_cover * (small_cover ^ 1.5)) * patch_width
  ]

end

;; Calculate the bonus to prey fish from cover in a patch
to set_cover_bonus

  ask wet_patches [
    ifelse cover > 0 [
      let exponent -1 * (dis_to_cover_int + dis_to_cover_par * distance_to_cover)
      set cover_bonus 1 / (1 + exp exponent)
    ][
      set cover_bonus 0
    ]

    ifelse small_cover > 0 [
      let exponent -1 * (dis_to_cover_int + dis_to_cover_par * distance_to_small_cover)
      set cover_bonus 1 / (1 + exp exponent)
    ][
      set small_cover_bonus 0
    ]
  ]

end

;; Calculate the probability of prey survivng a predator encounter based on amount of cover, turbidity, and pred success rate
to set_survival_prob

  ask wet_patches [
    set survival_prob  (1 - ((1 - turb_survival_bonus) * (1 - cover_bonus)))
    set small_survival_prob  (1 - ((1 - turb_survival_bonus) * (1 - small_cover_bonus)))
  ]

end

;; Determine the number of predators in each patch
to place_predators
  ; calculate the total number of predators in the reach on that time tick

  let total_wetted_area (sum [wetted_area] of wet_patches)
  set total_preds round (total_wetted_area * pred_per_area )

  ;; Calculate habitat ratings for each patch and predator species
  ask wet_patches [
    ; only do calculations if there is water in a patch
    ;ifelse (wetted_area > 0)
    ;[
      ; set an empty list to save habitat ratings for each species
      set hab_rating []

      set adj_hab_rating []

      ; a binary version of shade used by the model
      let shade_binary shade
      ifelse (shade_binary >= 0.5) [set shade_binary 1] [set shade_binary 0]

      ; calculate the habitat rating for each predator species
      foreach (range num_pred_species) [ n ->
        let exponent -1 * (item n partial_hab_rating + item n shade_glm * shade_binary + item n depth_glm * today_depth + item n velocity_glm * today_velocity)
        let model_prediction 1 / (1 + exp exponent)
        ; values < 0.5 indicate predictions of predator absence, so vals are set to 0
        ;ifelse (model_prediction < 0.5) [set model_prediction 0] [set model_prediction model_prediction]
        set hab_rating lput model_prediction hab_rating
        set adj_hab_rating lput (model_prediction * wetted_area) adj_hab_rating
      ]
  ]
  ;; End hab rating calcs

  ;; Calculate number of predators of each species and predator length
  ; Calculate the total hab rating across all patches for each predator
  ; used for calculating the number of predators in each cell
  let total_hab_rating []
  let all_wetted_vals ([wetted_area] of wet_patches)
  ; calculate the sum of wetted_area * hab_rating for each species across all patches
  ; used for weighting hab_rating values to predict the number of predators
  foreach (range num_pred_species) [n ->
    ; restructures the habitat ratings into a list of lists in which each sublist contains all values for a particular species
    ; initially, the sublists contain values for all species in each patch rather than all values for each species across all patches
    let hab_list (map [x -> item n x] ([adj_hab_rating] of wet_patches))
    set total_hab_rating lput (sum hab_list) total_hab_rating
  ]

  ask wet_patches [
    set num_preds []
    set pred_length []
    foreach (range num_pred_species) [n ->
      ; use the total preds in the system, patch habitat rating, and wetted area to calculate actual predator numbers
      let temp_pred_num 0
      if item n total_hab_rating > 0 [
        set temp_pred_num round (item n adj_hab_rating / item n total_hab_rating * total_preds)
      ]

      ; draw predator lengths from a log-normal distribution
      ;let mu item 0 butfirst item n butfirst pred_length_dist_params
      ; let sigma item 1 butfirst item n butfirst pred_length_dist_params
      ; filter predators that are above 15 cm
      let pred_length_list filter [i -> i >= 15] (n-values temp_pred_num [x -> exp random-normal item n meanlog item n sdlog ])

      ifelse (length pred_length_list > 0) [
        set pred_length lput pred_length_list pred_length
        set num_preds lput length pred_length_list num_preds
      ][
        set pred_length lput 0 pred_length
        set num_preds lput 0 num_preds
      ]
    ]

    ; combine the list-of-lists for pred_length into a single list
    set pred_length filter [i -> i > 0] (flatten pred_length)
    ; calculate pred_length as the average of all predator lengths across all species
    if length pred_length > 0 [
      ; set the patch's pred_length value to a random length from the list
      set pred_length item (random length pred_length) pred_length
      ; Need to change to allow different values of a_gape and B_gape if we want different values for each pred species
      set max_prey_length get-max-prey-length item 0 a_gape item 0 B_gape pred_length
    ]
    ;; End of pred counts and length calculations

    ;; Calculate proportional patch area occupied by predators
    set encounter_prob []
    foreach (range num_pred_species) [n ->
      ; calculate the effect of temperature on predator activity
      let exponent -1 * (item n int_temp + temperature * item n pred_temperature_activity)
      let pred_temperature_effect 1 / (1 + exp exponent)
      ; encounter_prob is simply the area occupied by predators divided by the wetted area of the patch
      set encounter_prob lput ((item n num_preds) * (reaction_distance + t_area_effect * pred_temperature_effect) / wetted_area) encounter_prob
    ]
    ; probability of encounter across all predator species
    set encounter_prob sum encounter_prob
  ]

end

;; Flatten a list of lists
to-report flatten [#list]
  set #list fput 0 #list ;; and a sacrificial scalar to the front of the list
  set #list ( reduce [ [ a b ] -> ( sentence a b) ] #list )
  report but-first #list ;; remove the sacrificial scalar before reporting
end

;; Calculate the maximum prey lenght of a predator
to-report get-max-prey-length [#a #B #pred_length]
  report exp (#a + #B * (#pred_length ^ 2))
end

;; Set the color of the cells/patches based on user input (right now colored by depth)
to color_patches

  if background_display != "none" [

    set max_cell_available_vel_shelter [cell_available_vel_shelter] of max-one-of patches [cell_available_vel_shelter] ; this is very ugly code (only used to color patches by max cell available shelter)
    set max_encounter_prob [encounter_prob] of max-one-of patches [encounter_prob]

    ask patches [
      if today_velocity <= 0 [set today_velocity 0]
      (ifelse
        background_display = "depth" [
          if (today_depth > 0)[
            set pcolor palette:scale-gradient palette:scheme-colors "Sequential" "YlGnBu" 9 today_depth 0 (max_depth)]
        ]
        background_display = "velocity" [
          if (today_depth > 0)[
            set pcolor palette:scale-gradient palette:scheme-colors "Sequential" "YlOrRd" 9 today_velocity 0 (max_velocity)]
        ]
        background_display = "wood" [
          if (today_depth > 0)[
            set pcolor palette:scale-gradient palette:scheme-colors "Sequential" "Oranges" 9 wood 0 1]
        ]
        background_display = "veg" [
          if (today_depth > 0)[
            set pcolor palette:scale-gradient palette:scheme-colors "Sequential" "PuRd" 9 veg 0 1]
        ]
        background_display = "shade" [
          if (today_depth > 0)[
            set pcolor palette:scale-gradient palette:scheme-colors "Sequential" "BuGn" 9 shade 0 1]
        ]
        background_display = "wetted fraction" [
          if (today_depth > 0)[
            set pcolor palette:scale-gradient palette:scheme-colors "Sequential" "Blues" 9 wetted_fraction 0 1]
        ]
        background_display = "predator encounter prob" [
          if (today_depth > 0)[
            set pcolor palette:scale-gradient palette:scheme-colors "Divergent" "RdYlBu" 9 encounter_prob 0 (max_encounter_prob)]
        ]
        background_display = "available velocity shelter" [
          if (today_depth > 0)[
            set pcolor palette:scale-gradient palette:scheme-colors "Sequential" "Purples" 9 cell_available_vel_shelter 0 (max_cell_available_vel_shelter) ]

        ]
      )
    ]
  ]

end

;; Add new fish to the reach (currently, only chinook juveniles are added, for testing)
to hatch_fish

  loop [
    ; get todays date
    let todays_date time:show tick_date "MM/dd/yyyy"
    ; check if today data exists in the first entry in the fish list
    ; and that the list is not empty
    let todays_fish_check false
    ifelse empty? paired_fish_list = false [
       set todays_fish_check position todays_date item 0 paired_fish_list
    ][stop]
    ; if it doden't stop the loop
    if todays_fish_check = false [stop]
    ; if the dates match, make the first fish entry a entry to be added today for today
    let todays_fish item 1 item 0 paired_fish_list
    ; now take it out so it's not added again
    set paired_fish_list but-first paired_fish_list

    ; Add in fish based on life stage
    ;  if item (lifestage_column - 1) todays_fish = "adult" [
    ;    create-adults (item (number_column - 1) todays_fish )[
    ;      set species (item (species_column - 1) todays_fish )
    ;      set species_id (position species species_list)
    ;
    ;      set f_length (item (length_column - 1) todays_fish ) ; fish length is in cm
    ;      set mass (item species_id (length_mass_a)) * (f_length ^ (item species_id (length_mass_b))) ; mass is in g
    ;      set fish_condition 1.0
    ;
    ;      set territory_size (item species_id territory_a) * f_length ^ (item species_id territory_b)
    ;
    ;      set size 2
    ;      set shape "fish"
    ;      set destination one-of wet_patches with [today_velocity < 100]  ; Place the turtle in a wet patch
    ;      move-to destination
    ;      set color red
    ;      set exit_status 0
    ;
    ;     ; Memory lists
    ;      set velocity_experience_list (list) ; A list of destination cell velocity fish experience each day
    ;
    ;      set is_in_shelter false        ; A boolean for whether trout is drift-feeding in velocity shelter
    ;      set is_alive true
    ;
    ;      ;save_event "initialized"
    ;    ]
    ;  ]

    if item (lifestage_column - 1) todays_fish = "juvenile" [
      create-juveniles (item (number_column - 1) todays_fish )[
        set species (item (species_column - 1) todays_fish )
        set species_id (position species species_list)

        set f_length (item (length_column - 1) todays_fish ) ; fish length is in cm
        set mass (item species_id (length_mass_a)) * (f_length ^ (item species_id (length_mass_b)))
        set fish_condition 1.0

        set territory_size (item species_id territory_a) * f_length ^ (item species_id territory_b)

        set size 2
        set shape "fish"
        set destination one-of wet_patches with [(today_velocity < .2 and today_velocity > .17) and today_depth > .15 and frac_velocity_shelter > 0]
        move-to destination
        set color red
        set exit_status 0

        ; Memory lists
        set velocity_experience_list (list) ; A list of destination cell velocity fish experience each day

        set is_in_shelter false          ; A boolean for whether trout is drift-feeding in velocity shelter.
        ;set is_smolt false               ; A boolean for whether fish has smolted.
        set is_migrant false             ; A boolean for whether fish has migrated
        set is_alive true                ; A boolean for whether fish is alive
        set is_drifter false             ; A boolean for whether fish is drifting downstream due to crappy habitat
        set starving? []
      ]
    ]
  ]

end

;; Have the fish do rearing actions
to rear_fish
  foreach sort-on [-1 * f_length] turtles [
    next_fish -> ask next_fish [
      ; Each fish completes the following procedures in order of longest to shortest
      update_fish
      find_potential_destination_cells
      calculate_starvation_prob
      calculate_outmigration_probability

      if is_migrant = true [
        migrate
        survive
      ]

      if is_migrant = false [
        ; If a fish decides not to migrate, it performs the following procedures in order
        ; If we set the fish to drift based on having no destination cells, skip this attempted move logic.
        ; The select_destination_cell funciton will in most cases set is_drifter to false which prevents
        ; the desired drift to avoid stranding behavior.
        if not is_drifter [
          calculate_energy_balance
          calculate_mortality_risk
          select_destination_cell
        ]

        if is_drifter = true [
          ; the fish checks whether it will have any positive net energy in any of the search radius cells. If not, it can move to another farther area
          drift_downstream
          ; If there are valid drift destination, calculate the net energy of the cells in radius of the random valid drift destinations identified
          ifelse any? random_drift_downstream_cells = TRUE [
            ifelse exit_status != 1 [
              ; If there are radius cells within the random valid drift destinations identified (exit_status = 0), calculate net energy/mortality and select destination cell
              calculate_net_energy_of_drift_cells
              calculate_mortality_risk
              select_destination_cell
            ][
              ; If there are no radius cells within the random valid drift destinations identified that have positive net energy, exit the river
              select_destination_cell
            ]
          ][
            ; If there are no valid drift destinations, the fish either strands or exits the river (even if they aren't at the end of the reach)
            select_destination_cell
          ]
        ]

        if exit_status != 1 or strand_status != 1 [
          ; If the fish have not stranded or exited the river, they grow and deplete destination resources
          deplete_destination_resources
        ]
        survive ; All fish go through the survive procedure
        grow
      ]
    ]
  ]

end

;; Update the fish variables that change every time step (turbidity functions, etc)
to update_fish

  ; Re-set the fish in shelter variable to false
  set is_in_shelter false

  if mass <= 0 [set mass .001] ; If mass is negative, set it to a very small number to calculate log mass in metabolic rate equation

  ; Cmax weight term
  set fish_cmax_wt_term (item species_id cmax_a) * (mass ^ (1 + item species_id cmax_b))
  ; Calculate cmax (g/d)
  set cmax fish_cmax_wt_term * item species_id cmax_temp_func

  ; Swim speed length term (convert form BL/s and come cm to m)
  set max_swim_l_term ((item species_id ucrit_a) / f_length + (item species_id ucrit_b)) * f_length / 100
  ; Calculate max swimm speed (BL/s)
  set max_swim_speed max_swim_l_term * item species_id max_swim_temp_func

  ; Update the turbidity function
  ifelse turbidity <= item species_id turbid_threshold [
    set fish_turbid_function 1.0
  ][
    set fish_turbid_function (item species_id turbid_min) + (1.0 - (item species_id turbid_min)) *
    exp ((item species_id turbid_exp) * (turbidity - (item species_id turbid_threshold)))
    ;show fish_turbid_function
  ]

   ; set the distance that fish can detect/react to prey
   set fish_detect_dist ((item species_id react_dist_a) + (item species_id react_dist_b * f_length)) * fish_turbid_function ; meters

   ; Reset the path survival list (in case they move to two cells while drifting
   set path_survival_list []

end

;; Find all of the potential destination cells that the fish can choose to move to
to find_potential_destination_cells

  ;print "find potential dest cells"

  ; Number of patches within the maximum distance that a fish can travel. Essentially the "radius" in cm converted to meters and divided by the resolutio
  set patch_radius (((item species_id move_dist_a) * (f_length ^ (item species_id move_dist_b)))) / resolution
  set patch_radius max (list patch_radius 1)

  ; Find all of the reachable cells within the radius
  set wet_cells_in_radius find_possible_destinations self patch_radius

  ; Calculate the mean water velocity in the radius
  set mean_velocity_in_radius mean [today_velocity] of wet_cells_in_radius

   ; If it is the first time step, the first value in the velocity experience list is the mean velocity of the radius
  set velocity_experience_list lput mean_velocity_in_radius velocity_experience_list

end

;; Find possible destinations the fish can swim to within the given move_dist.
; This minimizes the predation risk along a path and limits total distance.
; travelled by the provided move distance.
; This also handles stranding by having fish stuck on a dry patch use yesterday's
; water levels for valid pathing decisions. If the results are just the current
; patch, than the fish has stranded.
to-report find_possible_destinations [fish move_dist]
  ask pathfinding_dirty_patches [
    clear_patch_path_data
  ]
  let destinations table:make
  ; We start looking for valid destinations with the fish's current location.
  let to_visit (list [patch-here] of fish)
  ask [patch-here] of fish [
    set has_visited? true
    set path_to_here_cost 0
    set path_survival 1
  ]
  let dirty (list[patch-here] of fish)
  ; Check if the fish is trying to avoid stranding or not
  let avoiding_stranding [today_depth] of [patch-here] of fish <= 0
  while [length to_visit > 0] [
    ; Pull the patch we're looking at off the to_visit list.
    let cur_patch first to_visit
    set to_visit but-first to_visit
    ask cur_patch [
      ask neighbors [
        ; validate neighbor is wet
        if (today_depth > 0 or (avoiding_stranding and yesterday_depth > 0)) [
          let survival [path_survival] of cur_patch * calculate_patch_survival fish
          ; If this is the first time being visited or this path was less risky than an alternative
          if (has_visited? = false) or (path_survival < survival) [
            let move_cost [path_to_here_cost] of cur_patch + calculate_move_cost cur_patch
            if (move_cost < move_dist) [
              if (has_visited? = false) [
                set dirty lput self dirty
              ]
              store_pathfinding_patch_values cur_patch move_cost survival 0
              ; If we've moved too far, don't bother adding to the to_visit list, but
              ; if we still have distance the fish can travel than keep going.
              set to_visit lput self to_visit
              ; If we're in stranding logic we might be evaluating patches that aren't currently wet.
              ; Make sure a patch is wet before considering it a valid destination.
              ; Also chack to make sure there is area fo the fish
              ; and (pycor < [ ycor ] of fish) may add in later?
              if (is_valid_destination fish destinations) [
                ; If all checks pass (including depth and having available area), mark as a potential destination.
                table:put destinations patch_identifier self self
              ]
            ]
          ]
        ]
      ]
    ]
  ]

  let cur_patch [patch-here] of fish
  ifelse (table:length destinations = 0) [
    ; This fish has nowhere to go and is stuck, have them attempt drifting.
    ask fish [set is_drifter true]
    ; We're expected to return something, so even if we're stranding add the current patch
    table:put destinations patch_identifier cur_patch cur_patch
  ] [
    ; Make sure the current patch is an option to avoid fish shifting back and forth between adjacent patches.
    if ([is_valid_destination fish destinations] of cur_patch) [
      ask cur_patch [
        set path_survival calculate_patch_survival fish
      ]
      table:put destinations patch_identifier cur_patch cur_patch
    ]
  ]
  set pathfinding_dirty_patches patch-set dirty
  report patch-set table_to_value_list destinations
end

;; Calculate the starvation probablity
to calculate_starvation_prob

; Calculate the probability of surviving starvation based on K. This survival does not depend on the cell. It implements the linear condition mortality model.
; The equation is algebraically equivalent to a line with survival = mort-condition-S-at-K5 at K = 0.5 and survival = 1.0 at K = 1.0

  set fish_death_starv_survival_prob (evaluate_logistic "poor_condition" species fish_condition)

  end

;; Calculate the probability of a fish migrating, dependent on changes in velocity, photoperiod, and length
to calculate_outmigration_probability

  ;print "calc outmigration prob"

 ; Only evaluate probability if the individual isnt migrant
  if is_migrant = false [
    set fish_smolting_prob_photoperiod (evaluate_logistic "smolt_photoperiod" species photoperiod)

    set fish_smolting_prob_flength (evaluate_logistic "smolt_flength" species f_length)

    ;If the velocity experience list has less than 5 items, we take the average of those values
    ifelse length velocity_experience_list <= 5 [
      set running_average_velocity  mean velocity_experience_list
    ][
      ; Calculate the running average of the mean velocity that the fish has experienced in its radius the last 5 time steps
      let running_average_velocity_sublist  sublist velocity_experience_list (length velocity_experience_list - 6) (length velocity_experience_list - 1)
      set running_average_velocity mean running_average_velocity_sublist
    ]

    let percent_change_velocity 0
    ; Avoid divide by zero error. Check if running_average_velocity is 0 first, and if so, percent_change_velocity will be 0.
    if running_average_velocity != 0 [
      ; Calculate the percent change from the running average to the current radius velocity
      set percent_change_velocity ( mean_velocity_in_radius - running_average_velocity) / running_average_velocity

      ; If the change is negative (velocity decreased) then we set it to zero so the outmigration probability is 0
      if percent_change_velocity < 0 [set percent_change_velocity 0]
    ]

    ; The probability of outmigrating increases as the difference in velocity between the current radius and the running average increases.
    set fish_outmigration_prob_velocity (evaluate_logistic "outmigrate_velocity" species percent_change_velocity)

    ; Overall outmigration prob combines the probability of smolting due to photoperiod, the probability of smolting due to length, and the probability of migrating due to change in velocity

    set overall_outmigration_prob max (list fish_outmigration_prob_velocity (fish_smolting_prob_photoperiod * fish_smolting_prob_flength))

    if ((random-float 1.0) < overall_outmigration_prob) [
      set is_migrant true
      set breed migrants
      ;set daily_migrant_count count migrants
    ]
    ;set is_smolt true  ; or pseudo-smolt for sturgeon
    ;save_event "smolted"  ; saving the smolted event as with chinook, but may not want/need for sturgeon
  ]

  if is_migrant = false [table:put nonmigrants_count_table species table:get nonmigrants_count_table species + 1]

end

;; Migrate to new cell
to migrate

 ; Set max migration distance (currently 24 km) in patches
 let max_migration_distance (item species_id migration_max_dist) / resolution

 set destination find_pathable_destination_at_y self reach_end max_migration_distance

 move_fish destination

 ask destination [set migrant_patch true] ; Set the destination's to identify itself as a migrant patch (this is so we don't include these cells as destination cells for the output files)

 save_event "migrated"

 table:put migrant_count_table species table:get migrant_count_table species + 1

end

;; Move the fish
to move_fish [target]
  if draw_fish_movements? [
    ; Draw the path taken to get to the destination.
    let curpatch target
    ; The patches know the path the fish took to this location in reverse, so we
    ; actually start at the destination and draw backwards before jumping back to
    ; the end.
    move-to target
    pen-down
    while [curpatch != nobody] [
      move-to curpatch
      set curpatch [previous_patch] of curpatch
    ]
    pen-up
  ]

  ; Move to the destination.
  move-to target

end

;; Find possible a pathable destination at the specified y of length up to the move_dist.
to-report find_pathable_destination_at_y [fish y_target move_dist]
  ask pathfinding_dirty_patches [
    clear_patch_path_data
  ]
  ; We start looking for valid destinations with the fish's current location.
  let to_visit (list [patch-here] of fish)
  ask [patch-here] of fish [
    set has_visited? true
    set path_to_here_cost 0
    set path_survival 1
    set path_score 0
  ]
  let dirty (list[patch-here] of fish)
  let path_destination [patch-here] of fish
  ; Check if the fish is trying to avoid stranding or not
  let avoiding_stranding [today_depth] of [patch-here] of fish <= 0
  while [length to_visit > 0] [
    ; Pull the patch we're looking at off the to_visit list.
    let cur_patch first to_visit
    set to_visit but-first to_visit
    ask cur_patch [
      ifelse path_to_here_cost > move_dist [
        if [today_depth] of previous_patch > 0 and [cell_available_wet_area] of previous_patch >= [territory_size] of fish [
          ; We've reached the max distance we can travel. Assume we're along a good path towards the target and return
          ; the previous patch (less than the max_dist) as the destination.
          set path_destination previous_patch
          set to_visit (list)
        ]
      ][
        ifelse pycor = y_target and today_depth > 0 and cell_available_wet_area >= [territory_size] of fish [
          ; We've found our destination, clear the to visit list and save it so we can return it.
          set path_destination self
          set to_visit (list)
        ][
          ask neighbors [
            ; validate neighbor is wet
            if (today_depth > 0 or (avoiding_stranding and yesterday_depth > 0)) [
              let survival [path_survival] of cur_patch * calculate_patch_survival fish
              let move_cost [path_to_here_cost] of cur_patch + calculate_move_cost cur_patch
              let survival_score (1 - survival)
              let score (move_cost + y_diff_distance y_target) * survival_score
              ; If this is the first time being visited or this path was less risky than an alternative
              if (has_visited? = false) or (path_score > score) [
                if (has_visited? = false) [
                  set dirty lput self dirty
                ]
                store_pathfinding_patch_values cur_patch move_cost survival score
                ; If we've moved too far, don't bother adding to the to_visit list, but
                ; if we still have distance the fish can travel than keep going.
                set to_visit insert_sorted_path_score to_visit
              ]
            ]
          ]
        ]
      ]
    ]
  ]

  set pathfinding_dirty_patches patch-set dirty
  report path_destination
end

;; Determines whether fish die and of what cause
to survive

  set previous_condition fish_condition

 ; print "survive"

  if strand_status = 1 [
    ;print "died of stranding"
    table:put death_stranding_table species table:get death_stranding_table species + 1
    save_event "died of stranding"
    set is_alive false
    table:put dead_fish_count_table species table:get dead_fish_count_table species + 1
    (ifelse is_migrant = false [table:put dead_nonmigrants_count_table species table:get dead_nonmigrants_count_table species + 1]
      is_migrant = true [table:put dead_migrants_count_table species table:get dead_migrants_count_table species + 1])
      ;is_smolt = false [table:put dead_nonsmolts_count_table species table:get dead_nonsmolts_count_table species + 1])
    (ifelse is_migrant = false and daily_growth > 0 [table:put dead_rearing_count_table species table:get dead_rearing_count_table species + 1])
    die
  ]

  ifelse not empty? path_survival_list [ ; If fish has a path survival list because it's a drifter, we use the two values in the list to determine whether it dies

    ;Compare each item in the path survival list to a random number to see if the fish dies in either path
    foreach path_survival_list [n ->

      if (random-float 1.0) > n [

        ;print "died of fish predation"
        table:put death_pred_table species table:get death_pred_table species + 1
        save_event "died of predation"
        set is_alive false
        table:put dead_fish_count_table species table:get dead_fish_count_table species + 1
        (ifelse is_migrant = false [table:put dead_nonmigrants_count_table species table:get dead_nonmigrants_count_table species + 1]
          is_migrant = true [table:put dead_migrants_count_table species table:get dead_migrants_count_table species + 1])
        ;is_smolt = false [table:put dead_nonsmolts_count_table species table:get dead_nonsmolts_count_table species + 1])
        (ifelse is_migrant = false and daily_growth > 0 [table:put dead_rearing_count_table species table:get dead_rearing_count_table species + 1])
        die
      ]
    ]
  ][  ; If the fish is not a drifter, we use the regular path survival of the destination cell

    ; If the fish is eaten in its destination cell or if the survival probability of the path is less than a random number
    if (random-float 1.0) > [path_survival] of destination [
      ; Fish died of fish predation
      ;print  "died of fish predation"
      table:put death_pred_table species table:get death_pred_table species + 1
      save_event "died of predation"
      set is_alive false
      table:put dead_fish_count_table species table:get dead_fish_count_table species + 1
      (ifelse is_migrant = false [table:put dead_nonmigrants_count_table species table:get dead_nonmigrants_count_table species + 1]
        is_migrant = true [table:put dead_migrants_count_table species table:get dead_migrants_count_table species + 1])
      (ifelse is_migrant = false and daily_growth > 0 [table:put dead_rearing_count_table species table:get dead_rearing_count_table species + 1])
      die
    ]
  ]

  if (random-float 1.0) < ([fish_death_hightemp_prob] of destination) [
    ; Fish died of high temperature
    ;print "died of high temperature"
    table:put death_temp_table species table:get death_temp_table species + 1
    save_event "died of high temp"
    set is_alive false
    table:put dead_fish_count_table species table:get dead_fish_count_table species + 1
    (ifelse is_migrant = false [table:put dead_nonmigrants_count_table species table:get dead_nonmigrants_count_table species + 1]
      is_migrant = true [table:put dead_migrants_count_table species table:get dead_migrants_count_table species + 1])
    (ifelse is_migrant = false and daily_growth > 0 [table:put dead_rearing_count_table species table:get dead_rearing_count_table species + 1])
    die
  ]

  if (random-float 1.0) > (fish_death_starv_survival_prob) [
    ; Fish died of poor condition
    ;print "died of poor condition"
    table:put death_condition_table species table:get death_condition_table species + 1
    save_event "died of poor condition"
    set is_alive false
    table:put dead_fish_count_table species table:get dead_fish_count_table species + 1
    (ifelse is_migrant = false [table:put dead_nonmigrants_count_table species table:get dead_nonmigrants_count_table species + 1]
      is_migrant = true [table:put dead_migrants_count_table species table:get dead_migrants_count_table species + 1])
    (ifelse is_migrant = false and daily_growth > 0 [table:put dead_rearing_count_table species table:get dead_rearing_count_table species + 1])
    die
  ]

  if is_migrant = true and ycor = reach_end [
    save_event "migrant exited river"
    die
  ]

end

;; Calculates the energy benefits of each cell in the search radius
to calculate_energy_balance

  ask wet_cells_in_radius  [

    let fish_species [species] of myself
    let my_species_id [species_id] of myself

    ; Calculate the swim speed (m/s) of the fish in each cell if it were to drift feed (dependent on whether there are velocity shelters)
    ; Set swimming velocity
    set swim_speed (set_swim_speed item my_species_id benthic_fish cell_available_vel_shelter [territory_size] of myself today_velocity)

    ; Choose between benthic and and drift feeding
    ifelse (item my_species_id benthic_fish) = 0 [
      ; Calculate the capture area of the fish
      set capture_area (2 * fish_detect_dist) * min (list fish_detect_dist today_depth) ; m^2

      ; Set up logistic equation to determine capture success
      set ratio_vel_max_swim today_velocity / [max_swim_speed] of myself
      set capture_success (evaluate_logistic "capture_success" fish_species ratio_vel_max_swim)

      ; Calculate daily intake as a daily rate, g/d
      set daily_intake capture_area * hab_drift_con * today_velocity * capture_success * 3600 * photoperiod
    ][
      ; Calculate the fish width assuming it has a density of water
      let f_width sqrt([mass] of myself / [f_length] of myself)
      let n_steps (item my_species_id feeding_speed) * [f_length] of myself / f_width * (3600 * (24 - photoperiod))
      set daily_intake pi * n_steps * f_width ^ 2 / ln(n_steps) / 1e4 *  hab_ben_con
    ]

    set active_metab_rate (calculate_metabolic temperature [mass] of myself my_species_id swim_speed)
    set passive_metab_rate (calculate_metabolic temperature [mass] of myself my_species_id 0)

    ifelse (item my_species_id benthic_fish) = 0 [
      set total_metab_rate (active_metab_rate * (photoperiod) + passive_metab_rate * (24 - photoperiod)) / 24
    ][
      set total_metab_rate (active_metab_rate * (24 - photoperiod) + passive_metab_rate * (photoperiod)) / 24
    ]

    ; Use cmax to limit intake
    if daily_intake > [cmax] of myself [set daily_intake [cmax] of myself]

    ifelse (item my_species_id benthic_fish) = 0 [
      ; Calculate energy obtained each cell (J/d)
      set daily_energy_intake daily_intake * hab_drift_ene
    ][
      ; limit based on avaiable food
      if daily_intake > cell_available_ben [ set daily_intake cell_available_ben ]
      ; Calculate energy obtained each cell (J/d)
      set daily_energy_intake daily_intake * hab_ben_ene
    ]

    ; Calculate net energy intake by subtracting the metabolic rate (J/d)
    set daily_net_energy daily_energy_intake - total_metab_rate

    set total_net_energy_in_cell precision (daily_net_energy) 2 ; Value can be negative since daily net energy can be negative

  ]

end

;; Calculate the swim speed accounting for benthic effects or shelter
to-report set_swim_speed [#benthic_flag #shelter #territory #velocity]
  ifelse (#benthic_flag) = 0 [
      ifelse (#shelter) > (#territory) [ ; If there are velocity shelters in its cell, the speed is reduced
        report #velocity *  shelter_frac  ; Swim speed is in m/s
      ][
        ; Otherwise, the speed is the velocity of the cell
        report #velocity ; Swim speed is in m/s
      ]
    ][
      ; The fish is benthic so experiences a reduced velocity
      ; 0.07 is a constant representing between 5 and 10%
      ; 0.41 is Von Karman constant
      ; 30 and 3.5 are also fitted constants
      report (0.07 * #velocity / 0.41 * ln (ben_vel_height / d84_size * 30 / 3.5))
    ]
end

;; Calculate the metabolic rate
to-report calculate_metabolic [#temperature #mass #specise_id #swim_speed]
  let log_total_metab_rate item #specise_id met_int +
    item #specise_id met_lm * ln #mass +
    item #specise_id met_lt * ln #temperature +
    item #specise_id met_v * #swim_speed +
    item #specise_id met_lm_lt * ln #mass * ln #temperature +
    item #specise_id met_t * #temperature +
    item #specise_id met_lm_t * ln #mass * #temperature +
    item #specise_id met_sqv * sqrt(#swim_speed)

  report exp log_total_metab_rate
end

;; Calculates the mortality risk of each cell in the search radius (previously, was set to all non-starvation risks multiplied)
to calculate_mortality_risk

  ask wet_cells_in_radius [

    let fish_species [species] of myself

    ; Calculate the probability of death from high temp (the logistic calculates probability of surviving the risk, so we subtract from 1)
    set fish_death_hightemp_prob (evaluate_logistic "high_temperature" fish_species temperature)
    set fish_death_hightemp_prob 1 - fish_death_hightemp_prob

    ; Calculate the probability of dying from predation
    ifelse [f_length] of myself > (item [species_id] of myself small_cover_length) [
      set fish_death_aq_pred_prob calc_pred_mortality survival_prob encounter_prob max_prey_length ([f_length] of myself) num_preds
    ][
      set fish_death_aq_pred_prob calc_pred_mortality small_survival_prob encounter_prob max_prey_length ([f_length] of myself) num_preds
    ]
  ]

end

;; Cell selection strategy for movement
to select_destination_cell

   ifelse exit_status = 1 [ ; If the drifter is going to exit the system (due to there not being valid destination cells downstream of its position, or no cell with positive net energy), it selects one of the furthest cell downstream

    move_fish destination  ; Destination should be set to the fallback migration patch

    let destination_patch_path_survival fallback_migration_patch_path_survival

    ask destination [ set path_survival destination_patch_path_survival]

    if is_drifter = true and ycor = reach_end [set drifter_history "no valid destinations or cells with pos net energy, drifted out of river"]
    if is_drifter = true and ycor != reach_end [set drifter_history "no valid destinations or cells with pos net energy, did not reach end"]

    table:put drifter_count_table species table:get drifter_count_table species + 1

  ][

  ; Each fish performs this in order of longest length to shortest length
  ifelse (random-float 1.0) > fish_death_starv_survival_prob [ ; If the probability of surviving starvation is less than the randomly generated number, the fish selects cells with higher positive net energy regardless of risk

   set starving? true
   ; print "starving fish, select food"

   if (all? wet_cells_in_radius [total_net_energy_in_cell <= 0] and is_drifter = false) or (all? wet_cells_in_radius [total_net_energy_in_cell <= 0] and is_drifter = true) [  ; if all of the cells in the radius have negative net energy values, the fish moves elsewhere in the reach to get out of crappy area
      ;print "turned to drifter, no dests available"
      set is_drifter true
      set drifter_history "drifting, no dests available"
      table:put drifter_count_table species table:get drifter_count_table species + 1 ]

  if any? wet_cells_in_radius with [total_net_energy_in_cell > 0] and is_drifter = false [
      ;print "was not drifting, found dest"
      set drifter_history "was not drifting, found dest"
      set destination max-one-of wet_cells_in_radius [total_net_energy_in_cell] ; If they do not become drifters, they select cell with higher net energy regardless of risk
        move_fish destination]

  if any? wet_cells_in_radius with [total_net_energy_in_cell > 0] and is_drifter = true [ ; if ANY of the cells in the radius have positive net energy values, the fish select cell with higher net energy regardless of risk
      ;print "was drifting, found dest"
      set drifter_history "was drifting, found dest"
      set destination max-one-of wet_cells_in_radius [total_net_energy_in_cell]
      move_fish destination
      set is_drifter false] ; If they found a destination, turned drifter off

    ][ ; If the probability of surviving starvation is greater than the randomly generated number, the fish selects cells that maximize net energy to nonstarvation risks ratio

      set starving? false
      ; print "not starving, consider risks"

      if (all? wet_cells_in_radius [total_net_energy_in_cell <= 0] and is_drifter = false) or (any? wet_cells_in_radius with [total_net_energy_in_cell > 0] and is_drifter = false) [
        ;print "was not drifting, found dest"
        ask wet_cells_in_radius [
          ;Fish takes into account the net energy-risk ratio AND actual path risk (prob of surviving along the path) in selecting a destination:
          set consider_path_risk  total_net_energy_in_cell * path_survival
        ]
        set destination max-one-of wet_cells_in_radius [consider_path_risk]
        set drifter_history "was not drifting, found dest"
        move_fish destination
      ]

      if (all? wet_cells_in_radius [total_net_energy_in_cell <= 0] and is_drifter = true) or (any? wet_cells_in_radius with [total_net_energy_in_cell > 0] and is_drifter = true) [
        ;print "was drifting, found dest"
        ask wet_cells_in_radius [
          ;Fish takes into account the net energy-risk ratio AND actual path risk (prob of surviving along the path) in selecting a destination:
          set consider_path_risk  total_net_energy_in_cell * path_survival
        ]
        set destination max-one-of wet_cells_in_radius [consider_path_risk]
        set drifter_history "was drifting, found dest"
        move_fish destination
        set is_drifter false
      ]
    ]
  ]

  ; If there is already a value in their path_survival_list, we add the second value to it
  if not empty? path_survival_list [set path_survival_list lput ([path_survival] of destination) path_survival_list]

  ask destination [set migrant_patch false]  ; The destination cell's migrant_patch status is set to false

end

;; Find all possible drift destinations for the fish. Anything reachable by today's depth
; (or yesterday's depth if avoiding stranding) and downstream are considered valid
; destinations (within the move_dist).
; This calculates predation risk, but doesn't try to minimize it.
to-report find_possible_drift_destinations [fish max_dist]
  ask pathfinding_dirty_patches [
    clear_patch_path_data
  ]
  let destinations table:make
  ; We start looking for valid destinations with the fish's current location.
  let to_visit (list [patch-here] of fish)
  ask [patch-here] of fish [
    set has_visited? true
    set path_to_here_cost 0
    set path_survival 1
  ]
  let dirty (list[patch-here] of fish)
  ; Check if the fish is trying to avoid stranding or not
  let avoiding_stranding [today_depth] of [patch-here] of fish <= 0
  let reached_end false
  set fallback_migration_patch [patch-here] of fish
  while [length to_visit > 0] [
    ; Pull the patch we're looking at off the to_visit list.
    let cur_patch first to_visit
    set to_visit but-first to_visit
    ask cur_patch [
      ask neighbors [
        ; validate neighbor is wet
        if (today_depth > 0 or (avoiding_stranding and yesterday_depth > 0)) [
          let move_cost [path_to_here_cost] of cur_patch + calculate_move_cost cur_patch
          ; If this is the first time being visited or this path was less risky than an alternative
          if (has_visited? = false) or (path_to_here_cost > move_cost) [
            if (has_visited? = false) [
              set dirty lput self dirty
            ]
            let survival [path_survival] of cur_patch * calculate_patch_survival fish
            store_pathfinding_patch_values cur_patch move_cost survival 0
            ; If we've moved too far, don't bother adding to the to_visit list, but
            ; if we still have distance the fish can travel than keep going.
            set to_visit lput self to_visit
            if pycor = reach_end [
              set reached_end true
            ]
            ; If we're in stranding logic we might be evaluating patches that aren't currently wet.
            ; Make sure a patch is wet before considering it a valid destination.
            ; Also chack to make sure there is area fo the fish
            if pycor < [ ycor ] of fish and ((pycor = reach_end and today_depth > 0) or is_valid_destination fish destinations) [
              ; If all checks pass (including depth and having available area), mark as a potential destination.
              table:put destinations patch_identifier self self
              if (pycor < [pycor] of [fallback_migration_patch] of fish) and move_cost < max_dist [
                let current_patch self
                ask fish [
                  set fallback_migration_patch current_patch
                ]
              ]
            ]
          ]
        ]
      ]
    ]
  ]

  set fallback_migration_patch_path_survival [path_survival] of fallback_migration_patch

  if (table:length destinations = 0) [
    ifelse reached_end [
      ; Fish drifted out of river
      ask fish [set exit_status 1]
    ][
      ifelse avoiding_stranding [
        ; This fish has nowhere to go and is stuck. They are stranded.
        ask fish [set strand_status 1]
      ][]
    ]
    let cur_patch [patch-here] of fish
    ; We're expected to return something, so even if we're stranding add the current patch
    table:put destinations patch_identifier cur_patch cur_patch
  ]
  set pathfinding_dirty_patches patch-set dirty
  report patch-set table_to_value_list destinations
end

;; Procedure for drifters drifting downstream
to drift_downstream

  ; Temporarily set the drifter's color to blue
  set color blue

  ; Set the distance a fish can disperse to be equal to 10 times the current radius (currently same as migration distance)
  set dispersal_distance item species_id migration_max_dist / resolution

  ; Find all of the wet cells within the new area that the fish can disperse to
  set open_cells_for_dispersal find_possible_drift_destinations self dispersal_distance

  set all_downstream_cells open_cells_for_dispersal with [pycor < [ ycor ] of myself ]

  ; Determine the number of random cells that the fish can evaluate for drifting
  let num_random_cells (([pycor] of self - reach_end) / dispersal_distance) * 100

  ; Select random "num_random_cells" number of cells downstream, or whatever amount there is
  ifelse count all_downstream_cells >= num_random_cells [
  set random_drift_downstream_cells n-of num_random_cells all_downstream_cells
  ][
    ; There are less cells than the number want, so just take them all.
    set random_drift_downstream_cells all_downstream_cells
   ]

  ; If there are no valid cells that the fish can drift to, it drifts out of the river or strands
  if any? random_drift_downstream_cells = FALSE [
    print "no random drift downstream cells"
    ; This formerly marked fish as stranded, but that's now handled in the drift function.

    let max_migration_distance (item species_id migration_max_dist) / resolution

    ; If there is no downstream cell to move to, the drifter exits out of the river
    set destination fallback_migration_patch

    set exit_status 1
  ]

end

;; Calculate the net energy in a drift cell
to calculate_net_energy_of_drift_cells

  ; Find the distance between these random cells and the fish
  ask random_drift_downstream_cells [set distance_to_drifter distance myself]

  ; Sort the random patches by the distance to the fish
  set sorted_distance_cells sort-on [distance_to_drifter] random_drift_downstream_cells

  ; can we take this out and use self below?
  let current_fish self

  set closest_cell_with_pos_energy nobody

  set no_cell_has_pos_energy FALSE

  while [closest_cell_with_pos_energy = nobody and no_cell_has_pos_energy = FALSE] [
    set positive_energy_cell_count 0
    let n_index 0

    ; Feed in the random cells (in ascending order):
    foreach sorted_distance_cells [n ->

    while [positive_energy_cell_count = 0 and no_cell_has_pos_energy = FALSE] [
        ;While there are no positive net energy cells in radius and we haven't reached the end of the list, keep going
        ask n [
          ; For each of the random cells, find the patches in the radius
          ;set possible_wet_cells_in_radius patches in-radius ([patch_radius] of myself)
          set all_net_energy []
          ask current_fish [
            move-to n
            ;set wet_cells_in_radius possible_wet_cells_in_radius
            set wet_cells_in_radius find_possible_destinations self patch_radius
            calculate_energy_balance
            set all_net_energy max [total_net_energy_in_cell] of wet_cells_in_radius
          ]

          ifelse all_net_energy > 0 [
            ; If there is a radius cell with positive net intake, we can exit the loop
            set positive_energy_cell_count 1
            ; If any of the element in the list is positive, we have found a cell with positive net energy
            set closest_cell_with_pos_energy n
          ][
            set positive_energy_cell_count 0
            set closest_cell_with_pos_energy nobody
            ifelse length sorted_distance_cells = n_index + 1 [
              ; If we have reached the end of the random drift cells
              set no_cell_has_pos_energy TRUE
            ][
              set n item (n_index + 1) sorted_distance_cells
              set n_index n_index + 1
            ]
          ]
        ]
      ]
    ]
  ]

  ifelse closest_cell_with_pos_energy = nobody [
    ; If there are no cells with positive net energy, the drifter exits out of the river

    ; Set max migration distance in patches
    ;let max_migration_distance (item species_id migration_max_dist) / resolution
    set destination fallback_migration_patch
    set exit_status 1
  ][
    ; Fish moves to closest drift cell
    move-to closest_cell_with_pos_energy

    ; Reset path survival list for the drifters who move to two cells (this store the path survivals of the two paths)
    set path_survival_list []

    ;For the drifter fish, store the path survival probabilities
    set path_survival_list lput [path_survival] of closest_cell_with_pos_energy path_survival_list

    ;Wet cells in radius become the valid patches in the radius of the closest cell
    ;set wet_cells_in_radius find_possible_destinations self patch_radius

    ; Calculate the mean water velocity in the radius
    set mean_velocity_in_radius mean [today_velocity] of wet_cells_in_radius

    set velocity_experience_list lput mean_velocity_in_radius velocity_experience_list
  ]

end

;; Remove resources form cells
to deplete_destination_resources

; Deplete the food resources and the shelter resources in the desination cell

  if (item species_id benthic_fish) = 0 [  ; for some reason, I can't set is_in_shelter to true within the code block above, so I have it here for now
      if (cell_available_vel_shelter) >= (territory_size) [
      set is_in_shelter true ]
  ]

  ask destination [
    ; If there are velocity shelters for the fish to use, and it's not benthic we remove the shelter from available shelter
    ifelse (item [species_id] of myself benthic_fish) = 0 [
      if (cell_available_vel_shelter) >= ([territory_size] of myself) [
        set cell_available_vel_shelter cell_available_vel_shelter - ([territory_size] of myself * superind_ratio)
      ]
      if (cell_available_wet_area) >= ([territory_size] of myself) [
        set cell_available_wet_area cell_available_wet_area - ([territory_size] of myself * superind_ratio)
      ]
    ][
      if (cell_available_ben) >= (daily_intake) [
        set cell_available_ben max list (cell_available_ben - daily_intake * superind_ratio) 0
      ]
    ]
  ]
end

;; Update the fish size
to grow

  set previous_condition fish_condition

  set daily_growth ([daily_net_energy] of destination) / item species_id energy_density

  ifelse daily_growth = 0.0 [ ; if daily growth is 0, set the percent daily growth to a very small number to avoid div by 0 error
    ; This is the daily growth in percent body weight (column in output file)
    set percent_daily_growth 0
  ][
    ; This is the daily growth in percent body weight (column in output file)
    set percent_daily_growth (daily_growth / mass) * 100
  ]

  ; Calculate the fish's new weight
  set new_mass mass + daily_growth

  ; If the fish's mass is 0, the condition is 0
  if new_mass <= 0.0 [
    set new_condition 0
    set new_mass 0.0
  ]

  set healthy_mass (item species_id length_mass_a) * (f_length ^ (item species_id length_mass_b)) ; g
  ;print "healthy mass"
  ;show healthy_mass

  set desired_length (new_mass / (item species_id length_mass_a)) ^ (1 / (item species_id length_mass_b)) ; cm
  ;print "desired length"
  ;show desired_length

  ; If the new mass is greater than the healthy mass for its length, we set the new length to the desired length and new condition to 1
  ifelse new_mass > healthy_mass [
   set new_length desired_length
   set new_condition 1.0
  ][ ; Otherwise, we divide the new mass by the healthy mass to get the new fish condition
   set new_length f_length ; The fish keeps its current length (cm)
   set new_condition new_mass / healthy_mass
  ]

  set start_mass mass
  set mass new_mass
  set start_length f_length
  set change_length new_length - f_length
  set f_length new_length
  set fish_condition new_condition

  ; set territory size (if benthif fish size is f_lenght^2)
  ifelse item species_id benthic_fish = 0 [
    set territory_size (item species_id territory_a) * f_length ^ (item species_id territory_b)
  ][
    set territory_size (f_length ^ 2) / 1e4
  ]

    if is_alive = true [
    ifelse is_migrant = true [
      save_event "alive_migrant" ][
      ifelse is_drifter = true [
        save_event "drifter_alive"][
        save_event "alive"]
       ask destination [
        set count_fish_destination count turtles-here
        set avg_weight_fish_in_destination mean [mass] of turtles-here
        set avg_length_fish_in_destination mean [f_length] of turtles-here
        set avg_condition_fish_in_destination mean [fish_condition] of turtles-here
      ]
    ]
  ]

  ; If the drifter has reached the end of the reach and hasn't died, it is removed from the system but doesnt get added to the dead count
  if exit_status = 1 and ycor = reach_end [die]

;    print "###########################################"
;
;    show word "start length" start_length
;    show word "length" f_length
;    show word "start mass" start_mass
;    show word "mass" mass
;    show word "cmax" cmax
;    show word "cmax temp func" cmax_temp_func
;    show word "cmax wt term" fish_cmax_wt_term
;    show word "photoperiod" photoperiod
;    show word "velocity" [today_velocity] of destination
;    show word "swim speed" [swim_speed] of destination
;    show word "depth" [today_depth] of destination
;    show word "turbidity" [turbidity] of destination
;    show word "temperature" temperature
;    show word "active metab" active_metab_rate
;    show word "passive metab" passive_metab_rate
;    show word "daily intake" [daily_intake] of destination
;    show word "daily energy intake" [daily_energy_intake] of destination
;    show word "net energy intake" [daily_net_energy] of destination
;
;    print "###########################################"

end

;##### Fish Pathfinding Functions ##########################################
; Clear all of the values used in the pathfinding algorithm
to clear_patch_path_data
  set has_visited? false
  set previous_patch nobody
  set path_to_here_cost -1
  set path_survival -1
  set fish_survival -1
  set path_score -1
end

;; Calculate the cost to move to a new patch.
to-report calculate_move_cost [from_patch]
  ; assume the cost == the distance
  ; calculate distance instead of using 1 to account for diagonals
  ; todo - is this how cost should be calculated? maybe energy expenditure estimate?
  report distance from_patch
end

;; Calcuate mortality form predators
to-report calc_pred_mortality [#survival_prob #encounter_prob #max_prey_length #prey_f_length #num_preds]

  ; mortality is 0 if fork length is too big for predators
  ; f_length is in cm but the model that calcs max_prey_length uses mm
  if #max_prey_length < (#prey_f_length) [
    report 0
  ]

  ifelse #encounter_prob <= 1 [
    ; this will be the output in most cases with relatively low predator density
    report #encounter_prob * (1 - #survival_prob)
  ][
    ; allow for multiple encounters in patches with encounter_prob > 1
    ; find the most appropriate value to act as an encounter rate
    ; prevents absurdly high numbers from being used
    let new_enc_num (min (list (#encounter_prob) (sum #num_preds)))
    ; integer value of the new enc number determines how many encounters a prey fish is guaranteed to have in high enc prob patches
    let guaranteed_num_encounters floor new_enc_num
    ; any leftover decimal-point value can be used to factor in an additional potential encounter with prob of occurring equal to the decimal value
    let potential_extra_encounter new_enc_num - guaranteed_num_encounters

    report 1 - (#survival_prob ^ (guaranteed_num_encounters + 1) * potential_extra_encounter + (1 - potential_extra_encounter) * #survival_prob ^ guaranteed_num_encounters)
  ]
end

;; Calcuate the survival chances of this patch. Used to determine what patches are options
to-report calculate_patch_survival [fish]
  if (fish_survival = -1) [
    ifelse [f_length] of fish > (item [species_id] of fish small_cover_length) [
      set fish_survival 1 - (calc_pred_mortality survival_prob encounter_prob max_prey_length [f_length] of fish num_preds)
    ][
      set fish_survival 1 - (calc_pred_mortality small_survival_prob encounter_prob max_prey_length [f_length] of fish num_preds)
    ]
  ]
  report fish_survival
end

;; Store values relevant for the pathfinding. Use the from_patch and the provided cost
; to calculate values for myself.
to store_pathfinding_patch_values [from_patch cost survival score]
  ; Set the path data for this patch (costs, previous patch, visited)
  set previous_patch from_patch
  set path_to_here_cost cost
  set has_visited? true
  set path_survival survival
  set path_score score
end

;; Gives the patch an identifier based on it lat and long
to-report patch_identifier [loc]
  report (word [pxcor] of loc " " [pycor] of loc)
end

;; Makes checks on depth velocity and conncetion to see if the cell is valid for path finding
to-report is_valid_destination [fish destinations]
  let possible_swim_speed (set_swim_speed (item [species_id] of fish benthic_fish) cell_available_vel_shelter ([territory_size] of fish) today_velocity)
  report (today_depth > 0  and (possible_swim_speed < [max_swim_speed] of fish) and (not table:has-key? destinations patch_identifier self) and cell_available_wet_area >= [territory_size] of fish)
end

;; Makes a lookup tabel for pathfinding cells
to-report table_to_value_list [my_table]
  let keys table:keys my_table
  let values (list)
  foreach keys [ [value] -> set values lput table:get my_table value values ]
  report values
end

to-report binary_search_insert_index_path_score [my_list]
  let L 0
  let R length my_list - 1
  let m 0
  while [L <= R] [
    set m floor((L + R) / 2)
    let score_middle [path_score] of item m my_list
    ifelse score_middle < path_score [
      set L m + 1
    ][
      ifelse score_middle > path_score [
        set R m - 1
      ][
        report m + 1
      ]
    ]
  ]
  ifelse m > 0 [
    report m + 1
  ][
    report 0
  ]
end

to-report insert_sorted_path_score [my_list]
  ; binary search to find location to insert
  let index binary_search_insert_index_path_score my_list
  ; insert value into list and return
  report insert-item index my_list self
end

to-report y_diff_distance [y_target]
  let y_diff pycor - y_target
  ifelse y_diff >= 0[
    report y_diff
  ][
    report (- y_diff)
  ]
end

;##### Make Output Files #######################################################
;; Saves the information of each destination cell every timestep (for cell_info_list csv)
to save_destination_cell_info

  set destination_cells [self] of patches with [ any? turtles-here and migrant_patch = false ]

  foreach destination_cells [[next_cell] ->

    set cell_info_list lput (
      csv:to-row ( list
        time:show tick_date "yyyy-MM-dd"
        next_cell
        [x_pos] of next_cell
        [y_pos] of next_cell
        ([count_fish_destination] of next_cell * superind_ratio)
        [avg_weight_fish_in_destination] of next_cell
        [avg_length_fish_in_destination] of next_cell
        [avg_condition_fish_in_destination] of next_cell
        [today_velocity] of next_cell
        [today_depth] of next_cell
        [total_net_energy_in_cell] of next_cell
        [total_mort_risk_for_cell] of next_cell
        [fish_death_aq_pred_prob] of next_cell
      )
    )
    cell_info_list

  ]

end

; a turtle (migrant) procedure saving information about the path it takes to migrate out of the river
to save_migrant_path_info [migrant_path]

 set migrant_path_info_list lput ( csv:to-row (list
    time:show tick_date "yyyy-MM-dd"
    who
    f_length
    pathfinding_list_x
    pathfinding_list_y
    path_survival
    wetted_area
    today_velocity
    today_depth
    num_preds
    cover_bonus
    encounter_prob
    survival_prob
        )) migrant_path_info_list
end

;; A turtle procedure to save events for the fish output files (events include mortality, initialization, smolting etc)
to save_event [an_event_type]

  ; an-event-type is a character string that says what event happened.
  if breed = juveniles or breed = migrants [
    set fish_events_list lput (
      csv:to-row ( list
        time:show tick_date "yyyy-MM-dd"
        species
        who
        [x_pos] of destination
        [y_pos] of destination
        start_length
        f_length
        change_length
        start_mass
        mass
        previous_condition
        fish_condition
        daily_growth
        percent_daily_growth
        max_swim_speed
        cmax
        [swim_speed] of destination
        ;fish_smolting_prob_photoperiod
        overall_outmigration_prob
        [cell_available_wet_area] of destination
        is_in_shelter
        [encounter_prob] of destination
        is_drifter
        drifter_history
        is_migrant
        starving?
        an_event_type
        temperature
        flow
        turbidity
        photoperiod
        [today_velocity] of destination
        [today_depth] of destination
        [distance_to_cover] of destination
        [cell_available_vel_shelter] of destination
        [passive_metab_rate] of destination
        [active_metab_rate] of destination
        [total_metab_rate] of destination
        [daily_intake] of destination
        [daily_energy_intake] of destination
        [total_net_energy_in_cell] of destination
        [path_survival] of destination
        [fish_death_aq_pred_prob] of destination
      )
    )
    fish_events_list
  ]

end

;; Saves detailed summary info of the population every timestep ( total number fish migrating, total number dead fish etc)
to save_detailed_population_info

  foreach species_list [ next_species ->
    let current_set juveniles with [species = next_species]
    ;set total_daily_juveniles count juveniles ; the number of non-smolt and smolt individuals in the river that day
    set total_daily_juveniles count current_set ; the number of non-smolt and smolt individuals in the river that day (does not include migrants)(cumulative)
    let rearing_juveniles count current_set with [daily_growth > 0 ]
    set total_daily_migrants table:get migrant_count_table next_species ; the number of individuals that turned into migrants that day or are currently migrating
    ;set total_daily_smolts table:get smolt_count_table next_species    ; the number of individuals that turned into smolts that day
    set total_daily_nonmigrants table:get nonmigrants_count_table next_species  ; the number of individuals that are nonmigrants at the beginning of that day (cumulative)
    let mean_length 0
    let mean_energy 0
    if  any? current_set = true [
      set mean_length mean [f_length] of current_set
      set mean_energy mean [daily_net_energy] of current_set
    ]
    let rearing_growth_fra 0
    let rearing_growth_length 0
    if any? current_set with [daily_growth > 0 ] [
      set rearing_growth_fra mean [daily_growth / mass ] of current_set with [daily_growth > 0 ]
      set rearing_growth_length mean [change_length] of current_set with [daily_growth > 0 ]
    ]

    ;  set mean_migrant_mass mean migrant_mass_list
    ;  set mean_migrant_condition mean migrant_condition_list
    ;
    ;  set mean_smolt_length mean smolt_length_list
    ;  set mean_smolt_mass mean smolt_mass_list
    ;  set mean_smolt_condition mean smolt_condition_list
    ;
    ;  set mean_nonsmolt_length mean nonsmolt_length_list
    ;  set mean_nonsmolt_mass mean nonsmolt_mass_list
    ;  set mean_nonsmolt_condition mean nonsmolt_condition_list

    set total_daily_dead_fish table:get dead_fish_count_table next_species ; the number of individuals (smolts and nonsmolts) that have died that day
    set total_daily_dead_migrants table:get dead_migrants_count_table next_species ; the number of migrants that have died that day
    ;set total_daily_dead_smolts table:get dead_smolts_count_table next_species ; the number of smolts that have died that day
    let total_daily_dead_rearers table:get dead_rearing_count_table next_species ; the number of smolts that have died that day
    set total_daily_dead_nonmigrants table:get dead_nonmigrants_count_table next_species ; the number of nonsmolts that have died that day
    set total_daily_drifters table:get drifter_count_table next_species  ; the number of individuals that turned into drifters that day (can be smolts or nonsmolts)
    let count_death_predation table:get death_pred_table next_species
    let count_death_hightemp table:get death_temp_table next_species
    let count_death_stranding table:get death_stranding_table next_species
    let count_death_poorcond table:get death_condition_table next_species

    set detailed_population_list lput (
      csv:to-row (list
        time:show tick_date "yyyy-MM-dd"
        next_species
        (total_daily_juveniles * superind_ratio)   ;this includes smolts
        (rearing_juveniles * superind_ratio)
        mean_length
        mean_energy
        rearing_growth_fra
        rearing_growth_length
        (total_daily_migrants * superind_ratio)
        ;      mean_migrant_length
        ;      mean_migrant_mass
        ;      mean_migrant_condition
        ;(total_daily_smolts * superind_ratio)
        ;      mean_smolt_length
        ;      mean_smolt_mass
        ;      mean_smolt_condition
        (total_daily_nonmigrants * superind_ratio)
        ;      mean_nonsmolt_length
        ;      mean_nonsmolt_mass
        ;      mean_nonsmolt_condition
        (total_daily_drifters * superind_ratio)
        (total_daily_dead_fish * superind_ratio)
        (total_daily_dead_migrants * superind_ratio)
        ;(total_daily_dead_smolts * superind_ratio)
        (total_daily_dead_nonmigrants * superind_ratio)
        (total_daily_dead_rearers * superind_ratio)
        (count_death_predation * superind_ratio)
        (count_death_hightemp * superind_ratio)
        (count_death_stranding * superind_ratio)
        (count_death_poorcond * superind_ratio)
        temperature
        flow
        photoperiod
      )
    )
    detailed_population_list
  ]

end

;; Saves basic info about all cell
to save_all_cell_info

  set all_cells [self] of patches with [ wetted_fraction > 0 ]

  foreach all_cells [[next_cell] ->

  set all_cell_attributes_list lput (
      csv:to-row (list
        time:show tick_date "yyyy-MM-dd"
        next_cell
        [x_pos] of next_cell
        [y_pos] of next_cell
        [today_velocity] of next_cell
        [today_depth] of next_cell
        [wetted_fraction] of next_cell
        [encounter_prob] of next_cell
      )
    )
    all_cell_attributes_list

  ]

end

;; An observer procedure to initialize an output file.
to build_output_file_named [a_file_name]

  ; The parameter a_file_name is the global variable for the file name.

  ;; Create the detailed population output file.
  if a_file_name = "d-p-o-n" [ ; This is the value of the uninitialized file name
    set detailed_population_outfile_name (word run_folder "/detailed_pop_output.csv")
    if file-exists? detailed_population_outfile_name [ file-delete detailed_population_outfile_name ]
    ; These header lines must be put at the *start* of the list. Use fput with header
    ; lines in reverse order.
    set detailed_population_list fput "time, Species, juveniles, rearers, mean_length, mean_energy, mean_rearing_mass_growth_fra, mean_rearing_growth_length, migrants, nonmigrants, drifters, dead_fish, dead_migrants, dead_nonmigrants, dead_rearers, predation_deaths, high_t_deaths, stranding_deaths, poor_condition_deaths, temperature, flow, photoperiod" detailed_population_list
    set detailed_population_list fput (word "FHAST detailed population output file, Created " date-and-time) detailed_population_list
  ]
  ;; Create the destination cell info output file.
  if a_file_name = "c-i-o-n" [ ; This is the value of the uninitialized file name
    set cell_info_outfile_name (word run_folder "/cell_info_output.csv")
    if file-exists? cell_info_outfile_name [ file-delete cell_info_outfile_name ]
    ; These header lines must be put at the *start* of the list. Use fput with header
    ; lines in reverse order.
    set cell_info_list fput "time, cell, x_pos, y_pos, fish_count, mean_fish_mass, mean_fish_length, mean_fish_condition, velocity, depth, food, survival_prob, prob_of_predation" cell_info_list
    set cell_info_list fput (word "FHAST destination cell info output file, Created " date-and-time) cell_info_list
  ]

  ; Create the fish events output file.
  if a_file_name = "f-e-o-n" [ ; This is the value of the uninitialized file name
    set fish_events_outfile_name (word run_folder "/events_output.csv")
    if file-exists? fish_events_outfile_name [ file-delete fish_events_outfile_name ]
    ; There can be events on the fish-events-list when file is created (from fish initialization)
    ; so these header lines must be put at the *start* of the list. Use fput with header
    ; lines in reverse order.
    set fish_events_list fput "time, Species, id, x_pos, y_pos, start length , length, length change, start mass, mass, previous_condition, condition, growth, percent_daily_growth, max_swim_speed, cmax, swim_speed, overall_outmigration_prob, cell_available_wet_area, in_shelter, encounter_prob, fis_drifter, drifter_history, is_migrant, starving?, event, temperature, flow, turbidity, photoperiod, velocity, depth, distance_to_cover, available_velocity_shelter, capture_area, capture_success, fish_turbid_function, fish_detect_distance, passive_metab_rate, active_metab_rate, total_metab_rate, daily_intake, daily_energy_intake, total_net_energy, path_survival, prob_of_surviving_predation_of_destination" fish_events_list
    set fish_events_list fput (word "FHAST fish events output file, Created " date-and-time) fish_events_list
  ]

  ; Create output file for recording attributes of all cells in the model (for mapping and testing purposes)
  if a_file_name = "a-c-o-n"  [ ; This is the value of the uninitialized file name
     set all_cell_outfile_name (word run_folder "/all_cell_output.csv")
     if file-exists? all_cell_outfile_name [ file-delete all_cell_outfile_name ]
     ; These header lines must be put at the *start* of the list. Use fput with header
    ; lines in reverse order.
    set all_cell_attributes_list fput "time, cell_id, x_pos, y_pos, velocity, depth, wetted_fraction, encounter_prob, velocity, depth, cover_bonus" all_cell_attributes_list
    set all_cell_attributes_list fput (word "FHAST all cell output file, Created " date-and-time) all_cell_attributes_list
  ]

end

;; Updates all output files
to update_output

  ; Output files are created when first used, instead of in setup,
  ; to keep new output files from being created if setup is executed but go is not.
  ifelse all_cell_output? [
    if not empty? all_cell_attributes_list [
      if all_cell_outfile_name = "a-c-o-n" [ build_output_file_named all_cell_outfile_name ]
      file-open all_cell_outfile_name
      foreach all_cell_attributes_list [ next -> file-print next ]  ; Write each detail to the file
      file-close
      set all_cell_attributes_list (list)                ; Clear the list
    ]
  ][
    set all_cell_attributes_list (list)                ; Clear the list
  ]

  ; The following outputs are produced each tick

  ; Update detailed population output file
  ifelse detailed_population_output? [
    if not empty? detailed_population_list [
      if detailed_population_outfile_name = "d-p-o-n" [ build_output_file_named detailed_population_outfile_name ]
      file-open detailed_population_outfile_name
      foreach detailed_population_list [ next -> file-print next ]  ; Write each detail to the file
      file-close
      set detailed_population_list (list)                ; Clear the list
    ]
  ][
    set detailed_population_list (list)                ; Clear the list
  ]

  ; Update detailed fish events output file
  ifelse fish_events_output? [
    if not empty? fish_events_list [
      if fish_events_outfile_name = "f-e-o-n" [ build_output_file_named fish_events_outfile_name ]
      file-open fish_events_outfile_name
      foreach fish_events_list [ next_cell -> file-print next_cell ]  ; Write each cell event to the file
      file-close
      set fish_events_list (list)                ; Clear the event list
    ]
  ][
    set fish_events_list (list)                ; Clear the event list
  ]

  ; Update detailed cell events output file
  ifelse cell_info_output? [
    if not empty? cell_info_list [
      if cell_info_outfile_name = "c-i-o-n" [ build_output_file_named cell_info_outfile_name ]
      file-open cell_info_outfile_name
      foreach cell_info_list [ next_cell -> file-print next_cell ]  ; Write each cell event to the file
      file-close
      set cell_info_list (list)                ; Clear the event list
    ]
  ][
    set cell_info_list (list)                ; Clear the event list
  ]

  ; Just to be safe & tidy
  file-close-all

end
@#$#@#$#@
GRAPHICS-WINDOW
211
15
570
629
-1
-1
5.769230769230769
1
10
1
1
1
0
1
1
1
-30
30
0
104
1
1
1
ticks
30.0

BUTTON
14
238
78
272
setup
setup
NIL
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

BUTTON
97
238
196
309
go
go
T
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

PLOT
579
14
864
231
Juvenile Sum (cumulative)
Time
# of Juveniles Alive
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"default" 1.0 0 -16777216 true "" "plot count juveniles"

PLOT
579
256
864
477
Fork length over time
Time
Average fork length
0.0
10.0
0.0
3.0
true
true
"" ""
PENS
"mean" 1.0 0 -16777216 true "" "plot mean [f_length] of juveniles"
"min" 1.0 0 -7500403 true "" "plot min [f_length] of juveniles"
"max " 1.0 0 -2674135 true "" "plot max [f_length] of juveniles"

PLOT
871
14
1151
231
Condition factor over time
Time
Condition factor 
0.0
1.0
0.0
1.0
true
true
"" ""
PENS
"mean" 1.0 0 -16777216 true "" "plot mean [fish_condition] of juveniles"
"min" 1.0 0 -9276814 true "" "plot min [fish_condition] of juveniles"

PLOT
871
257
1152
478
Flow vs time
Time
Flow cm3/s
0.0
10.0
0.0
10.0
true
true
"" ""
PENS
"daily flow" 1.0 0 -13791810 true "" "plot flow"

PLOT
1165
12
1451
236
Migrant sum vs time (daily)
Time
Migrant Sum
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"migrant sum" 1.0 0 -16777216 true "" "plot sum table:values migrant_count_table"

PLOT
1465
160
1750
376
Photoperiod vs time
Time
Photoperiod
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"default" 1.0 0 -16777216 true "" "plot photoperiod"

SWITCH
14
112
198
145
detailed_population_output?
detailed_population_output?
0
1
-1000

SWITCH
14
154
198
187
fish_events_output?
fish_events_output?
0
1
-1000

SWITCH
13
195
200
228
cell_info_output?
cell_info_output?
0
1
-1000

CHOOSER
13
19
202
64
background_display
background_display
"veg" "wood" "depth" "velocity" "shade" "predator encounter prob" "wetted fraction" "available velocity shelter" "none"
5

SWITCH
14
73
200
106
draw_fish_movements?
draw_fish_movements?
0
1
-1000

PLOT
1163
258
1453
479
Causes of death (daily)
Time
# of juveniles dead
0.0
10.0
0.0
10.0
true
true
"" ""
PENS
"velocity" 1.0 0 -14070903 true "" "plot sum table:values death_velocity_table"
"temperature" 1.0 0 -2674135 true "" "plot sum table:values death_temp_table"
"stranding" 1.0 0 -6459832 true "" "plot sum table:values death_stranding_table"
"predation" 1.0 0 -10899396 true "" "plot sum table:values death_pred_table"
"poor condition " 1.0 0 -10141563 true "" "plot sum table:values death_condition_table"

BUTTON
13
274
78
308
step
go
NIL
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

SWITCH
13
318
201
351
all_cell_output?
all_cell_output?
1
1
-1000

SWITCH
4
361
210
394
migrant_path_info_output?
migrant_path_info_output?
1
1
-1000

INPUTBOX
7
413
209
473
run_folder
0
1
0
String

@#$#@#$#@
@#$#@#$#@
default
true
0
Polygon -7500403 true true 150 5 40 250 150 205 260 250

airplane
true
0
Polygon -7500403 true true 150 0 135 15 120 60 120 105 15 165 15 195 120 180 135 240 105 270 120 285 150 270 180 285 210 270 165 240 180 180 285 195 285 165 180 105 180 60 165 15

arrow
true
0
Polygon -7500403 true true 150 0 0 150 105 150 105 293 195 293 195 150 300 150

box
false
0
Polygon -7500403 true true 150 285 285 225 285 75 150 135
Polygon -7500403 true true 150 135 15 75 150 15 285 75
Polygon -7500403 true true 15 75 15 225 150 285 150 135
Line -16777216 false 150 285 150 135
Line -16777216 false 150 135 15 75
Line -16777216 false 150 135 285 75

bug
true
0
Circle -7500403 true true 96 182 108
Circle -7500403 true true 110 127 80
Circle -7500403 true true 110 75 80
Line -7500403 true 150 100 80 30
Line -7500403 true 150 100 220 30

butterfly
true
0
Polygon -7500403 true true 150 165 209 199 225 225 225 255 195 270 165 255 150 240
Polygon -7500403 true true 150 165 89 198 75 225 75 255 105 270 135 255 150 240
Polygon -7500403 true true 139 148 100 105 55 90 25 90 10 105 10 135 25 180 40 195 85 194 139 163
Polygon -7500403 true true 162 150 200 105 245 90 275 90 290 105 290 135 275 180 260 195 215 195 162 165
Polygon -16777216 true false 150 255 135 225 120 150 135 120 150 105 165 120 180 150 165 225
Circle -16777216 true false 135 90 30
Line -16777216 false 150 105 195 60
Line -16777216 false 150 105 105 60

car
false
0
Polygon -7500403 true true 300 180 279 164 261 144 240 135 226 132 213 106 203 84 185 63 159 50 135 50 75 60 0 150 0 165 0 225 300 225 300 180
Circle -16777216 true false 180 180 90
Circle -16777216 true false 30 180 90
Polygon -16777216 true false 162 80 132 78 134 135 209 135 194 105 189 96 180 89
Circle -7500403 true true 47 195 58
Circle -7500403 true true 195 195 58

circle
false
0
Circle -7500403 true true 0 0 300

circle 2
false
0
Circle -7500403 true true 0 0 300
Circle -16777216 true false 30 30 240

cow
false
0
Polygon -7500403 true true 200 193 197 249 179 249 177 196 166 187 140 189 93 191 78 179 72 211 49 209 48 181 37 149 25 120 25 89 45 72 103 84 179 75 198 76 252 64 272 81 293 103 285 121 255 121 242 118 224 167
Polygon -7500403 true true 73 210 86 251 62 249 48 208
Polygon -7500403 true true 25 114 16 195 9 204 23 213 25 200 39 123

cylinder
false
0
Circle -7500403 true true 0 0 300

dot
false
0
Circle -7500403 true true 90 90 120

face happy
false
0
Circle -7500403 true true 8 8 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Polygon -16777216 true false 150 255 90 239 62 213 47 191 67 179 90 203 109 218 150 225 192 218 210 203 227 181 251 194 236 217 212 240

face neutral
false
0
Circle -7500403 true true 8 7 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Rectangle -16777216 true false 60 195 240 225

face sad
false
0
Circle -7500403 true true 8 8 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Polygon -16777216 true false 150 168 90 184 62 210 47 232 67 244 90 220 109 205 150 198 192 205 210 220 227 242 251 229 236 206 212 183

fish
false
0
Polygon -1 true false 44 131 21 87 15 86 0 120 15 150 0 180 13 214 20 212 45 166
Polygon -1 true false 135 195 119 235 95 218 76 210 46 204 60 165
Polygon -1 true false 75 45 83 77 71 103 86 114 166 78 135 60
Polygon -7500403 true true 30 136 151 77 226 81 280 119 292 146 292 160 287 170 270 195 195 210 151 212 30 166
Circle -16777216 true false 215 106 30

flag
false
0
Rectangle -7500403 true true 60 15 75 300
Polygon -7500403 true true 90 150 270 90 90 30
Line -7500403 true 75 135 90 135
Line -7500403 true 75 45 90 45

flower
false
0
Polygon -10899396 true false 135 120 165 165 180 210 180 240 150 300 165 300 195 240 195 195 165 135
Circle -7500403 true true 85 132 38
Circle -7500403 true true 130 147 38
Circle -7500403 true true 192 85 38
Circle -7500403 true true 85 40 38
Circle -7500403 true true 177 40 38
Circle -7500403 true true 177 132 38
Circle -7500403 true true 70 85 38
Circle -7500403 true true 130 25 38
Circle -7500403 true true 96 51 108
Circle -16777216 true false 113 68 74
Polygon -10899396 true false 189 233 219 188 249 173 279 188 234 218
Polygon -10899396 true false 180 255 150 210 105 210 75 240 135 240

house
false
0
Rectangle -7500403 true true 45 120 255 285
Rectangle -16777216 true false 120 210 180 285
Polygon -7500403 true true 15 120 150 15 285 120
Line -16777216 false 30 120 270 120

leaf
false
0
Polygon -7500403 true true 150 210 135 195 120 210 60 210 30 195 60 180 60 165 15 135 30 120 15 105 40 104 45 90 60 90 90 105 105 120 120 120 105 60 120 60 135 30 150 15 165 30 180 60 195 60 180 120 195 120 210 105 240 90 255 90 263 104 285 105 270 120 285 135 240 165 240 180 270 195 240 210 180 210 165 195
Polygon -7500403 true true 135 195 135 240 120 255 105 255 105 285 135 285 165 240 165 195

line
true
0
Line -7500403 true 150 0 150 300

line half
true
0
Line -7500403 true 150 0 150 150

pentagon
false
0
Polygon -7500403 true true 150 15 15 120 60 285 240 285 285 120

person
false
0
Circle -7500403 true true 110 5 80
Polygon -7500403 true true 105 90 120 195 90 285 105 300 135 300 150 225 165 300 195 300 210 285 180 195 195 90
Rectangle -7500403 true true 127 79 172 94
Polygon -7500403 true true 195 90 240 150 225 180 165 105
Polygon -7500403 true true 105 90 60 150 75 180 135 105

plant
false
0
Rectangle -7500403 true true 135 90 165 300
Polygon -7500403 true true 135 255 90 210 45 195 75 255 135 285
Polygon -7500403 true true 165 255 210 210 255 195 225 255 165 285
Polygon -7500403 true true 135 180 90 135 45 120 75 180 135 210
Polygon -7500403 true true 165 180 165 210 225 180 255 120 210 135
Polygon -7500403 true true 135 105 90 60 45 45 75 105 135 135
Polygon -7500403 true true 165 105 165 135 225 105 255 45 210 60
Polygon -7500403 true true 135 90 120 45 150 15 180 45 165 90

sheep
false
15
Circle -1 true true 203 65 88
Circle -1 true true 70 65 162
Circle -1 true true 150 105 120
Polygon -7500403 true false 218 120 240 165 255 165 278 120
Circle -7500403 true false 214 72 67
Rectangle -1 true true 164 223 179 298
Polygon -1 true true 45 285 30 285 30 240 15 195 45 210
Circle -1 true true 3 83 150
Rectangle -1 true true 65 221 80 296
Polygon -1 true true 195 285 210 285 210 240 240 210 195 210
Polygon -7500403 true false 276 85 285 105 302 99 294 83
Polygon -7500403 true false 219 85 210 105 193 99 201 83

square
false
0
Rectangle -7500403 true true 30 30 270 270

square 2
false
0
Rectangle -7500403 true true 30 30 270 270
Rectangle -16777216 true false 60 60 240 240

star
false
0
Polygon -7500403 true true 151 1 185 108 298 108 207 175 242 282 151 216 59 282 94 175 3 108 116 108

target
false
0
Circle -7500403 true true 0 0 300
Circle -16777216 true false 30 30 240
Circle -7500403 true true 60 60 180
Circle -16777216 true false 90 90 120
Circle -7500403 true true 120 120 60

tree
false
0
Circle -7500403 true true 118 3 94
Rectangle -6459832 true false 120 195 180 300
Circle -7500403 true true 65 21 108
Circle -7500403 true true 116 41 127
Circle -7500403 true true 45 90 120
Circle -7500403 true true 104 74 152

triangle
false
0
Polygon -7500403 true true 150 30 15 255 285 255

triangle 2
false
0
Polygon -7500403 true true 150 30 15 255 285 255
Polygon -16777216 true false 151 99 225 223 75 224

truck
false
0
Rectangle -7500403 true true 4 45 195 187
Polygon -7500403 true true 296 193 296 150 259 134 244 104 208 104 207 194
Rectangle -1 true false 195 60 195 105
Polygon -16777216 true false 238 112 252 141 219 141 218 112
Circle -16777216 true false 234 174 42
Rectangle -7500403 true true 181 185 214 194
Circle -16777216 true false 144 174 42
Circle -16777216 true false 24 174 42
Circle -7500403 false true 24 174 42
Circle -7500403 false true 144 174 42
Circle -7500403 false true 234 174 42

turtle
true
0
Polygon -10899396 true false 215 204 240 233 246 254 228 266 215 252 193 210
Polygon -10899396 true false 195 90 225 75 245 75 260 89 269 108 261 124 240 105 225 105 210 105
Polygon -10899396 true false 105 90 75 75 55 75 40 89 31 108 39 124 60 105 75 105 90 105
Polygon -10899396 true false 132 85 134 64 107 51 108 17 150 2 192 18 192 52 169 65 172 87
Polygon -10899396 true false 85 204 60 233 54 254 72 266 85 252 107 210
Polygon -7500403 true true 119 75 179 75 209 101 224 135 220 225 175 261 128 261 81 224 74 135 88 99

wheel
false
0
Circle -7500403 true true 3 3 294
Circle -16777216 true false 30 30 240
Line -7500403 true 150 285 150 15
Line -7500403 true 15 150 285 150
Circle -7500403 true true 120 120 60
Line -7500403 true 216 40 79 269
Line -7500403 true 40 84 269 221
Line -7500403 true 40 216 269 79
Line -7500403 true 84 40 221 269

wolf
false
0
Polygon -16777216 true false 253 133 245 131 245 133
Polygon -7500403 true true 2 194 13 197 30 191 38 193 38 205 20 226 20 257 27 265 38 266 40 260 31 253 31 230 60 206 68 198 75 209 66 228 65 243 82 261 84 268 100 267 103 261 77 239 79 231 100 207 98 196 119 201 143 202 160 195 166 210 172 213 173 238 167 251 160 248 154 265 169 264 178 247 186 240 198 260 200 271 217 271 219 262 207 258 195 230 192 198 210 184 227 164 242 144 259 145 284 151 277 141 293 140 299 134 297 127 273 119 270 105
Polygon -7500403 true true -1 195 14 180 36 166 40 153 53 140 82 131 134 133 159 126 188 115 227 108 236 102 238 98 268 86 269 92 281 87 269 103 269 113

x
false
0
Polygon -7500403 true true 270 75 225 30 30 225 75 270
Polygon -7500403 true true 30 75 75 30 270 225 225 270
@#$#@#$#@
NetLogo 6.2.2
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
default
0.0
-0.2 0 0.0 1.0
0.0 1 1.0 0.0
0.2 0 0.0 1.0
link direction
true
0
Line -7500403 true 150 150 90 180
Line -7500403 true 150 150 210 180
@#$#@#$#@
0
@#$#@#$#@
