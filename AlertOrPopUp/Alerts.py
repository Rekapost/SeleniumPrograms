import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj=Service('C://Users/Reka/Drivers/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# opens the alert window: click the alert
#[normalize-space()='Click for JS Prompt'] is a text method ,
# normally in text method ,u have to give value without space
# but in normalize-space , u can give value  with space
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(3)

#Actions to perform:
#1.u have to capture the text
#2.write some message
#3.close the alert window by clicking ok or cancel

#1.driver.switch_to.alert will get(switch) to alert window
#alert window is captured
alertwindow=driver.switch_to.alert
#2. to capture the text in alert window
print(alertwindow.text)

# 3.pass value to inputbox
alertwindow.send_keys("Welcome")

# 4.accept (ok button) and dismiss (cancel button) method
#close alertwindow by ok button
#alertwindow.accept()

#5.if u want to close the alertwindow by cancel
alertwindow.dismiss()
driver.close()
