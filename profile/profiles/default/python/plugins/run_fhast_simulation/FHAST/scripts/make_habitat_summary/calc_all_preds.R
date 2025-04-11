# a function to do the predator calculations

calc_all_preds = function(p_id, pred_habitat, fish_length){
  # Get the pred and prey length
  pred_length = exp(pred_parm$pred_length_mean[[p_id]])
  prey_length = exp(pred_parm$gape_a[[p_id]] +
                      pred_parm$gape_b[[p_id]] * pred_length^2)
  # Check if it is vulnerable to predation
  length_pred_bonous = ifelse(fish_length >= prey_length, 0, 1)
  pred_habitat = pred_habitat %>% 
    mutate(shaded = ifelse(shade > 0.5, 1, 0),
           substrate = rowSums(across(gravel:rock)),
           # if rocky substrate is the majority in a cell, then 1, else 0
           substrate = if_else(substrate >= fine & substrate > 0, 1, 0),
           # Calculate the predation function
           input = pred_parm$pred_glm_int[[p_id]] +
             pred_parm$pred_glm_shade[[p_id]] * shaded +
             pred_parm$pred_glm_veg[[p_id]] * veg +
             pred_parm$pred_glm_wood[[p_id]] * wood +
             pred_parm$pred_glm_depth[[p_id]] * depth +
             pred_parm$pred_glm_velocity[[p_id]] * velocity +
             pred_parm$pred_glm_substrate[[p_id]] * substrate,
           # Calculate the habitat rating
           hab_rating = 1 / (1 + exp(-input))* ifelse(wetted_area > 0, 1, 0)) %>% 
    group_by(date) %>% 
    mutate(# Place predators
      predators = replace_na(round((hab_rating * wetted_area) /
                                     sum(hab_rating * wetted_area) *
                                     reach_preds), 0)) %>% 
    ungroup() %>% 
    mutate(# Calculate the temp effect 
      temp_effect = 1 / (1 + exp(-(temp* pred_parm$area_pred_b[[p_id]] +
                                     pred_parm$area_pred_a[[p_id]]))),
      # Calculate the fraction of area the predators occupy
      porp_area = pmin(predators * (ml$df$habitat_parms$reaction_distance *
                                      ml$df$habitat_parms$t_area_effect * temp_effect) / (wetted_area),
                       predators),
      # calculate the distance to cover
      dis_to_cover_m = pmax(sqrt(area) * (ml$df$habitat_parms$int_pct_cover +
                                ml$df$habitat_parms$sqrt_pct_cover * sqrt(cover_fra) +
                                ml$df$habitat_parms$pct_cover * cover_fra +
                                ml$df$habitat_parms$sqrt_pct_cover_x_pct_cover * cover_fra ^ 1.5),
                              0),
      # Calculate the survival bonuses 
      survival_bonus = 1/(1+exp(-(ml$df$habitat_parms$dis_to_cover_int +
                                    ml$df$habitat_parms$dis_to_cover_m * dis_to_cover_m))),
      turb_bonus = 1 / (1 + exp(-1 *(ml$df$habitat_parms$turbidity_int +
                                       turb * ml$df$habitat_parms$turbidity_slope))),
      survival_prob = 1 - (1 - survival_bonus) * (1 - turb_bonus),
      # Calculate the predation risk and include the length bonus
      pred_mort_risk = if_else(porp_area > 1,
                               1 - (survival_prob ^ porp_area),
                               porp_area * (1 - survival_prob)) * length_pred_bonous) %>% 
    # Remove temporary columns
    select(hab_rating, pred_mort_risk) %>% 
    rename_with( ~ paste0(.x, paste0("_" , p_id)))
}
