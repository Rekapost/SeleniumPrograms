from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.chrome.service import Service

serv_obj=Service('C://Users/Reka/Drivers/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()
"""
# 1. to select specific checkbox
driver.find_element(By.ID,"//input[@id='monday'] ").click()
#or
#driver.find_element(By.ID,"monday").click()
"""
# 2. count number of the checkboxes

checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
#print(len(checkboxes))   # checkboxes is list varaiable name   # 7

# 3. to select all the checkboxes
#approach 1
#for i in range(len(checkboxes)):
 #   checkboxes[i].click()

#approach 2
"""
for checkbox in checkboxes:
    checkbox.click()
"""

# 4 if u want to select specific checkboxes
"""
for checkbox in checkboxes:
    weekname=checkbox.get_attribute("id")
    if weekname== 'monday' or weekname=='sunday':
        checkbox.click() """

# 5 select last 2 checkboxes

for i in range(len(checkboxes)-2,len(checkboxes)):
    checkboxes[i].click()


#6 to select first 2 checkboxes
'''
for i in range(len(checkboxes)):
    if i<2:
        checkboxes[i].click()'''
"""
# clear all checkboxes if all are clicked/selected
for checkbox in checkboxes:
    checkbox.click()

for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
#driver.quit()
"""