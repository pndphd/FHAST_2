library(ggplot2)
library(tidyr)
library(dplyr)
library(stringr)

##### Load Files #####

#### Read in the brief population output file#############
#### Files should be saved into 'scripts' folder after a simulation run##########

brief_pop_output <- read.csv('BriefPopInfoOut.csv')

##Causes of death (single numbers)






#### Read in the detailed population output file ########

detailed_pop_output <- read.csv('DetailedPopInfoOut.csv')

# First add a column for dates

detailed_pop_output$Days <- seq(1: length(detailed_pop_output$End.of.time.step))

####### Number of juveniles rearing and migrating over time 

# Add column for cumulative migrants over time

detailed_pop_output$cumulative.migrants <- cumsum(detailed_pop_output$Number.of.migrants)

# Plot number of cumulative juveniles and migrants through time (juveniles include smolts)
p <- ggplot(detailed_pop_output, aes(x=Days)) + 
  geom_line(aes(y = Number.of.juveniles), color = "darkred") + 
  geom_line(aes(y = cumulative.migrants), color="steelblue", linetype="twodash") +
  labs (y= "Number of fish")

print(p)

ggsave("num_juveniles_and_migrants_cumulative.png")

#####Plot # of nonsmolts and smolts each day 

# Add column for cumulative smolts over time

detailed_pop_output$cumulative.smolts <- cumsum(detailed_pop_output$Number.of.smolts)

p <- ggplot(detailed_pop_output, aes(x=Days)) + 
  geom_line(aes(y = Number.of.nonsmolts), color = "darkred") +
  geom_line(aes(y = Number.of.smolts), color = "steelblue", linetype="twodash") +
  labs (y= "Number of fish")

print(p)

ggsave("num_nonsmolts_smolts.png")

### Survival estimates over time of rearing (non-smolts) and migrating fish 

#Daily mortality of rearing fish (# dead fish in a day/ # total fish alive in a day)
p <- ggplot(detailed_pop_output, aes(x=Days)) + 
  geom_line(aes(y = Number.of.dead.nonsmolts / Number.of.nonsmolts), color = "darkred") +
  labs (y = "# of dead nonsmolts / # of smolts alive per day")

print(p)

ggsave("mortality_nonsmolts.png")



###### Read in fish events file ########

fish_events_outputs <- read.csv('FishEventsOut.csv')

# First add in column for dates 

fish_events_outputs <- fish_events_outputs %>% 
  group_by(End.of.time.step) %>%
  mutate(Days = cur_group_id()) %>%
  mutate(Days = as.numeric(Days, levels = unique(Days)))

fish_events_outputs$Days<- as.numeric(factor(fish_events_outputs$Days, levels=unique(fish_events_outputs$Days)))

### Plot cause of death over time

# Turn events column into numbers corresponding to cause of death

fish_events_outputs$Event <- as.numeric(c("alive" = "0", "died of stranding" = "1", "died of predation" = "2", "died of poor condition" = "3", "died of temperature" = "4", "died of high velocity" = "5")[fish_events_outputs$Event])

#


# Look at relationship between simulated daily probability of surviving predation. Plots are for fish
# under 7 cm and over 7cm

juveniles_under_7 <- subset(fish_events_outputs,Length <= 7) 
juveniles_under_7 <- juveniles_under_7 %>%
  mutate(newCol = "Juveniles under 7 cm")

juveniles_over_7 <- subset(fish_events_outputs,Length >7)
juveniles_over_7 <- juveniles_over_7 %>%
  mutate(newCol = "Juveniles over 7 cm") 

juveniles <- do.call(rbind, list(juveniles_over_7,juveniles_under_7)) %>%
  rename(Size = newCol)

# remove migrants since their movement/ habitat selection isn't really governed
# by any cell variables

juveniles <- subset(juveniles, juveniles$Event != 'migrated')

# Histograms

# Length distribution of smolts in river at time of smolting
smolt_length <- fish_events_outputs %>%
  filter( Event == "smolted") 

ggplot(smolt_length, aes(x= Length)) + geom_histogram()

ggsave("hist_smoltlength.png")

# Length distribution of smolts in river at time of migration
migrant_length <- fish_events_outputs %>%
  filter( Event == "migrated") 

ggplot(migrant_length, aes(x= Length)) + geom_histogram()

ggsave("hist_migrantlength.png")

# Check if smaller fish (lower in the hierarchy) move around more than larger fish
# These don't include fish that migrated but do include drifters
# Number of cells visited

ju7 <- juveniles_under_7 %>%
  distinct(ID, Cell) %>%
  group_by(ID) %>%
  summarize("cells visited" = n()) %>%
  mutate(ID = replace(ID, ID < 10000, "Juveniles under 7"))

