from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# save_screenshot() ile ekran görüntüsünü alabiliriz.

service = Service("chromedriver.exe")
driver= webdriver.Chrome(service=service)

driver.get("http://ykakkaya.com")
driver.maximize_window()
time.sleep(3)
title=driver.title
if "ykakkaya" in title:
    print(f"bulunduğunğz sayfa {driver.current_url}")
else:
    driver.save_screenshot("./pages.png")

driver.quit()