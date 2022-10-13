from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.chrome.service import Service

#CREATING SERVICE OBJECT AND DRIVER OBJECT
serv_obj=Service('C://Users//Reka//Drivers//chromedriver_win32 (1)//chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

#OPEN THE APPLICATION url
driver.get('https://opensource-demo.orangehrmlive.com/')
#title of the current url ,as each page has different title
print(driver.title)   #OrangeHRM
#to check the current url is same as url we asked to open/launch
print(driver.current_url)    #https://opensource-demo.orangehrmlive.com/
#page source of the current url
print(driver.page_source)   # prints everything in page source of that current url (source code of the page)

driver.quit()
