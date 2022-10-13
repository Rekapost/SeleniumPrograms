from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #importing by class from module

serv_obj=Service('C://Users/Reka/Drivers/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com")
Elec=driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Electronics']")
CandP=driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Camera & photo']")
# in some application , it will not allow click action , in that case u can use mouse hover action
# MouseHover action
#to perform mouse hover we need create action chains object (built in class in selenium webdriver)
# first create object for the class, through the object we can access all methods through
# which we can perform mouse hover actions
actobj=ActionChains(driver)  # passing driver instance/method

# to create action , not perform the action,,move_to_element method is mouse hover action
#actobj.move_to_element(Elec).move_to_element(CandP).click()
#to perform the action we need to add method call .perform()
actobj.move_to_element(Elec).move_to_element(CandP).click().perform()