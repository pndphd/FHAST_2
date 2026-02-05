################################################################################
# This script makes the functions form compare runs
################################################################################

##### Subtract two data fromes numeric columns #################################
subtract_dfs = function(df_1, df_2){
  min_size = min(NCOL(df_1), NROW(df_2))
  # return dummy if different number of rows
  if(NROW(df_1) != NROW(df_2)){
    return(df_1)
  }
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

##### Subtract the sum tables ##################################################
subtract_sum = function(df_1, df_2){

  if("geometry" %in% colnames(df_1)){
    df = subtract_group_data(df_1, df_2, "geometry")
  } else {
    df = subtract_dfs(df_1, df_2)
  }
  return(df)
}

##### Subtract two data frames numeric columns #################################
subtract_group_data = function(df_1, df_2, groups){
  df_2_neg = mutate_if(df_2, is.numeric, ~ . * -1)

  df = bind_rows(df_1, df_2_neg) %>% 
    group_by(across(all_of(c(groups)))) %>% 
    summarise_all(sum) %>% 
    ungroup()
  
  if("geometry" %in% groups){
    df = st_as_sf(df)
  }
  return(df)
}

##### Merge the dault mighration energy use data ###############################
merge_adult_energy = function(df_1, df_2){

  # Merge the two date set by labeling
  df_1_lab =  df_1 %>% 
   mutate(species = paste0(species, "_1"))  

  df_out =  df_2 %>% 
    mutate(species = paste0(species, "_2")) %>%
    bind_rows(df_1_lab) 
  
  return(df_out)
}

##### Copy over input files ####################################################
merge_inputs = function(path_1, path_2, out_path, file_name){
  write.table(x = "FILE A _______________________________" %>%
                rbind(read.table(here(path_1, file_name),
                                 sep = '\t',
                                 header = FALSE,
                                 stringsAsFactors = FALSE)) %>%
                rbind("FILE B _______________________________") %>% 
                rbind(read.table(here(path_2, file_name),
                                 sep = '\t',
                                 header = FALSE,
                                 stringsAsFactors = FALSE)),
              file = here(out_path, file_name),
              row.names = FALSE,
              col.names = FALSE)
}

################################################################################
# End
################################################################################