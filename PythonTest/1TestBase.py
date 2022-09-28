from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# servise e driver konumunu tanımlıyoruz
# bir web driver oluşturuyoruz.
# get metodu ile url ye gidiyoruz.


service=Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://ykakkaya.com")
time.sleep(3)
driver.close()
