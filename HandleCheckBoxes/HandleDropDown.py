import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.chrome.service import Service
import requests as requests
from selenium.webdriver.support.select import Select

serv_obj=Service('C://Users//Reka//Drivers//chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()
#dropdowncountry_ele=driver.find_element(By.ID,"input-country")
#dropdowncountry=Select("dropdowncountry_ele")
dropdowncountry=Select(driver.find_element(By.ID,"input-country"))

# select option from dropdown
#dropdowncountry.select_by_visible_text("India")
#dropdowncountry.select_by_value("10")  # value
#dropdowncountry.select_by_index(13)   #index

# to capture all the option from dropdown and print
alloptions=dropdowncountry.options  #option==>return all options as webelement,dropdowncountry==>select class object
#print("total no of all options:", len(alloptions))   # 242
"""
for option in alloptions:
    print(option.text)"""

# REQUIREMENT IS i want to select from option without using built in functions like select_by_
"""
for option in alloptions:
    if option.text=="India":
        time.sleep(5)
        option.click()
    break"""

# if there is no select tag name , or only button
"""
driver.find_elements(By.XPATH,"//select[@id='input-country']/option")
print(len(alloptions)) """   #242

