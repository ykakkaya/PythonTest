from selenium.webdriver.support.select import Select
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

odeme=driver.find_element(By.XPATH,'//*[@id="odeme-tipi"]')
select=Select(odeme)
odeme_list=select.options

for item in odeme_list:
    print(item.text)

select.select_by_visible_text("Nakit")

time.sleep(3)

select.select_by_index(3)
time.sleep(2)
driver.quit()


