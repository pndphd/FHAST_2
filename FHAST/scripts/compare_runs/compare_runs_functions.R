################################################################################
# This script makes the functions form compare runs
################################################################################

##### Subtract two data fromes numeric columns #################################
subtract_dfs = function(df_1, df_2){

  min_size = min(NCOL(df_1), NROW(df_2))
  if(min_size > 1){
    df_1_num = df_1 %>% 
      select(where(is.numeric)) %>% 
      st_drop_geometry()
    df_2_num = df_2 %>% 
      select(where(is.numeric)) %>% 
      st_drop_geometry()
    df_3_num = df_1_num - df_2_num
    df_3 = df_1 %>% 
      select(-where(is.numeric)) %>% 
      bind_cols(df_3_num)
    
    return(df_3)
  } else {
    return(df_1)
  }
}

##### Subtract two data frames numeric columns #################################
subtract_time_data = function(df_1, df_2, time_name, group_name){
  df_2_neg = mutate_if(df_2, is.numeric, ~ . * -1)
  
  df = bind_rows(df_1, df_2_neg) %>% 
    group_by(across(all_of(c(group_name, time_name)))) %>% 
    summarise_all(sum)
  return(df)
}

##### Merge the dault mighration energy use data ###############################
merge_adult_energy = function(df_1, df_2){
  df_1 = ml_a$df$adult_migration_energy_data
  df_2 = ml_b$df$adult_migration_energy_data
  
  df_1_avg =  df_1 %>% 
    group_by(species) %>% 
    summarise(energy_cost = mean(energy_cost, na.rm = TRUE)) %>% 
    ungroup()
  
  df_out =  df_2 %>% 
    group_by(species) %>% 
    summarise(energy_cost = mean(energy_cost, na.rm = TRUE)) %>% 
    ungroup() %>% 
    mutate_if(is.numeric, ~ . * -1) %>% 
    bind_rows(df_1_avg) %>% 
    group_by(species) %>% 
    summarise(energy_cost = sum(energy_cost, na.rm = TRUE)) %>% 
    ungroup()
  
  return(df_out)
}



################################################################################
# End
################################################################################