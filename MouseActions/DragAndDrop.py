from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #importing by class from module

serv_obj=Service('C://Users/Reka/Drivers/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(3)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
#1. know source element
#2. know target element  to know to move from where to where
act=ActionChains(driver)

SourceCapital1=driver.find_element(By.ID,"box6")
TargetCountry1=driver.find_element(By.ID,"box106")
act.drag_and_drop(SourceCapital1,TargetCountry1).perform()  # drag and drop operations

SourceCapital2=driver.find_element(By.ID,"box3")
TargetCountry2=driver.find_element(By.ID,"box103")
act.drag_and_drop(SourceCapital2,TargetCountry2).perform()  # drag and drop operations

driver.close()
