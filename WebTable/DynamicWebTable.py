import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj=Service("C://Users//Reka//Drivers//chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

#driver.get("https://opensource-demo.orangehrmlive.com/")
driver.get("http://orangehrm.qedgetech.com/symfony/web/index.php/auth/login")
driver.maximize_window()

#LOGIN
driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys("admin")
driver.find_element(By.XPATH,"//input[@id='txtPassword']").send_keys("admin123")
driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()
time.sleep(3)

# admin--> UserMangemenet---> Users
driver.find_element(By.XPATH,"//*[@id='menu_admin_viewAdminModule']/b").click()
driver.find_element(By.XPATH,"//*[@id='menu_admin_UserManagement']/").click()
driver.find_element(By.XPATH,"//*[@id='menu_admin_viewSystemUsers']/").click()

#table
#find how many users are enabled and how many users are disabled
#go to each and every row and find out last column (status) and capture value
# for  every row , from each row we have to capture status 5th  last column value
# 5 coulumns including check box
# find total no of rows,  no of coulmn is not needed for loop to find all rows
# table tag denotes table , thead is table header  which has many tr and is not needed , so omit thead
# go to tbody , u will find all rows , tr row in a table

#total Rows in a table
rows=len(driver.find_elements(By.XPATH,"//table[@id='resultTable']//tbody/tr"))
print(" total no of rows in a table ", rows)
"""
# repeat each row and capture status column fully (both enabled and disabled),  passsing row no dynamically
for r in range (1,rows+1):
    statusvalues=driver.find_elements(By.XPATH,"//table[@id='resultTable']//tbody/tr["+str(r)+"]/td[5]").text
    print(statusvalues)
"""
# check how many enabled  are there
count=0
for r in range (1,rows+1):
    statusvalues=driver.find_elements(By.XPATH,"//table[@id='resultTable']//tbody/tr["+str(r)+"]/td[5]").text
    if statusvalues=="Enabled":
        count=count+1
print("no of  users(enabled and disabled:", rows) # no of rows is no of users
print("no of enabled users:",count)
print("no of disabled users:",(rows-count))
driver.close()