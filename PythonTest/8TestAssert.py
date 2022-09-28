#assert metodu test başarılı ise uyarı vermez ama başarısız ise hata fırlatır ve program kesilir.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

service=Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
def login(username,password):
    driver.get("https://the-internet.herokuapp.com/login")
    userBox=driver.find_element(By.XPATH,'//*[@id="username"]')
    userBox.send_keys(username)
    passBox=driver.find_element(By.XPATH,'//*[@id="password"]')
    passBox.send_keys(password)
    driver.find_element(By.XPATH,'//*[@id="login"]/button/i').click()
    message=driver.find_element(By.XPATH,'//*[@id="content"]/div/h4').text
    return message

loginMessage=login("tomsmith","SuperSecretPassword!")
print(loginMessage)
assert 'Welcome to the Secure Area' in loginMessage



