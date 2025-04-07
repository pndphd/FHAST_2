#############################################################
# This is the script copies the data from the 2 folders to 
# a new folder
#############################################################

# Make the new output folder
dir.create(file.path(new_folder))

# Make function that copies all the needed things
folder = 
  
copy_over = function(input_folder, number){
  j_files = c("abm_summary_table.rds",
              "predator_rating_area_stats_table.rds",
              "mort_risk_area_stats_table.rds",
              "fish_parm.rds",
              "pred_list.rds",
              "fish_list.rds")
                
                # mean_map variabel used for predator_map
  j_p_files = c("habitat_map.shp", 
                # map_data variabel used for predation_map
                "full_map_data.rds"
                
    
  )
  
  a_files = c("summary_migration_table.rds")
  
  g_files = c("summary_stats_table.rds",
              "summary_stats_cutoff_table.rds",
              "fish_energy_area_stats_table.rds",
              "habitat_parm.rds",
              "summary_fish_stats_table.rds")
} 