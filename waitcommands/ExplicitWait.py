import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium .webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj=Service('C://Users//Reka//Drivers//chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
#mywait=WebDriverWait(driver,10)   # basic syntax
# explicit syntax to avoid exceptions
mywait=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=
                        [Exception,NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
driver.get("https://www.google.com")
driver.maximize_window()

searchbox=driver.find_element(By.NAME,"q")
searchbox.send_keys("selenium")
searchbox.submit()

searchlink=mywait.until(EC.presence_of_element_located((By.TAG_NAME,"h3")))
searchlink.click()
driver.quit()