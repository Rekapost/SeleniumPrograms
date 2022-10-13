# some webpage have big content ,
# we cannot view the content in one shot fully,
# , we have to scroll down vertically on left side of page to see the remaing content
# scroll action comes from the browser not from application
# so u cannot do this with  mouse action class , we cannot use ActionChains class
# we have a special method , this scroll is related and designed by using javascript
# so have to use javascript to handle scroll
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #importing by class from module

serv_obj=Service('C://Users/Reka/Drivers/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(3)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
# u can scroll down in three different ways
#1. u can scroll down till certain location or certain no of pixel no
#2.**** u can scroll down till u want a specific element (exactly what i want like India flag)****
#3. initial point to end of page
"""
#1. scroll down the page by pixel no(till certain no)
# execute_scrip() in this method u can pass some java script stmts to scroll the web page
# (from 0 position  to 3000 pixel ,empty)
driver.execute_script("window.scrollBy(0,3000)","")
# now u can capture till where it have scrolled down and print the position
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value)   # 3000
"""
"""
#2.scrool down the page till the element u want is visible
IndiaFlag=driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
# argument 1=arguments[0].scrollIntoView(); argument 2= IndiaFlag
driver.execute_script("arguments[0].scrollIntoView();",IndiaFlag)
IndFlagloc=driver.execute_script(("return window.pageYOffset;"))
print("Number of pixels moved:",IndFlagloc)  # 4946  indiaflag will be the first element in the webpage
"""
"""
#3. scroll down till end of page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")   # till end of document
EndOfPage=driver.execute_script(("return window.pageYOffset;"))
print("Number of pixels moved:",EndOfPage)    #36046.66650390625
"""
# 4.it has scrolled from start to somewhere or to end of page , now go back to start(reverse) initial position
# scroll back to initial position
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")   # till end of document
time.sleep(3)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")  # - documenet to go to inital start position
startingofPage=driver.execute_script(("return window.pageYOffset;"))
print("Number of pixels moved:",startingofPage)  # 0