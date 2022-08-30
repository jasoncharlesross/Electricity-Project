library(dplyr)
library(tidyverse)
library(janitor)
library(rjson)

data <- clean_names(read_csv("/Users/jasonross/Desktop/Hortaçsu/Electricity-Project/Scrape #2/all.csv"))
pipeline_names <- read_csv("/Users/jasonross/Desktop/Hortaçsu/Electricity-Project/Scrape #2/pipeline_names.csv")

get_rates <- function(contracts, pipelines) {
  output <- matrix(ncol = 100, nrow = 11)
  for (i in 1:length(pipelines$pipeline_sys)) {
    filter <- contracts %>% filter(pipeline_name == pipelines$pipeline_sys[i])
    unique <- unique(filter$rate_schedule)
    output[i,1] <- pipelines$pipeline_sys[i]
    output[i,2:(length(unique)+1)] <- unique
  }
  output
}

out <- get_rates(data, pipeline_names)

write.table(out, "/home/jasonross/scratch-midway2/check_missing/columbia.csv", sep=",",  col.names = FALSE, row.names = FALSE)