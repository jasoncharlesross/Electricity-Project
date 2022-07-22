library(dplyr)
library(readxl)
library(writexl)

setwd('/home/jasonross/Desktop/ngas')
file_list = list.files()

remove = 1:4

for (file in file_list) {
  if (!exists("dataset")) {
    dataset = readxl::read_xls(file) %>% slice(-(remove))
    names(dataset) <- c("POINT_NAME", "OPERATIONAL_CAPACITY_KEY", "GAS_DAY", 
                        "RECEIPT_DLVY", "SCH CAPACITY", "PIPELINE_NAME", 
                        "POINT_TYPE", "FLOW_INDICATOR", "CYCLE", 
                        "AVAIL_CAPACITY", "FREQ", "MAX_CAPACITY")
    paste("/home/jasonross/Desktop/", as.character(i), ".csv", sep="")
  }
  else {
    temp_dataset = readxl::read_xls(file) %>% slice(-(remove))
    names(temp_dataset) <- c("POINT_NAME", "OPERATIONAL_CAPACITY_KEY", "GAS_DAY", 
                             "RECEIPT_DLVY", "SCH CAPACITY", "PIPELINE_NAME", 
                             "POINT_TYPE", "FLOW_INDICATOR", "CYCLE", 
                             "AVAIL_CAPACITY", "FREQ", "MAX_CAPACITY")
    dataset<-rbind(dataset, temp_dataset)
  }
}

write.csv(dataset, "/home/jasonross/Desktop/out.xlsx")