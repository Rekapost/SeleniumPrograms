from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #importing by class from module

serv_obj=Service('C://Users/Reka/Drivers/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(3)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()
driver.switch_to.frame("iframeResult")
driver.find_element(By.XPATH,"//input[@id='field1']").clear()
driver.find_element(By.XPATH,"//input[@id='field1']").send_keys("Welcome Reka")
button=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
act=ActionChains(driver)
act.double_click(button).perform()