juveniles_over_7 <- subset(juveniles_over_7, juveniles_over_7$Event != 'migrated')

jo7 <- juveniles_over_7 %>%
  distinct(ID, Cell) %>%
  group_by(ID) %>%
  summarize("cells visited" = n()) %>%
  mutate(ID = replace(ID, ID < 10000, "Juveniles over 7"))

juveniles_cell_visit <- do.call(rbind, list(jo7,ju7))

p <- boxplot(juveniles_cell_visit$`cells visited` ~ juveniles_cell_visit$ID, xlab = '', ylab = 'Number of cells visited') 

print(p)

ggsave("size_cells_visited.png")










# # Velocity
# p = ggplot() +
#   geom_point(data = juveniles, aes(x = Velocity.at.cell, y = Path.survival, group = Size, color = Size, alpha = .1)) +
#   xlab('Velocity (m/s)') +
#   ylab('Path survival of destination cell') + guides(alpha=FALSE)
#  
# print(p)
# 
# ggsave("pathsurvival_velocity.png")
# 
# # Depth
# p = ggplot() + 
#   geom_point(data = juveniles, aes(x = Depth.at.cell, y = Path.survival, group = Size, colour = Size, alpha = .1)) +
#   xlab('Depth (m/s)') +
#   ylab('Path survival of destination cell') + guides(alpha=FALSE)
# 
# print (p)
# 
# ggsave("path_survival_depth.png")
# 
# # Distance to cover
# p = ggplot() + 
#   geom_point(data = juveniles, aes(x = Distance.to.cover, y = Path.survival, group = Size, colour = Size, alpha = .1)) +
#   xlab('Distance to cover (m)') +
#   ylab('Path survival of destination cell') + guides(alpha=FALSE)
# 
# print (p)
# 
# ggsave("pathsurvival_distcover.png")
# 
# #Fish length
# p = ggplot() + 
#   geom_point(data = fish_events_outputs, aes(x = Length, y = Path.survival ), color = "red" ) +
#   xlab('Length (cm)') +
#   ylab('Path survival of destination cell') 
# 
# print(p)
# 
# ggsave("pathsurvival_flength.png")
# 
# #Fish condition
# p = ggplot() + 
#   geom_point(data = juveniles, aes(x = Condition, y = Path.survival, group = Size, colour = Size, alpha = .1)) +
#   xlab('Condition') +
#   ylab('Path survival of destination cell') + guides(alpha=FALSE)
# 
# print (p)
# 
# ggsave("pathsurvival_condition.png")
# 
# 
# # Look at relationship between velocity and other fish variables. Plots are for fish
# # under 7 cm and over 7cm
# 
# # Velocity 
# p = ggplot() + 
#   geom_point(data = juveniles, aes(x = Velocity.at.cell, y = Growth, group = Size, color = Size, alpha = .1)) +
#   xlab('Velocity (m/s)') +
#   ylab('Daily growth (g)') + guides(alpha=FALSE)
# 
# print (p)
# 
# ggsave("growth_velocity.png")
# 
# # Velocity
# p = ggplot() + 
#   geom_point(data = juveniles, aes(x = Velocity.at.cell, y = Fraction.growth.of.cmax, group = Size, color = Size, alpha = .1)) +
#   xlab('Velocity (m/s)') +
#   ylab('Daily food intake (fraction of cmax)')+ guides(alpha=FALSE)
# 
# print (p)
# 
# ggsave("fraccmax_velocity.png")
# 
# # Velocity
# p = ggplot() + 
#   geom_point(data = juveniles, aes(x = Velocity.at.cell, y = Percent.daily.growth, group = Size, color = Size, alpha = .1)) +
#   xlab('Velocity (m/s)') +
#   ylab('Daily growth (percent of body weight)') + guides(alpha=FALSE)
# 
# print (p)
# 
# ggsave("percentweight_velocity.png")
# 
# p = ggplot() + 
#   geom_point(data = juveniles, aes(x = Velocity.at.cell, y = Condition, group = Size, color = Size, alpha = .1)) +
#   xlab('Velocity (m/s)') +
#   ylab('Fish condition') + guides(alpha=FALSE)
# 
# print (p)
# 
# ggsave("condition_velocity.png")
# 
# # Depth 
# p = ggplot() + 
#   geom_point(data = juveniles, aes(x = Depth.at.cell, y = Growth, group = Size, color = Size, alpha = .1)) +
#   xlab('Depth (m)') +
#   ylab('Daily growth (g)') + guides(alpha=FALSE)
# 
# print (p)
# 
# ##### 
# 
#   
# 
# 
