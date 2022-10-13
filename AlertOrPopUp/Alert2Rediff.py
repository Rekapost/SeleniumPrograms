import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj=Service('C://Users/Reka/Drivers/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()
driver.implicitly_wait(30)

# opens the alert window: click the alert
#[normalize-space()='Click for JS Prompt'] is a text method ,
# normally in text method ,u have to give value without space
# but in normalize-space , u can give value  with space
driver.find_element(By.XPATH,"//input[@value='Login']").click()

#Actions to perform:
#1.u have to capture the text
#2.write some message
#3.close the alert window by clicking ok or cancel
time.sleep(10)
#1.driver.switch_to.alert will get(switch) to alert window
#alert window is captured
driver.switch_to.alert.accept()

driver.close()
