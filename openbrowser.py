# open browser
# webdriver is a module which is available in  selenium package

from selenium import webdriver
from selenium.webdriver.common.by import By   #selenium 4
from selenium .webdriver.chrome.service import Service   #  import service class from module , service is class for executable path deprecated error
#service class object serv_obj     service means location of chromedriver
serv_obj=Service('C://Users//Reka//Drivers//chromedriver.exe')  #constructor it takes the location of the object
# chrome class is given object name as driver
driver = webdriver.Chrome(service=serv_obj)  # mentioning the object  driver is object, to launch browser

#chrome class is given object name as driver
#driver = webdriver.Chrome('C://Users//Reka//Drivers//chromedriver.exe')
#or

# if u dont want to mention the path every time, u can save the chromedriver.exe where u installed Python,
# in Python folder , scripts folder save chromedriver.exe
#driver=webdriver.Chrome()
#or

#serv_obj=Service('C://Users//Reka//Drivers//chromedriver_win32 (1)//chromedriver.exe')
#driver = webdriver.Chrome(service=serv_obj)

# access all methods by driver object
driver.get('https://opensource-demo.orangehrmlive.com/')    # get method to launch url in browser

#selenium 4
driver.find_element(By.NAME,"txtUsername").send_keys("Admin") # find_element() method and send_keys()method
driver.find_element(By.ID, "txtPassword").send_keys("admin123") #find element take 2 arguments locator and actual value parameters
driver.find_element(By.ID,"btnlogin").click()

"""SELENIUM 3
driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
"""

act_title = driver.title
exp_title = "OrangeHRM"
if act_title == exp_title:
    print("login passed")
else:
    print("login failed")
driver.close()     # driver object
#DeprecationWarning: executable_path has been deprecated, please pass in a Service object, so importing service class

