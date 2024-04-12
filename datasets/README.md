# Datasets explanation
## 1. Gasoline Price:
First, we downloaded the dataset named **historical_country_turkey_indicator_gasoline_prices_.csv** which explains the price of gasoline in Turkey in US dollars during our desired time interval from **tradingeconomics.com**
.Then, we scraped **tgju.org** website to get the price of US dollars related to IRR (Iranian Rial) and put it in the format of **dollar_price.csv**.
Using these two datasets, we got the **Gas_Price_Rial** column in **turkey_border_data.csv**.

## 2. Traffic Data:
Scraping the data from **141.ir/traffic_datas** and cleaning the datasets, we got **AzarbayjanQharbi1395-1401.csv**. This dataset contains the number of vehicles on most of the roads in Azarbayjan Gharbi province in north-west of Iran, which is located on the border with Türkiye, from 1395 AD to 1401 AD.
From this dataset, we have the columns **Bazargan_vehicles**, **Sarv_vehicles**, **Razi_vehicles** and **Total_vehicles** of **turkey_border_data.csv**. Where Bazargan, Sarv and Razi are the land borders with Türkiye.
