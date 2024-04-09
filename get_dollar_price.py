from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Setup ChromeDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get('https://www.tgju.org/profile/price_dollar_rl/history')

print("opening website...")

time.sleep(5)

data = []
for i in range(100):
    table = driver.find_element(By.XPATH, "//table")
    headers = [header.text for header in table.find_elements(By.XPATH, ".//th")]
    rows = table.find_elements(By.XPATH, ".//tr")
    print('downloading rows')
    for row in rows[1:]: # Skip the header row
        cols = row.find_elements(By.XPATH, ".//td")
        data.append([col.text for col in cols])
    print('downloaded page number' , i)
    button = driver.find_element(By.ID, "DataTables_Table_0_next")
    button.click()
    print('found next button...')
    time.sleep(2)

df = pd.DataFrame(data)
df.to_csv('doolar.csv', index=False)
print(df)