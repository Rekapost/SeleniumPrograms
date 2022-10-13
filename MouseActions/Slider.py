from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #importing by class from module

serv_obj=Service('C://Users/Reka/Drivers/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(3)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

minslider=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")
maxslider=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")

print("Location of slider Before moving .....")
# we can move only in x-axis in horizontal slider,
# if slider is in vertical position we move y axis 
print(minslider.location)  #{'x': 59, 'y': 250}
print(maxslider.location)   #{'x': 510, 'y': 250}

act=ActionChains(driver)
#Add some value to x-axis to move forward(increase price)
act.drag_and_drop_by_offset(minslider,100,0).perform()  # pass(element, x-axis, y-axis as we r not going to do anything with y)
#decrease some value from x-axis to move backward(decrease price)
act.drag_and_drop_by_offset(maxslider,-110,0).perform()

print("Location of slider after moving .....")
print(minslider.location)    #{'x': 159, 'y': 250}
print(maxslider.location)    #{'x': 398, 'y': 250}
