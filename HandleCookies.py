from selenium import webdriver
from selenium .webdriver.chrome.service import Service

serv_obj=Service('C://Users//Reka//Drivers//chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# get default cookies created by website  capture cookies from the browser
cookieslist=driver.get_cookies()
print("cookies list:",len(cookieslist))     # 3

# print details of all cookies
for c in cookieslist:
    print(c)
"""
#to extract specific value of the cookies
for c in cookieslist:
    print(c.get('name'))
# to print name and value of the cookies
for c in cookieslist:
    print(c.get('name'),":",c.get('value'))
"""
# How to add new cookie to the browser
driver.add_cookie({"name":"mycookie","value":"123456"})
cookieslist=driver.get_cookies()
print("cookies list after adding 1 cookie:",len(cookieslist))
# delete specific cookie from the browser
# specify cookie name
driver.delete_cookie("mycookie")
cookieslist=driver.get_cookies()
print("new cookies list after deleting 1 cookie:",len(cookieslist))
# delete all cookies
driver.delete_all_cookies()
cookieslist=driver.get_cookies()
print("new cookies list after deleting all cookie:",len(cookieslist))

driver.quit()
