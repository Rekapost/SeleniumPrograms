from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium .webdriver.chrome.service import Service
import os

serv_obj=Service('C://Users//Reka//Drivers//chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

"""
#METHOD 1:
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
#to open register link in second tab
registerlink= Keys.CONTROL+Keys.RETURN  # return is enter      control and enter key to open in new tab
driver.find_element(By.LINK_TEXT,"Register").send_keys(registerlink)
"""
"""
#METHOD 2:  opens a new tab and switches to new tab
driver.get("https://demo.nopcommerce.com/")
driver.switch_to.new_window('tab')   # open another tab 
driver.get("https://www.opencart.com")
"""
#METHOD 2:  opens a new tab and switches to new window
driver.get("https://demo.nopcommerce.com/")
driver.switch_to.new_window('window')   # open another window
driver.get("https://www.opencart.com")