from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import glob
import shutil

# Setup ChromeDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get('https://141.ir/')

print("opening website...")

# Add cookies from your manually logged-in session
# Replace 'cookie_name' and 'cookie_value' with actual cookie names and values
driver.add_cookie({'name': 'XSRF-TOKEN', 'value': ''})
driver.add_cookie({'name': '_ga_FL2KFC7ED7', 'value': ''})
driver.add_cookie({'name': 'remember_client_web_59ba36addc2b2f9401580f014c7f58ea4e30989d', 'value': ''})
driver.add_cookie({'name': '141_session', 'value': ''})
driver.add_cookie({'name': '_ga', 'value': ''})
# Add other cookies as needed

driver.get('https://141.ir/traffic_datas')
time.sleep(5)

print("logging in...")

# Find the year buttons
year_buttons = driver.find_elements(By.CSS_SELECTOR, '[class*="select-year"]')

main_dir = 'داده های تردد'
if not os.path.exists(main_dir):
        os.makedirs(main_dir)

for year_button in year_buttons:
    
    year_dir = f"{main_dir}/{year_button.text}"
    if not os.path.exists(year_dir):
        os.makedirs(year_dir)
        
    while (True):
                try:
                    year_button.click()
                    break
                except Exception as e:
                    driver.execute_script("arguments[0].scrollIntoView(true);", year_button)
        
    time.sleep(5)
    
    month_buttons = driver.find_elements(By.CSS_SELECTOR, '[class*="select-month"]')
    for month_button in month_buttons:
        
        month_dir = f"{year_dir}/{month_button.text}"

        if not os.path.exists(month_dir):
            os.makedirs(month_dir, exist_ok=True)
            
        desired_folder = os.path.abspath(month_dir)
    
        while (True):
                try:
                    month_button.click()
                    break
                except Exception as e:
                    driver.execute_script("arguments[0].scrollIntoView(true);", month_button)
                    
        
        print("started downloading", year_button.text, month_button.text)
        
        time.sleep(5)
        
        download_buttons = driver.find_elements(By.CSS_SELECTOR, '[title*="دانلود"]')
        for download_button in download_buttons:
            
            while (True):
                try:
                    download_button.click()
                    break
                except Exception as e:
                    driver.execute_script("arguments[0].scrollIntoView(true);", download_button)
                    
                    
            time.sleep(5)
        
            folder_path = r"C:\Users\asus\Downloads"
            file_type = r'\*rar*'
            
            while(True):
                files = glob.glob(folder_path + file_type)
                latest_file = max(files, key=os.path.getctime)
                if not latest_file.endswith('.crdownload'):
                    shutil.move(latest_file, desired_folder)
                    print("moving file...")
                    break
                else:
                    time.sleep(1)
        
            time.sleep(5)
            
driver.quit()
            
            
            
    




