library(tidyverse)
library(dplyr)

data <- read.csv("/project2/hortacsu/naturalgas/ngasdata.csv")

pipelines <- unique(data$PIPELINE_NAME)

for (i in 1:length(pipelines)) {
  filter <- data[data$PIPELINE_NAME == pipelines[i], ]
  dates <- unique(filter$GAS_DAY)
  dates[length(dates) + 1] <- 44561
  date_diff <- as.data.frame(matrix(ncol = 3, nrow = 0))
  colnames(date_diff) <- c("begin_date_diff", "end_date_diff", "date_diff")
  for (j in 1:(length(dates) - 1)) {
    diff_j <- dates[j+1] - dates[j]
    if (diff_j > 1) {
      date_diff[nrow(date_diff) + 1,] <- c(dates[j], dates[j+1], diff_j)
    }
  }
  new_path <- paste("/home/jasonross/scratch-midway2/check_missing/missing_dates/", as.character(pipeline), ".csv", sep="")
  write.table(date_diff, new_path, sep=",",  col.names=TRUE, row.names = FALSE)
}