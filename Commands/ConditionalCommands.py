from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.chrome.service import Service

serv_obj=Service('C://Users//Reka//Drivers//chromedriver_win32 (1)//chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

#to check whether search box is displayed or not and enabled or not
searchbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("is searchbox displayed :",searchbox.is_displayed())   #True
print("is searchbox enabled:",searchbox.is_enabled())    #True

# in register page , getting the radio buttons of male and female
rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")

#to check whether the radio buttons for male and female is selected or not
print("default male radio button is selected or not:",rd_male.is_selected())  #False
print("default female radio button is selected or not:",rd_female.is_selected())   #False

#selecting /clicking male button
rd_male.click()
# checking again whether the radio buttons for male and female is selected or not
print("is the male radio button is selected or not:",rd_male.is_selected())  #True
print("is the female radio button is selected or not:",rd_female.is_selected())  #False

#selecting /clicking female button
rd_female.click() # IF Female is selected , male will get deselected
print("is the male radio button is selected or not:",rd_male.is_selected())    #False
print("is the female radio button is selected or not:",rd_female.is_selected())  #True

driver.quit()

