from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


# send_keys ile input gönderme
#find_element() ile locator bulma


service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://duckduckgo.com")
driver.maximize_window()
title=driver.title
print(title)
url=driver.current_url
print(url)
time.sleep(2)

searchbox=driver.find_element(By.XPATH,'//*[@id="search_form_input_homepage"]')
searchbox.send_keys("selenium")
time.sleep(2)
searchbox.send_keys(Keys.ENTER)
time.sleep(2)

driver.get("http://google.com")
print(driver.title)
print(driver.current_url)
time.sleep(1)
searchBox2=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
searchBox2.send_keys("python selenium")
time.sleep(1)
searchBox2.send_keys(Keys.ENTER)
time.sleep(2)

driver.quit()