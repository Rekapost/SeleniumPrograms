from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #importing by class from module

#driver=webdriver.Chrome()
serv_obj=Service('C://Users/Reka/Drivers/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(By.NAME,"Email").clear()
driver.find_element(By.NAME,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.NAME,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()

act_title=driver.title
exp_title="Dashboard / nopCommerce administration"
if act_title==exp_title:
    print("login passed")
else:
    print("login failed")
driver.close()



