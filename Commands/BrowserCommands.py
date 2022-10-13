# CLOSE()  QUIT()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.chrome.service import Service
serv_obj=Service('C://Users/Reka/Drivers/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
#driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()
driver.find_element(By.LINK_TEXT,'OrangeHRM, Inc').click()

time.sleep(5)  # to wait for 5 sec

#driver.close()   # it closes only "https://opensource-demo.orangehrmlive.com/"
driver.quit() # it closes both "https://opensource-demo.orangehrmlive.com/" and LINK_TEXT,"OrangeHRM, Inc".click()
