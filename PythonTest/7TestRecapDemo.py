# https://the-internet.herokuapp.com/login sitesine git
# kullanıcı adı: tomsmith
# password: SuperSecretPassword! gir. giriyorsa  içindeki metni yazdır. logout ol doğrula
# yanlış kullanıcı adı gir dene doğrula
# yanlış password gir dene doğrula

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

servis=Service("chromedriver.exe")
driver=webdriver.Chrome(service=servis)
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()



userName="tomsmith"
wronguser="tom"
password="SuperSecretPassword!"
wrongPass="SuperSecretPassword"

userArea=driver.find_element(By.XPATH,'//*[@id="username"]')
userArea.send_keys(userName)
time.sleep(1)
passArea=driver.find_element(By.XPATH,'//*[@id="password"]')
passArea.send_keys(password)
time.sleep(1)

driver.find_element(By.XPATH,'//*[@id="login"]/button/i').click()
time.sleep(2)
message=driver.find_element(By.XPATH,'//*[@id="content"]/div/h4')


if "Welcome" in message.text:
    print("pozitif test passed")
    messagePass=driver.find_element(By.XPATH,'//*[@id="flash"]').text
    print(messagePass)

    driver.find_element(By.XPATH,'//*[@id="content"]/div/a').click()
    messageLogout=driver.find_element(By.XPATH,'//*[@id="flash"]').text
    print(messageLogout)
else:
    print("negatif test passed")
    messageFailed=driver.find_element(By.XPATH,'//*[@id="flash"]').text
    print(messageFailed)

driver.quit()
