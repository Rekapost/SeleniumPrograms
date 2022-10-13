from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj=Service("C://Users//Reka//Drivers//chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

#driver.get("https://opensource-demo.orangehrmlive.com/")
driver.get("http://orangehrm.qedgetech.com/symfony/web/index.php/auth/login")
driver.maximize_window()
window1id=driver.current_window_handle
print(window1id)  #CDwindow-45F3BF15DD39ACFCDB97451E08EE4993   open 1st time
                  #CDwindow-67821C7D3DCC8D3D4A337A914B478C60  When u open second time
                  # new windowid will be created randomly (dynamic)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

windowIDs=driver.window_handles
print(windowIDs)
"""
#Approach 1 for switching bet. 2 browser windows
parentID=windowIDs[0]
print(parentID)
childID=windowIDs[1]
print(childID)
driver.switch_to.window(childID)  # switch to child window
print(driver.title)
driver.switch_to.window(parentID)   # switch to parent window
print(driver.title)
driver.quit()
"""
"""
#Approach 2  switching bet. mulitiple (10..) browser windows  , loop approach
for winid in windowIDs:
    driver.switch_to.window(winid)
    print(driver.title)
"""
"""
# have multiple browser window and want to close specific browser window
#Closing parent window
for winid in windowIDs:
    driver.switch_to.window(winid)
    if (driver.title=="OrangeHRM"):
        driver.close()
"""
"""
#closing child window
for winid in windowIDs:
    driver.switch_to.window(winid)
    if driver.title=="OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM":
        driver.close()
"""
# to randomly close few browser window
for winid in windowIDs:
    driver.switch_to.window(winid)
    if driver.title == "OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM" or driver.title=="xyz":
        driver.close()
