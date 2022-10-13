from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #importing by class from module

serv_obj=Service('C://Users/Reka/Drivers/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.monsterindia.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//span[@class='uprcse semi-bold']").click()
driver.find_element(By.XPATH,"//*[@id='file-upload']").send_keys("C://Users/Reka/Desktop/New/file-sample_150kB.pdf")

