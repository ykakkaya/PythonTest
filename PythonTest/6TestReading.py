from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

service=Service("chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("http:duckduckgo.com")
driver.maximize_window()
searchBox=driver.find_element(By.XPATH,'//*[@id="search_form_input_homepage"]')
searchBox.send_keys("ykakkaya")
time.sleep(1)
searchBox.send_keys(Keys.ENTER)
time.sleep(2)

result=driver.find_element(By.XPATH,'//*[@id="r1-0"]/div[2]/h2/a/span')
print(result.text)
time.sleep(1)


driver.get("https://ykakkaya.com")
time.sleep(3)
article=driver.find_element(By.XPATH,'//*[@id="ct_text_editor-120ea190"]/div')
print(article.text)

driver.quit()
