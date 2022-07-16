library(dplyr)
library(readxl)
library(writexl)

setwd('/home/jasonross/Desktop/ngas/dir_001')
file_list = list.files()

remove = 1:4

i <- 1
for (file in file_list) {
  temp_dataset = readxl::read_xls(file) %>% slice(-(remove))
  new_path <- paste("/home/jasonross/scratch-midway2/csv_ngas_data/1/", as.character(i), ".csv", sep="")
  write.table(temp_dataset, new_path, sep=",",  col.names=FALSE, row.names = FALSE)
  rm(temp_dataset)
  i <- i + 1
  i
}