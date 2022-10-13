from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj=Service("C://Users//Reka//Drivers//chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.automationtesting.in/Frames.html")

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()
outerframe=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")   # capture
driver.switch_to.frame(outerframe)                           # pass
innerframe=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")   # capture
driver.switch_to.frame(innerframe)                                 #pass
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("welcome")
driver.switch_to.parent_frame()  # directly switch to parent frame (outerframe)
