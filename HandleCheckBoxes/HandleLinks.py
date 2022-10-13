from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.chrome.service import Service

serv_obj=Service('C://Users//Reka//Drivers//chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# how to click a link
#driver.find_element(By.LINK_TEXT,"Digital downloads").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()


# how to get no of links in the webpage, links have common tagname //a
#links=driver.find_elements(By.TAG_NAME,"a")
#links=driver.find_elements(By.XPATH,"//a")
#print(len(links))   # 90

# how to print all the links in the webpage
links=driver.find_elements(By.TAG_NAME,"a")
for link in links:
    print(link.text)

#driver.quit()