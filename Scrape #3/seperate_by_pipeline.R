library(tidyverse)
library(dplyr)

data <- read.csv("/project2/hortacsu/naturalgas/ngasdata_fixed.csv")

pipelines <- unique(data$PIPELINE_NAME)

#all_date_diffs <- as.data.frame(matrix(ncol = 4, nrow = 0))
#colnames(all_date_diffs) <- c("begin_date_diff", "end_date_diff", "date_diff", "pipeline")

for (i in 1:length(pipelines)) {
  filter <- data[data$PIPELINE_NAME == pipelines[i], ]
  #dates <- sort(unique(filter$GAS_DAY))
  #if (dates[length(dates)] != 44561) {
  #  dates[length(dates) + 1] <- 44561
  #}
  #date_diff <- as.data.frame(matrix(ncol = 4, nrow = 0))
  #colnames(date_diff) <- c("begin_date_diff", "end_date_diff", "date_diff", "pipeline")
  #for (j in 1:(length(dates) - 1)) {
  #  diff_j <- dates[j+1] - dates[j]
  #  if (diff_j > 1) {
  #    date_diff[nrow(date_diff) + 1,] <- c(dates[j], dates[j+1], diff_j, pipelines[i])
  #  }
  #}
  #all_date_diffs <- rbind(all_date_diffs, date_diff)
  new_path <- paste("/project2/hortacsu/naturalgas/data_by_pipeline/", as.character(pipelines[i]), ".csv", sep="")
  write.table(filter, new_path, sep=",",  col.names=TRUE, row.names = FALSE)
}

#write.table(all_date_diffs, 
#            "/project2/hortacsu/naturalgas/missing_dates.csv", 
#            sep=",",  col.names=TRUE, row.names = FALSE)

#diffs <- function(vector) {
#  res <- as.data.frame(matrix(nrow = 0, ncol = 2))
#  for (i in 1:(length(vector) - 1)) {
#    diff <- vector[i+1] - vector[i]
#    if (diff > 1) {
#      res[nrow(res) + 1,] <- c(vector[i], diff)
#    }
#  } 
  res
}