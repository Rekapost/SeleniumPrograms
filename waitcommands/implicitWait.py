import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.chrome.service import Service

serv_obj=Service('C://Users//Reka//Drivers//chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://www.google.com")
driver.maximize_window()

searchbox=driver.find_element(By.NAME,"q")
#time.sleep(10)
searchbox.send_keys("selenium")
searchbox.submit()

driver.find_element(By.TAG_NAME,"h3").click()
driver.quit()