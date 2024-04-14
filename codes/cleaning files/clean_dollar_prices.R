library(dplyr)

df = read.csv("dollar_price_all.csv")
View(df)

df <- df %>% select(Close, DateTime)
df$DateTime <- as.Date(df$DateTime)
df$Close <- as.integer(gsub(",", "", df$Close))
df<- df %>% filter(DateTime >= "2016-04-01")
df <- df %>% mutate(year = format(DateTime, "%Y")) %>% mutate(month = format(DateTime, "%m"))
df <- df %>% group_by(year, month) %>% filter(DateTime == max(DateTime))%>%
  ungroup() %>% select(-year, -month)
View(df)
write.csv(df, "dollar_price.csv", row.names = F)
