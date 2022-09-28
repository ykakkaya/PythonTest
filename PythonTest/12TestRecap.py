
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

service=Service("chromedriver.exe")
driver=webdriver.Chrome(service=service)
url="https://tomspizzeria.herokuapp.com/"
name='a'

def mesaj():
    mesj=driver.find_element(By.XPATH,'//*[@id="mesaj"]').text
    return mesj


def login(url):
    driver.get(url)
    driver.maximize_window()
    validationText=driver.find_element(By.XPATH,'//*[@id="baslik"]/h2')
    if "TOM's Pizzeria" in validationText.text:
        print("sayfa doğrulandı")
  



def process(names):
    name=driver.find_element(By.XPATH,'//*[@id="musteri-adi"]')
    name.send_keys(names)
    
    
def boySecim(int):
    boy=driver.find_element(By.XPATH,f'//*[@id="select-size"]/div/div/div[{int}]/input')
    if boy.is_selected()==False:
        boy.click()
    

def malzeme():


    ybiber=driver.find_element(By.XPATH,'//*[@id="select-topping"]/div/div/div[2]/input')
    if ybiber.is_selected()==False:
        ybiber.click()
    mantar=driver.find_element(By.XPATH,'//*[@id="select-topping"]/div/div/div[3]/input')
    if mantar.is_selected()==False:
        mantar.click()
    
def choosePay():
    paying=driver.find_element(By.XPATH,'//*[@id="odeme-tipi"]')
    select=Select(paying)
    items=select.options    
    select.select_by_value("Kredi Kartı")
    button=driver.find_element(By.XPATH,'//*[@id="siparis"]')
    button.click()


def valid():
    onay=mesaj()
    print(onay)
       



login(url=url)
time.sleep(2)
process(names=name)
time.sleep(2)
boySecim(1)
malzeme()
choosePay()
time.sleep(2)
valid()
time.sleep(2)
driver.quit()

    
