# Make the summary tabel of values
make_abm_table = function(df){
  summary_abm_stats = data.frame(Species = df$Species[1]) %>% 
    mutate(reach_capacity = max(df$rearers),
           mean_daily_survival_all = weighted.mean(x = df$all_survival_prob,
                                                   w = df$juveniles),
           mean_daily_survival_nonmigrant = weighted.mean(x = df$nonmigrant_survival_prob,
                                                        w = df$nonmigrants),
           #mean_daily_survival_smolt = weighted.mean(x = df$smolt_survival_prob,
                                                    # w = df$smolts),
           mean_daily_survival_migrant = weighted.mean(x = df$migrant_survival_prob,
                                                       w = df$migrants),
           mean_daily_survival_rearing = weighted.mean(x = df$rear_survival_prob,
                                                       w = df$rearers),
           fraction_dead_stranding = sum(df$stranding_deaths, na.rm = TRUE)/
             sum(df$dead_fish, na.rm = TRUE),
           fraction_dead_temperature = sum(df$high_t_deaths, na.rm = TRUE)/
             sum(df$dead_fish, na.rm = TRUE),
           fraction_dead_condition = sum(df$poor_condition_deaths, na.rm = TRUE)/
             sum(df$dead_fish, na.rm = TRUE),
           fraction_dead_predation = sum(df$predation_deaths, na.rm = TRUE)/
             sum(df$dead_fish, na.rm = TRUE),
           mean_net_energy_ppJdd = weighted.mean(x =df$mean_energy,
                                                 w = df$juveniles,
                                                 na.rm = TRUE),
           mean_growth_rearing_ppcmdd = weighted.mean(x =df$mean_rearing_growth_length,
                                                      w = df$rearers,
                                                      na.rm = TRUE)) %>% 
    pivot_longer(cols = !matches("Species"), names_to = "Item", values_to = "Value") %>% 
    mutate(Item = str_replace_all(Item, "_", " "),
           Item = str_replace_all(Item, "pp", "("),
           Item = str_replace_all(Item, "dd", ")"),
           Value = round(Value,4))
}