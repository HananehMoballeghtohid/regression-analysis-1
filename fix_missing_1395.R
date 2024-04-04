library(readr)
library(openxlsx)

# Add column to some data

# root = 'G:/Data_Selected/1395/1'
root = 'G:/Data_Selected/1395/2'
# Just data in 1395/1,2 had 15 column

files = list.files(path= root, recursive = T, full.names = T)


adjust_vehciel = function(total_vehciel, time_span){
  y = as.integer(1440 / time_span * total_vehciel)
  return(y)
}

for (f in files){
  df = read_excel(f)
  if(ncol(df) == 15){
    df$`تعداد برآورد شده` = adjust_vehciel(df$`تعداد کل وسیله نقلیه`, df$`مدت زمان کارکرد(دقیقه)`)
    write.xlsx(df, file = f, utf8= T)
  }
}

# check corrolation in other data
root = 'G:/Data_Selected/1400/1/Ardebil/Daily'
files = list.files(path= root, full.names = T)
for (i in 1:length(files)){
  file = files[i]
  df = read_excel(file)
  n_adj = df$`تعداد برآورد شده`
  total = df$`تعداد کل وسیله نقلیه`
  time = df$`مدت زمان کارکرد (دقیقه)`
  c = cor(time * n_adj, total)
  l = lm(time * n_adj~ total)
  cat(coef(l), c, "\n")
}
