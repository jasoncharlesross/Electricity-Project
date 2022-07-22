library(dplyr)
library(readxl)
library(writexl)

setwd('/home/jasonross/scratch-midway2/csv_ngas_data/6bad')
file_list = list.files()

i <- 1
for (file in file_list) {
 data = read.csv(file)[-c(1)]
 new_path <- paste("/home/jasonross/scratch-midway2/csv_ngas_data/6/", as.character(i), ".csv", sep="")
 write.table(data, new_path, sep=",",  col.names=FALSE, row.names = FALSE)
 rm(data)
 i <- i+1
}