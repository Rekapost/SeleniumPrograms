from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.chrome.service import Service
import os

serv_obj=Service('C://Users//Reka//Drivers//chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
# How to capture screenshot of the webpage
""" 
# method 1: to capture homepage screenshot
# specify path to save screenshot  specify screenshot name homepage.png, jpg....
#driver.save_screenshot("C://Users//Reka//PycharmProjects//SeleniumProject//homepage.png")    or or or or
driver.save_screenshot(os.getcwd()+"//homepage.png")
"""
"""
# method 2:
driver.get_screenshot_as_file(os.getcwd()+"//homepage.png")
"""

#capture screenshot in binary format, u have to write script to convert from binary to image
#method 3:
driver.get_screenshot_as_png()
#method:4:
driver.get_screenshot_as_base64()

driver.quit()