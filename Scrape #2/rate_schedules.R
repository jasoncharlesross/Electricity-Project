library(dplyr)
library(tidyverse)
library(janitor)

data <- clean_names(read_csv("/Users/jasonross/Desktop/Hortaçsu/Electricity-Project/Scrape #2/all.csv"))
pipeline_names <- read_csv("/Users/jasonross/Desktop/Hortaçsu/Electricity-Project/Scrape #2/pipeline_names.csv")
output <- matrix(nrow = 11, ncol = 100)

for (i in 1:length(pipeline_names$pipeline_sys)) {
  filter <- data %>% filter(pipeline_name == pipeline_names$pipeline_sys[i])
  rate_schedules <- unique(filter$rate_schedule)
  output[i,] <- c(pipeline_names$pipeline_sys[i], rate_schedules, 
                  rep("", 99-length(rate_schedules)))
}

write.csv(output, "/Users/jasonross/Desktop/Hortaçsu/Electricity-Project/Scrape #2/rate_schedule.csv")