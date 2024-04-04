library(readxl)
library(data.table)
library(dplyr)
library(jalcal)

setwd('G:/Data_Selected')


country = 'AzarbayjanQharbi'
# root = '1400/1/AzarbayjanQharbi/Daily'
# files = list.files(path = root, recursive = T, full.names = TRUE)

files <- c()
for (year in 1395:1401) {
  for (month in 1:12) {
    root <- file.path(as.character(year), as.character(month), country, "Daily")
    files <- c(files, list.files(path = root, recursive = T, full.names = TRUE))
  }
}

# year = '1395'
# for (month in 1:12) {
#   root <- file.path(year, as.character(month), country, "Daily")
#   files <- c(files, list.files(path = root, recursive = T, full.names = TRUE))
# }

tables <- lapply(files, read_excel)
D <- do.call(rbind , tables)

# for (file in files){
#   d = read_excel(file)
#   D = rbind(D, d)
#   print(file)
# }

names(D) = c('road_id', 'road_name', 'time_start', 'time_end', 'time_span',
             'vehicles_total', 'vehicles_class1', 'vehicles_class2',
             'vehicles_class3', 'vehicles_class4', 'vehicles_class5', 'average_speed', 
             'unauthorized_speed', 'unauthorized_distance', 'unauthorized_overtaking', 'n_adjusted')
D0 <- D %>% select(!(average_speed:unauthorized_overtaking))

date_adjust = function(t){
  t <- t %>% strsplit(' ') %>% unlist()
  d <- t[1]
  date_list <- d %>% strsplit('/') %>% unlist() %>% sapply(as.numeric)
  date <- jal2greg(date_list[1], date_list[2], date_list[3])
  #date <- as.POSIXct(date)
  return(date)
}

D0 <-D0 %>% mutate(time = do.call(c, lapply(D$time_end, date_adjust)))
D0 <- D0 %>% select(!(time_start:time_span))

D0 <- D0 %>% mutate(month = format(time, "%m"))
D0 <- D0 %>% mutate(year = format(time, "%Y"))
View(D0)

D1 <- D0 %>% group_by(road_id,year, month) %>% summarize(road_name = first(road_name),
            vehicles_total = sum(n_adjusted),time = first(time)) %>% ungroup() %>%
  arrange(year, month) %>% select(road_id, road_name, vehicles_total, everything())
View(D1)

write.csv(D1, 'C:/Users/Almas/OneDrive/Documents/R/AzarbayjanQharbi1395-1401.csv', fileEncoding = 'UTF-8')
