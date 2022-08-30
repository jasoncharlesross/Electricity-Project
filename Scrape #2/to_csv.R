library(dplyr)
library(readxl)
library(writexl)

setwd('/Users/jasonross/Desktop/download')
file_list = list.files()

i <- 1
for (file in file_list) {
  temp_dataset = read.csv(file)[seq(2,11)]
  new_path <- paste("/Users/jasonross/Desktop/processed/", as.character(i), ".csv", sep="")
  write.table(temp_dataset, new_path, sep=",",  col.names=FALSE, row.names = FALSE)
  rm(temp_dataset)
  i <- i + 1
  i
}