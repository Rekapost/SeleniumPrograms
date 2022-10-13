import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import mysql.connector

serv_obj = Service("C://Users//Reka//Drivers//chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()

con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb")
curs = con.cursor()
curs.execute("use fixeddepositcal")
curs.execute("select * from caldat")  # select cmd will return value which will be stored in cursor

for row in curs:  # from cursor get first row and store
    # in first row , capture all data and pass the data to application , when completed go to next row
    principal = row[0]
    RateOfInterest = row[1]
    period1 = row[2]
    period2 = row[3]
    frequency = row[4]
    ExpectedMaturityValue = row[5]
    # 2. pass the data captured to the application
    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(principal)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(RateOfInterest)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(period1)
    # select tag as we have drop down for period 2 year, month date
    periodDrp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))  # "//select[@id='tenurePeriod']"
    periodDrp.select_by_visible_text(period2)
    # select tag as we have drop down for simple interest , compound .........
    frequencyDrp = Select(driver.find_element(By.ID, "frequency"))
    frequencyDrp.select_by_visible_text(frequency)
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()  # calculate button
    # Calculated result is dynamic and it changes frequently, capture the result text
    ActualMaturityValue = driver.find_element(By.XPATH, "//*[@id='resp_matval']/strong").text
    # 3.validation
    if float(ExpectedMaturityValue) == float(ActualMaturityValue):
        print("Test passed")
        # write the captured result in the excel  result column
        # apply green colour if passed
    else:
        print("Test failed")
    # 4. clear all inputs after completing 1 set of data , so that u can enter new set of data ,
    # else it will append and give wrong results
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()  # clear button
    time.sleep(2)
con.close()
driver.close()
