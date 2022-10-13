from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #importing by class from module

serv_obj=Service('C://Users/Reka/Drivers/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
# in right click , u cannot find inspect to capture the element , but u want to inspect ,
# u can still inspect by using certain no of attributes
# right click somewhere on the page , inspect and go to inspect action arrow mark on top left
# then show the element by pointing cursor now the html will be highlighted, now capture the xpath
button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
# right click the button
act=ActionChains(driver)
act.context_click(button).perform()    # perform right click
