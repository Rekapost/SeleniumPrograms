from selenium import webdriver
from selenium.webdriver.common.by import By

import os
location=os.getcwd()    # current working directory

#How to Download File in chrome browser
def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service('C://Users/Reka/Drivers/chromedriver.exe')

# to download the file inside the python directory without changing the global location of the system,
# download at the desired location at run time (preferences is dictionary object  to store key and value pair)
# or preferences ={"download.default_directory":"C://Users/Reka/PycharmProjects/SeleniumProject/DownloadFile.py"}   # save files in desired location
    preferences ={"download.default_directory":location}   # save files in desired location
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)  # desired location   prefs is default keyword predefined parameter

    driver = webdriver.Chrome(service=serv_obj,options=ops)
    return driver

#AUTOMATION CODE
my_driver=chrome_setup()
my_driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
my_driver.maximize_window()
my_driver.find_element(By.XPATH,"//*[@id='table-files']/tbody/tr[1]/td[5]/a[1]").click()

#FIREFOX
# ops=webdriver.FirefoxOptions()
# ops.set_preferences("browser.helperApps.neverAsk.saveToDisk","application/msword")
#application/msword is mime type as document type may vary
# MIME TYPES OF different files
#https://www.sitepoint.com/mime-types-complete-list/
#ops.set_preference("browser.download.manager.showWhenStarting",False)  to skip that popup open with
#to download in desired location
#set_preferences("browser.download.folderList",0)    it can be 0 or 1 or 2
# 0 means file will be downloaded in desktop
# 1 means   default download location
# 2 means    desired or specific location
#ops.set_preference("browser.download.dir",location)

# TO DOWNLOAD PDF FILE  u have to add
# 1. for chrome
#preferences = {"download.default_directory": location,"plugins.always_open_pdf_externally":True}  # save files in desired location
# 2. for edge browser , it will open not download , as there is open bug in selenium
# 3. for firefox  edit mime type  application/pdf
# ops.set_preference("pdfjs.disabled",True)
