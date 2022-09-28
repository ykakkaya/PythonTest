
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

service=Service("chromedriver.exe")
driver=webdriver.Chrome(service=service)
url="https://tomspizzeria.herokuapp.com/"
driver.get(url)
driver.maximize_window()
orta=driver.find_element(By.XPATH,'//*[@id="select-size"]/div/div/div[2]/input')
if orta.is_selected()==False:
    orta.click()
time.sleep(1)
zeytin=driver.find_element(By.XPATH,'//*[@id="select-topping"]/div/div/div[1]/input')
if zeytin.is_selected()==False:
    zeytin.click()
time.sleep(1)
mantar=driver.find_element(By.XPATH,'//*[@id="select-topping"]/div/div/div[3]/input')
if mantar.is_selected()==False:
    mantar.click()
time.sleep(1)
driver.quit()