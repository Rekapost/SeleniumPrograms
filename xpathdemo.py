from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj=Service('C://Users//Reka//Drivers//chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

#relative xpath  find search button using relative xpath
"""
driver.find_element(By.XPATH,"//*[@id='search_query_top']").send_keys("T-Shirt")  # attribute value in single quatation
driver.find_element(By.XPATH,"//button[@id='searchbox']/button").click()"""

#absolute  xpath/full xpath
"""
driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("t-shirt")
driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()"""

# or operator
#driver.find_element(By.XPATH,"//*[@id='search_query_top'or @name='search_query']").send_keys("T-Shirt")
#driver.find_element(By.XPATH,"//*[@type='submit' or  @name='submit_search']").click()

#and  or operator
#driver.find_element(By.XPATH,"//input[@id='search_query_top'or @name='search_query']").send_keys("T-Shirt")
#driver.find_element(By.XPATH,"//button[@type='submit' and @name='submit_search']").click()

#contains and starts-with operator
#driver.find_element(By.XPATH,"//input[contains(@id,'search')]").send_keys("T-Shirt") # since conatins search word is enough
#driver.find_element(By.XPATH,"//button[starts-with(@name,'submit_')]").click()

#text method  if u want to identify an element using inner text
#Women
driver.find_element(By.XPATH,"//a[text()='Women']").click()





