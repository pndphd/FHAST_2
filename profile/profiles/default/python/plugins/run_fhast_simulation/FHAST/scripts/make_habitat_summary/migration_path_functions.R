
# function to select appropriate columns and filter depths  --------

prep_habitat_df <- function(df, fish_parm, habitat_parm, min_depth) {
  test = df %>%
    as.data.table() %>% 
    #setnames(old = grep("dista|lat|velo", names(.), value = TRUE), new = c("distance", "lat_dist", "velocity")) %>%
    .[order(distance, lat_dist)] %>%
    # filter cells accessible to the species based on flow
    .[.[[grep(fish_parm$specie, names(.), value = TRUE)]] == 1,] %>%
    # filter columns by depth
    .[.$depth > min_depth, ] %>%
    adjust_velocity_for_wall_factor(fish_parm, habitat_parm) %>%
    # select columns
    .[, .SD, .SDcols = grep("dista|lat|velo|dept|area|temp", names(.), value = TRUE)] %>%
    .[, id := seq(1, nrow(.))] %>% 
    as_tibble()
}

# changes velocity to reflect the depth of benthic fish -------------------

adjust_velocity_for_wall_factor <- function(df, fish_parm, habitat_parm) {
  if (fish_parm$benthic_fish == 1) {
    df %>%
      .[depth >= habitat_parm$ben_vel_height, velocity := velocity * habitat_parm$base_wall_factor]
  } else {
    df
  }
}

# provides minimal columns of prepped df to provide environmental info for destination cells  ---------------------

trim_df_for_joining <- function(prepped_df) {
  prepped_df %>%
    # select columns
    .[, c("distance", "lat_dist", "velocity", "area", "id")] %>%
    setnames(old = c("id", "velocity"), new = c("to", "to_velocity"))
}

# adds coordinates for possible destination cells depending on forward or diagonal movement --------

get_destination_coords <- function(prepped_df, cell_width_m) {
  dist_opt <- c(cell_width_m)
  lat_opt <- c(cell_width_m, -cell_width_m, 0)
  df_w_cell_distances <- expand_grid(prepped_df, node_distance = dist_opt, node_lat_dist = lat_opt)
  df_w_cell_distances %>%
    mutate(
      node_dir = fifelse(node_lat_dist == 0, "f", "s"),
      across(
        node_distance:node_lat_dist,
        .fns = ~ .x + get(str_remove(cur_column(), "node_"))
      )
    )
}

# adds destinations to prepped df and environment values for all cells --------

add_destination_info_to_start_cells <- function(prepped_df, cell_width_m){
  df_trimmed <- trim_df_for_joining(prepped_df)
  test = get_destination_coords(prepped_df, cell_width_m) %>%
    # use inner join of the trimmed df to add data (e.g., velocity) for the destination coordinates and filter
    # out destinations coordinates that don't actually exist
    inner_join(df_trimmed, by = c("node_distance" = "distance", "node_lat_dist" = "lat_dist")) %>%
    # renaming to clarify which cells are origin ("from") and which are destinations ("to")
    setnames(old = c("area.x", "area.y", "id", "velocity"), new = c("from_area", "to_area", "from", "from_velocity"))
  
}


# minimum depth a cell can have to be usable by a fish --------------------

get_min_depth <- function(params, factor) {
  m_per_cm <- 0.01
  factor * params$eg_adult_length * m_per_cm
}

get_cell_length <- function(df, cell_width_m) {
  df %>%
    mutate(across(contains("area"),
      ~ .x / cell_width_m,
      .names = "{str_replace(.col, 'area', 'cell_length')}"
    ))
}

get_cell_hypotenuse <- function(df, cell_width_m) {
  df %>%
    mutate(
      across(contains("cell_length"),
        ~ sqrt(.x^2 + cell_width_m^2),
        .names = "{str_replace(.col, 'length', 'hypotenuse')}"
      )
    )
}

# ratio of cell length to hypotenuse --------------------------------------

# used for scaling diagonal swim speed
get_ratios <- function(df) {
  df %>%
    mutate(
      across(contains("hypotenuse"),
        ~ fifelse(node_dir == "f", 
                  1, 
                  get(str_replace(cur_column(), "hypotenuse", "length")) / .x),
        .names = "{str_replace(.col, 'cell_hypotenuse', 'ratio')}"
      )
    )
}

# calculates swim speed of all fish ---------------------------------------

# based on a numerical estimate of the optimal speed for the Martin et al. model 
# substituted with the FHAST metabolic equations

get_cell_swim_speeds <- function(df, fish_parm) {
  ucrit <- fish_parm$ucrit_m_per_s
  ucrit_cutoff <- fish_parm$ucrit_cutoff_m_per_s
  swim_speed_max <- fish_parm$swim_speed_max_m_per_s
  min_vel_ucrit <- fish_parm$min_vel_ucrit_m_per_s
  max_vel_ucrit <- fish_parm$max_vel_ucrit_m_per_s
  max_water_vel <- fish_parm$max_water_vel_m_per_s
  
  calculate_slope_and_intercept <- function(x1,x2,y1,y2){
   slope <- ( y2 - y1 )/ (x2 - x1)
   intercept <- y1 - slope * x1
   list(intercept=intercept, slope=slope)
  }
  min_vel_params <- calculate_slope_and_intercept(0, min_vel_ucrit, ucrit_cutoff, ucrit)
  max_vel_params <- calculate_slope_and_intercept(max_vel_ucrit, max_water_vel, ucrit, swim_speed_max)
  
  df %>%
    mutate(
      across(ends_with("velocity"),
        .fns = ~ fcase(
          # # multiply swim speed by the ratio of the cell length and cell hypotenuse
          ucrit > ucrit_cutoff &
            min_vel_ucrit * get(str_replace(cur_column(), "velocity", "ratio")) > .x, .x / get(str_replace(cur_column(), "velocity", "ratio")) * min_vel_params$slope + ucrit_cutoff,
          # set ucrit swim speed
          fish_parm$max_vel_ucrit * get(str_replace(cur_column(), "velocity", "ratio")) >= .x, ucrit,
          # burst swim speeds between ucrit and max speed are +50% higher than water velocity
          swim_speed_max > (max_vel_params$slope * .x) / get(str_replace(cur_column(), "velocity", "ratio")) + max_vel_params$intercept, (max_vel_params$slope * .x) / get(str_replace(cur_column(), "velocity", "ratio")) + max_vel_params$intercept,
          swim_speed_max <= .x, NA_real_,
          default = swim_speed_max
        ),
        .names = "{str_replace(.col, 'velocity', 'swim_speed')}"
      )
    )
}

