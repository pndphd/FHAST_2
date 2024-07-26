########################################
# This makes functions for the summarize habitat script
########################################

get_bined_results = function(df = NULL, 
                             column = NULL,
                             name = NULL,
                             bin_count = 4){

  df_bare = st_drop_geometry(df)
  total_area = sum(df_bare$wetted_area, na.rm = TRUE)
  bins = seq(0,
             max(select(df_bare, {{column}}), na.rm = TRUE),
             length.out = bin_count)
 
  
  result = df_bare %>%
    group_by(name = cut({{column}}, breaks = bins)) %>%
    summarise(area = round(sum(wetted_area),2),
              percent_area = round(sum(wetted_area)/total_area * 100,3)) %>% 
    na.omit()
  
  return(result)
}

