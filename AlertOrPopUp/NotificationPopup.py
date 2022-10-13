from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

optionsobject=webdriver.ChromeOptions()
optionsobject.add_argument("--disable-notifications")

serv_obj=Service("C://Users//Reka//Drivers//chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj,options=optionsobject)

driver.get("https://whatmylocation.com/")
driver.maximize_window()