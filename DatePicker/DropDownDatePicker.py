import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

serv_obj=Service("C://Users//Reka//Drivers//chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
expyear="2021"
expmonth="August"
expdate="15"

#DATE OF BIRTH
#1.INPUT BOX
driver.find_element(By.XPATH,"//input[@id='dob']").click() # OPEN DATE PICKER
#2.Class name to handle dropdown  is Select
actmonth=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
actmonth.select_by_visible_text("Aug")
actyear=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
actyear.select_by_value("1983")
# comparing and clicking date
alldates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td")
for d in alldates:
    if d.text==expdate:
        d.click()
        break
time.sleep(10)
driver.close()
