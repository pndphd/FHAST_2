## ---- include = FALSE---------------------------------------------------------
knitr::opts_chunk$set(
  collapse = TRUE,
  comment = "#>",
  fig.width = 7
)
knitr::opts_knit$set(
  global.par = TRUE
)

## ---- include = FALSE---------------------------------------------------------
par(mar = c(1, 1, 1, 1))

## ----setup, message = FALSE---------------------------------------------------
library(dplyr)
library(exactextractr)
library(raster)
library(sf)

## ----load-data-1--------------------------------------------------------------
pop_count <- raster(system.file('sao_miguel/gpw_v411_2020_count_2020.tif',
                                package = 'exactextractr'))
concelhos <- st_read(system.file('sao_miguel/concelhos.gpkg',
                                 package = 'exactextractr'),
                     quiet = TRUE)
plot(pop_count, axes = FALSE)
plot(st_geometry(concelhos), add = TRUE)

## ----total-pop-cellstats------------------------------------------------------
cellStats(pop_count, 'sum')

## ---- echo = FALSE------------------------------------------------------------
sao_miguel_pop <- cellStats(pop_count, 'sum')

## ----extract-example----------------------------------------------------------
exact_extract(pop_count, concelhos, 'sum', progress = FALSE)

## ----extract-pop-by-sum, cache = TRUE-----------------------------------------
concelho_pop <- exact_extract(pop_count, concelhos, 'sum', 
                              append_cols = 'name', progress = FALSE) %>%
  rename(pop = sum) %>%
  arrange(desc(pop)) %>%
  bind_rows(summarize(., name = 'Total', pop = sum(pop)))

## ---- echo = FALSE------------------------------------------------------------
concelho_pop %>%
  mutate(pop = prettyNum(round(pop), big.mark = ',')) %>%
  knitr::kable()

## ----calc-missing-pop, echo=FALSE, results='hide'-----------------------------
total_pop <- filter(concelho_pop, name == 'Total') %>% pull(pop)
missing_pop_pct <- (sao_miguel_pop - total_pop) / sao_miguel_pop
missing_pop_pct

## ----plot-pop-ponta-delgada---------------------------------------------------
plot.new()
plot.window(xlim = c(-25.75, -25.55), ylim = c(37.70, 37.77))
rect(par("usr")[1], par("usr")[3], par("usr")[2], par("usr")[4], col = "#9cc0f9")
plot(pop_count, add = TRUE, axes = FALSE, alpha = 0.8, horizontal = TRUE)
plot(st_geometry(concelhos), add = TRUE)

## ----load-data-2--------------------------------------------------------------
pop_density <- raster(system.file('sao_miguel/gpw_v411_2020_density_2020.tif',
                                  package = 'exactextractr'))

## ----pop-from-density, cache = TRUE-------------------------------------------
concelho_pop2 <- exact_extract(pop_density, concelhos, 
                               function(density, frac, area) {
                                 sum(density * frac * area)
                               }, 
                               weights = raster::area(pop_density),
                               append_cols = 'name',
                               progress = FALSE)

## ---- echo = FALSE------------------------------------------------------------
concelho_pop2 %>%
  rename(pop = result) %>%
  arrange(desc(pop)) %>%
  bind_rows(summarize(., name = 'Total', pop = sum(pop))) %>%
  mutate(pop = prettyNum(round(pop), big.mark = ',')) %>%
  knitr::kable()

## ----pop-missing-from-density, echo=FALSE, results='hide'---------------------
missing_pop_pct <- 100 * (sao_miguel_pop - sum(concelho_pop2$result)) / sao_miguel_pop
stopifnot(missing_pop_pct < 1)

## ----pop-from-density-2, results = 'hide'-------------------------------------
exact_extract(pop_density, concelhos, 'weighted_sum', weights = 'area')

## ----plot-elevation-----------------------------------------------------------
elev <- raster(system.file('sao_miguel/eu_dem_v11.tif', package = 'exactextractr'))

plot(elev, axes = FALSE, box = FALSE)
plot(st_geometry(concelhos), add = TRUE)

## ----pop-weighted-mean-elev, results = 'hide'---------------------------------
exact_extract(elev, concelhos,  'weighted_mean', weights = pop_density)

## ----pop-weighted-mean-elev-2, results = 'hide'-------------------------------
exact_extract(elev, concelhos,
              function(df) {
                weighted.mean(x = df$value,
                              w = df$coverage_fraction * df$pop_density * df$area,
                              na.rm = TRUE)},
              weights = stack(list(pop_density = pop_density,
                                   area = area(pop_density))),
              summarize_df = TRUE,
              progress = FALSE)

## ----pop-weighted-mean-elev-3-------------------------------------------------
concelho_mean_elev <- exact_extract(elev, concelhos, c('mean', 'weighted_mean'), 
                                    weights = pop_density,
                                    coverage_area = TRUE, 
                                    append_cols = 'name', progress = FALSE)

## ---- echo = FALSE------------------------------------------------------------
concelho_mean_elev %>%
  rename(mean_elev = mean,
         pop_weighted_mean_elev = weighted_mean) %>%
  arrange(name) %>%
  knitr::kable()