# calculation of cheapest paths between a given set of start and end points --------
# based on Djikstra's algorithm
# returns the distance and lat distance coordinates of cells and the number of paths that went through that cell

get_paths <- function(prepped_df, graph, from, to, weights) {
  map(from, ~ shortest_paths(graph = graph, weights = weights, mode = "out", from = .x, to = to)$vpath) %>%
    unlist() %>%
    as.data.table() %>%
    .[, .N, by = .] %>%
    .[as.data.table(prepped_df), on = c("." = "id"), nomatch = 0] %>%
    setnames(old = "N", new = "num_paths") %>%
    .[, c("distance", "lat_dist", "num_paths")] %>%
    as_tibble()
}

# calculates all costs and paths for a given species ----------------------

get_paths_and_costs <- function(hab_df, 
                                fish_parm_temp, 
                                habitat_parm, 
                                fish_id) {
  # set params --------------------------------------------------------------
  fish_parm <- map(fish_parm_temp, ~.x[[fish_id]])
  species <- fish_parm$specie
  date <- hab_df$date[[1]]
  reach_temp_C <- hab_df$temp[[1]]
  min_depth_m <- get_min_depth(factor = 0.5, fish_parm)
  cell_width_m <- habitat_parm$resolution
  fish_parm[["ucrit_m_per_s"]] <- get_ucrit(fish_parm_temp, fish_id, reach_temp_C)
  fish_parm[["min_vel_ucrit_m_per_s"]] <- get_estimate_for_linear_model(
    fish_parm$pars_min_water_vel_ucrit_int, fish_parm$pars_min_water_vel_ucrit_slope, fish_parm$ucrit_m_per_s)
  fish_parm[["max_vel_ucrit_m_per_s"]] <- get_estimate_for_linear_model(
    fish_parm$pars_max_water_vel_ucrit_int, fish_parm$pars_max_water_vel_ucrit_slope, fish_parm$ucrit_m_per_s)

  # determine cell relationships and costs ----------------------------------
  prepped_df <- prep_habitat_df(hab_df, fish_parm, habitat_parm, min_depth_m)
  relations <- add_destination_info_to_start_cells(prepped_df, cell_width_m) %>% 
    get_cell_length(cell_width_m) %>%
    get_cell_hypotenuse(cell_width_m) %>%
    # hypotenuse multiplier for determining forward velocity component during diagonal movement
    get_ratios() %>%
    get_cell_swim_speeds(
      fish_parm
    ) %>%
    # drop any cells that would have negative overground velocity values
    drop_na() %>%
    mutate(
      energy_cost = rowSums(across(ends_with("swim_speed"),
                                   .fns = ~ get_cost_of_travel(.x, 
                                                               get(str_replace(cur_column(), "swim_speed", "velocity")), 
                                                               fish_parm$ucrit_m_per_s,
                                                               fish_parm_temp,
                                                               fish_id,
                                                               reach_temp_C,
                                                               get(str_replace(cur_column(), "swim_speed", "ratio")) 
                                                               ) *
                                     get(str_replace(cur_column(), "swim_speed", "cell_length"))
      )),
    ) %>%
    .[, c("from", "to", "energy_cost")]

  # build graph and calculate distances ------------------------------------------

  # get ids for all cells
  actors <- prepped_df$id

  # create a graph of all cell relationships
  g <- graph_from_data_frame(relations, vertices = actors)

  # # select cells to start at
  from <- prepped_df[prepped_df$distance == min(prepped_df$distance), ]$id
  to <- prepped_df[prepped_df$distance == max(prepped_df$distance), ]$id


  # costs of moving between cells are equal to the energy cost to the fish
  weights <- relations$energy_cost

  # calculate shortest paths based on energy costs
  distances <- distances(g, weights = weights, mode = "out", v = from, to = to)

  # convert matrix to vector
  distance_vector <- unlist(as.list(distances))
  # check for div by 0
  distance_vector <- distance_vector[is.finite(distance_vector)]

  paths <- get_paths(prepped_df, g, from, to, weights)

  
  data.table(
    date = date, 
    species = species, 
    energy_cost = list(distance_vector),
    paths = list(paths)
  )

}

# runs through the main function for all species --------------------------

get_path_min_costs_all_species <- function(hab_df, fish_parm, habitat_parm, fish_schedule) {
  species <- fish_schedule$species
  fish_ids <- match(species, fish_parm$specie)
  pathfinding_table <- map_dfr(fish_ids, ~ get_paths_and_costs(hab_df, fish_parm, habitat_parm, .x))
  pathfinding_table[as.data.table(fish_schedule), on = "species", nomatch = 0]
}




