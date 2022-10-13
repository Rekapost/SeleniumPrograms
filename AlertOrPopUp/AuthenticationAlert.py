import time

from selenium import webdriver
#from selenium.webdriver.service.by import By
from selenium.webdriver.chrome.service import Service

serv_obj=Service("C://Users//Reka//Drivers//chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

app=driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
time.sleep(5)
driver.close()
