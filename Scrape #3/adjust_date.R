library(tidyverse)
library(dplyr)
library(lubridate)

data <- read.csv("/Users/jason/Desktop/Hortaçsu/Electricity-Project/Scrape #3/missing_dates.csv")

new_data <- data
for (i in 1:nrow(data)) {
  new_data$begin_date_diff[i] <- format(as.Date(as.character(mdy(data$begin_date_diff[i]) + 1), '%Y-%m-%d'), "%m/%d/%Y")
  new_data$end_date_diff[i] <- format(as.Date(as.character(mdy(data$end_date_diff[i]) - 1), '%Y-%m-%d'), "%m/%d/%Y")
}