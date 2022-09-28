from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# get ile url ye gidiyoruz
# penceremizi maximize_window ile tam ekran yapıyoruz
# current_url ile sayfanın url sini alıyoruz
# title ile sayfanın title ını alıyoruz
# back() ile önceki sayfa forward() ile ilerideki sayfaya geçiş yapılıyor.

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

print("ykakkaya olması beklenen")
driver.get("http://ykakkaya.com")
driver.maximize_window()
title1=driver.title
print(f"syfamızın url :{driver.current_url}")
print(f"sayfamızın title : {title1}")
time.sleep(2)

print("etsy olması beklenen")
driver.get("http://etsy.com")
title2=driver.title
print(f"sayfamızın url :{driver.current_url}")
print(f"sayfamızın title : {title2}")
time.sleep(2)

print("ykakkaya olması beklenen")
driver.back()
titleback=driver.title
print(f"sayfamızın url :{driver.current_url}")
print(f"sayfamızın title : {titleback}")
time.sleep(1)

print("etsy olması beklenen")
driver.forward()
titleforw=driver.title
print(f"sayfamızın url :{driver.current_url}")
print(f"sayfamızın title : {titleforw}")

driver.close()