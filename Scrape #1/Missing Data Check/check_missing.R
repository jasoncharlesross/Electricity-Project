library(tidyverse)
library(dplyr)
library(janitor)

downloaded <- read.csv("/Users/jasonross/Desktop/Hortaçsu/Electricity-Project/Scrape #1/names.csv")$Names
all <- read.csv("/Users/jasonross/Desktop/Hortaçsu/Electricity-Project/Scrape #1/pipeline_names_copy.csv")$Names

missing <- c()

for (i in 1:length(all)) {
  if (!(all[i] %in% downloaded)) {
    missing <- c(missing, all[i])
  }
}

write_csv(data.frame(missing), "/Users/jasonross/Desktop/missing.csv")