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
library(exactextractr)
library(dplyr)
library(sf)
library(raster)

## -----------------------------------------------------------------------------
clc <- raster(system.file('sao_miguel/clc2018_v2020_20u1.tif',
                     package = 'exactextractr'))
concelhos <- st_read(system.file('sao_miguel/concelhos.gpkg',
                                 package = 'exactextractr'),
                     quiet = TRUE)

## ---- echo = FALSE------------------------------------------------------------
corine_palette <- c(
  "#e6004d", "#ff0000", "#cc4df2", "#cc0000", "#e6cccc", "#e6cce6", "#a600cc",
  "#a64d00", "#ff4dff", "#ffa6ff", "#ffe6ff", "#ffffa8", "#ffff00", "#e6e600",
  "#e68000", "#f2a64d", "#e6a600", "#e6e64d", "#ffe6a6", "#ffe64d", "#e6cc4d",
  "#f2cca6", "#80ff00", "#00a600", "#4dff00", "#ccf24d", "#a6ff80", "#a6e64d",
  "#a6f200", "#e6e6e6", "#cccccc", "#ccffcc", "#000000", "#a6e6cc", "#a6a6ff",
  "#4d4dff", "#ccccff", "#e6e6ff", "#a6a6e6", "#00ccf2", "#80f2e6", "#00ffa6",
  "#a6ffe6", "#e6f2ff", "#ffffff")

plot(clc, col = corine_palette,
     axes = FALSE, legend = FALSE)
plot(st_geometry(concelhos), add = TRUE)

## -----------------------------------------------------------------------------
clc_classes <- foreign::read.dbf(system.file('sao_miguel/clc2018_v2020_20u1.tif.vat.dbf',
                                             package = 'exactextractr'),
                                 as.is = TRUE) %>%
  dplyr::select(value = Value,
                landcov = LABEL3)

levels(clc) <- list(data.frame(ID = clc_classes$value,
                               landcov = clc_classes$landcov))

## -----------------------------------------------------------------------------
factorValues(clc, c(2, 18, 24))

## ----landcov-mode-------------------------------------------------------------
landcov_mode <- exact_extract(clc, concelhos, 'mode', 
                              append_cols = 'name', progress = FALSE) %>%
  inner_join(clc_classes, by=c(mode = 'value'))

## ----landcov-mode-table, echo = FALSE-----------------------------------------
landcov_mode %>%
  dplyr::select(-mode) %>%
  knitr::kable()

## ----landcov-fracs, message = FALSE-------------------------------------------
landcov_fracs <- exact_extract(clc, concelhos, function(df) {
  df %>%
    mutate(frac_total = coverage_fraction / sum(coverage_fraction)) %>%
    group_by(name, value) %>%
    summarize(freq = sum(frac_total))
}, summarize_df = TRUE, include_cols = 'name', progress = FALSE)

## -----------------------------------------------------------------------------
head(landcov_fracs)

## ----landcov-fracs-table------------------------------------------------------
landcov_fracs %>%
  inner_join(clc_classes, by = 'value') %>%
  group_by(name) %>%
  arrange(desc(freq)) %>%
  slice_head(n = 3) %>%
  mutate(freq = sprintf('%0.1f%%', 100*freq)) %>%
  knitr::kable()

## ----landcov-areas, message = FALSE-------------------------------------------
landcov_areas <- exact_extract(clc, concelhos, function(df) {
  df %>%
    group_by(name, value) %>%
    summarize(area_km2 = sum(coverage_area) / 1e6)
}, summarize_df = TRUE, coverage_area = TRUE, include_cols = 'name', progress = FALSE)

## ----landcov-areas-table, echo = FALSE----------------------------------------
landcov_areas %>%
  inner_join(clc_classes, by = 'value') %>%
  dplyr::select(-value) %>%
  group_by(name) %>%
  arrange(desc(area_km2)) %>%
  slice_head(n = 3) %>%
  knitr::kable()

## ----load-pop-density---------------------------------------------------------
pop_density <- raster(system.file('sao_miguel/gpw_v411_2020_density_2020.tif',
                                  package = 'exactextractr'))

## ----landcov-pop-areas, message = FALSE, results = FALSE----------------------
landcov_pop_areas <- exact_extract(clc, concelhos, function(df) {
  df %>%
    group_by(name, value) %>%
    summarize(pop = sum(coverage_area * weight / 1e6)) %>%
    mutate(pop_frac = pop / sum(pop))
}, weights = pop_density, coverage_area = TRUE,
   summarize_df = TRUE, include_cols = 'name')

## ----landcov-pop-areas-table, echo = FALSE------------------------------------
landcov_pop_areas %>%
  inner_join(clc_classes, by = 'value') %>%
  group_by(name) %>%
  arrange(desc(pop_frac)) %>%
  slice_head(n = 1) %>%
  dplyr::select(name, landcov, pop, pop_frac) %>%
  mutate(pop = round(pop),
         pop_frac = round(pop_frac, 3)) %>%
  knitr::kable()

