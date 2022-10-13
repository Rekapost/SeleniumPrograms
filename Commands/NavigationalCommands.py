from selenium import webdriver
from selenium .webdriver.chrome.service import Service

serv_obj=Service('C://Users//Reka//Drivers//chromedriver_win32 (1)//chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.snapdeal.com") # opens snapdeal
driver.get("https://www.amazon.com")   # opens amazon

driver.back()     #open snapdeal
driver.forward()  #open amazon

driver.refresh()
driver.quit()