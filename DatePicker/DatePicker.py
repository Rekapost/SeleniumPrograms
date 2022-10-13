import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj=Service("C://Users//Reka//Drivers//chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
#date picker is inside frame, so u have to switch to frame and then insert date
# since u have 1 frame in this page , u can use switch_to.frame(index)
driver.switch_to.frame(0)   #switch to frame
#Real time applications , either one can be selected not both past or future
# Travel websites future date
# for enetering date of birth , we need past dates and years
#mm/dd//yy
"""
#1. direct type
driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("09/28/2022")
"""
#Pass everything in text format through date picker (Expected)
year="2021"
#year="2023"
month="August"
date="15"
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()   # opens datepicker element

#2. If u know the starting point and ending point then for loop
# since we dont know the satrting point and ending point we have to go to while loop, dont know condition
# making while loop true for starting ,it will go to infinite loop , as condition is true all times,
# but when it will be exited , when condition is false
# so here coming out of the while loop , by using break command  to exit from loop
# first focus on month and year
# capture month and year and compare with the expected month and year
while True:
    actmonth=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    actyear=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if actmonth==month and actyear==year:
        break

    else:
# or    driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click() #Next arrow
#       driver.find_element(By.XPATH,"//a[@title='Next']").click()
        driver.find_element(By.XPATH,"//a[@title='Prev']").click()  #(previous arrow)

# after month and year is selected , now we have to select date
# capture all the dates from the table
alldates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td")
# compare with expected date
for d in alldates:
    if d.text==date:
        d.click()
        break
time.sleep(10)
driver.close()


