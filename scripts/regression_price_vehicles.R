library(dplyr)
library(ggplot2)
library(corrplot)

df = read.csv("turkey_border_data.csv")
View(df)

df <- df %>% select(-DateTime)

correlation_matrix = cor(df)
testRes = cor.mtest(df, conf.level = 0.95)
corrplot(correlation_matrix, method = "circle", addCoef.col = "black",
         tl.col = "black", type = 'upper', col.lim = c(0,1),
         p.mat = testRes$p, sig.level = 0.05, diag = F)

corrplot(correlation_matrix, p.mat = testRes$p, method = 'color', diag = FALSE, type = 'upper',
         sig.level = c(0.001, 0.01, 0.05), pch.cex = 1,
         insig = 'label_sig', pch.col = 'grey20', order = 'AOE')

l = lm(Sarv_vehicles~Gas_Price_Rial, data= df)
summary(l)
ggplot(df, aes(Razi_vehicles, Gas_Price_Rial)) + geom_point() + geom_smooth(method='lm') +
  labs(
    x = "Number of Vehicles (Razi)",
    y = "Gas Price (Rial)",
  )

ggplot(df, aes(Sarv_vehicles, Gas_Price_Rial)) + geom_point() + geom_smooth(method='lm') +
  labs(
    x = "Number of Vehicles (Sarv)",
    y = "Gas Price (Rial)",
  )

ggplot(df, aes(Bazargan_vehicles, Gas_Price_Rial)) + geom_point() + geom_smooth(method='lm') +
  labs(
    x = "Number of Vehicles (Bazargan)",
    y = "Gas Price (Rial)",
  )

ggplot(df, aes(Total_vehicles, Gas_Price_Rial)) + geom_point() + geom_smooth(method='lm') +
  labs(
    x = "Number of Vehicles (Total)",
    y = "Gas Price (Rial)",
  )
