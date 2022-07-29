library("rjson")

on_website <- fromJSON(file = "/Users/jasonross/Desktop/Hortaçsu/Electricity-Project/Scrape #2/data.json")
scrape1 <- read.csv(file = "/Users/jasonross/Desktop/Hortaçsu/Electricity-Project/Scrape #2/rate_schedule.csv")

get_missing <- function(website, scrape) {
  missing <- matrix(ncol = 100, nrow= 11)
  for (i in 1:nrow(scrape)) {
    k <- 2
    missing[i,1] <- scrape[i,1]
    for (j in 2:ncol(scrape)) {
      if (!(scrape[i,j] %in% website[[scrape[i,1]]])) {
        missing[i,k] <- scrape[i,j]
        k <- k + 1
      }
    }
  }
  missing
}

out <- get_missing(on_website, scrape1)

write.table(out, "/Users/jasonross/Desktop/Hortaçsu/Electricity-Project/Scrape #2/missing.csv", sep=",",  col.names=FALSE, row.names = FALSE)