library(dplyr)
library(readxl)
library(writexl)

setwd('/Volumes/Macintosh HD-1/Users/jason/Downloads')
file_list = list.files()

i <- 1
for (file in file_list) {
  temp_dataset <- read_xls(file)
  temp_dataset <- temp_dataset[5:nrow(temp_dataset),]
  new_path <- paste("/Volumes/Macintosh HD-1/Users/jason/Desktop/Hortaçsu/Electricity-Project/Scrape #3/>4 csv format.nosync/", as.character(i), ".csv", sep="")
  write.table(temp_dataset, new_path, sep=",",  col.names=FALSE, row.names = FALSE)
  rm(temp_dataset)
  i <- i + 1
  i
}