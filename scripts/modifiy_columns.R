library(readxl)
library(openxlsx)

folder_path <- 'G:/Data_Selected'
valid_name5 = 'مدت زمان کارکرد (دقیقه)'
# In some files, name of column 5 is 'مدت زمان کارکرد(دقیقه)' (without space)

valid_name13 = 'تعداد تخلف سرعت غیر مجاز'
valid_name14 = 'تعداد تخلف فاصله غیر مجاز'
valid_name15 = 'تعداد تخلف سبقت غیر مجاز'
# In most files, غیرمجاز is with space

files <- list.files(path = folder_path, pattern = "\\.xlsx$",recursive = T, full.names = T)

for (file in files) {
  data <- read_excel(file)
  x <- colnames(data)[5]
  if (x != valid_name5){
    colnames(data)[5] <- valid_name5
    colnames(data)[13] <- valid_name13
    colnames(data)[14] <- valid_name14
    colnames(data)[15] <- valid_name15
    write.xlsx(data, file, utf8= T)

    cat("Modified file:", file, "\n")
  }
  else{
    cat('Not modified:', file, "\n")
  }

}

# Result : The data of 1395 and some of the data of 1396 were modified.