from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

#click() metodu kullanımı

service=Service("chromedriver.exe")
driver=webdriver.Chrome(service=service)

driver.get("http://www.duckduckgo.com")
driver.maximize_window()
time.sleep(1)
searchbox=driver.find_element(By.XPATH,'//*[@id="search_form_input_homepage"]')
searchbox.send_keys("ykakkaya.com")
driver.find_element(By.XPATH,'//*[@id="search_button_homepage"]').click()
driver.save_screenshot("ykakkaya.png")
time.sleep(2)



driver.get("http://google.com")
driver.maximize_window()
searcBox2=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
searcBox2.send_keys("python")
driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()
driver.save_screenshot("pythonSearch.png")
time.sleep(2)

driver.quit()