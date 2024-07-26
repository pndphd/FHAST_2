# the function selects valid paths the fish can migrate over

make_migration_paths = function(flows = NULL,
                                flow_level = NULL,
                                species = NULL,
                                df_in = NULL){

  # make a variable name
  variable_name = paste0("mig_path_", species)
  
  # find the flow value
  flow_value = ifelse(flow_level>=max(d_values),
                      max(d_values),
                      d_values[min(which(sort(d_values) >= flow_level))])

  # make a df of possible cells
  sampeled_grid_out = df_in %>% 
    select(paste0("wetd.D", flow_value)) %>% 
    rename(wetted = 1) %>% 
    mutate(!!variable_name := ifelse(wetted == 0, 0, 1)) %>% 
    select(-wetted)
}
         
