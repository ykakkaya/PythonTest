#imdb ye git. Menu ye tıkla. top 250 movies linkine tıkla
#film listesini getir sıra no -film adı- yılı
#2000 yılında çekilen filmleri getir


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

service=Service("chromedriver.exe")
driver=webdriver.Chrome(service=service)
url="https://www.imdb.com/"

def login():
    driver.get(url=url)
    driver.maximize_window()
    driver.find_element(By.XPATH,'//*[@id="imdbHeader-navDrawerOpen--desktop"]/div').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="imdbHeader"]/div[2]/aside/div/div[2]/div/div[1]/span/div/div/ul/a[2]/span').click()

def chose():
    film_list=driver.find_elements(By.XPATH,'//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr/td[2]')
    return film_list

login()
list=chose()
#film listesi

for i in list:
    print(i.text)

#2000 yılındaki filmler
print("***********************************************")
for i in list:
    if i.text[-5:-1]=="2020":
        print(i.text)

driver.quit()