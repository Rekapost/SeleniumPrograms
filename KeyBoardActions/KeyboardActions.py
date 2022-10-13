from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #importing by class from module

serv_obj=Service('C://Users/Reka/Drivers/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(3)
driver.get("https://text-compare.com/")
driver.maximize_window()
#Welcome Reka
#ctrl A
#Ctrl C
#tab
#Ctrl V

Frame1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']").send_keys("Welcome Reka")
act=ActionChains(driver)
# ctrl a to select all
act.key_down(Keys.CONTROL) # pressing down control key
act.send_keys("a") # sending key "a"
act.key_up(Keys.CONTROL)
act.perform()
# ctrl c to copy
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
#tab key
act.send_keys(Keys.TAB).perform()
#ctrl v
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
