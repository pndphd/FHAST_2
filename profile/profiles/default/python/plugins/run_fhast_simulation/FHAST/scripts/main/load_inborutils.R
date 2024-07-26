# This script checks if you have inborutils installed and loads it 

if(!require("inborutils", character.only = T)){
  install.packages("inborutils",
                   repos = c(inbo = "https://inbo.r-universe.dev",
                             CRAN = "https://cloud.r-project.org"))
}

