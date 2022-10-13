from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

serv_obj=Service('C://Users//Reka//Drivers//chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
# Dropdown input box
driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
# all countries  list
countrieslist=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(countrieslist))  #249
# to select one item from the list (bootstrap dropdown)
for country in countrieslist:
    if country.text=="India":     # webelement text:text
        country.click()
        break
