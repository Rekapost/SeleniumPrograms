from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
"""
serv_obj=Service("C://Users//Reka//Drivers//chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()  # to maximise the window

#TO FIND MULTIPLE WEB ELEMENTS
#to find how many elements/sliders (class ) with same name is present
sliders=driver.find_elements(By.CLASS_NAME,"homeslider-container")
#<li class="homeslider-container"
print(len(sliders))  # to print no of slides/web element present   #5

links=driver.find_elements(By.TAG_NAME,'a')
print(len(links))   #149   total no of links
"""

# CSS SELECTOR/ XPATH CANNOT BE DIRECTLY FIND IN HTML SO WE HAVE TO GENERATE TO USE IT   cascading style sheets
serv_obj=Service("C://Users//Reka//Drivers//chromedriver.exe")
d =webdriver.Chrome(service=serv_obj)
d.get("https://www.facebook.com/")
d.maximize_window()
#tag and id , tagname # value of id
#d.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
#tagname input is always optional , u can mention only id
#or
#d.find_element(By.CSS_SELECTOR,"#email").send_keys("abc")

#TAG AND CLASS COMBINATION  tagname.classvalue
#d.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc@gmail.com")
#or
#d.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abc@gmail.com")
#inputtext _55r1 _6luy  Unable to locate element: {"method":"css selector","selector":"input.inputtext _55r1 _6luy"}
# space in between inputtext and _55r1 is problem , as it may not take letters after space , its developers code
#so removing letters after inputtext

#tag and attribute COMBINATION   tagname[attribute=value]
#input[data-testid=royal_email]
#d.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("abcd")
#d.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("abcd")

#tag class attribute COMBINATION  tagname.valueofclass[attribute=value]
#if u have more than one  element with same tagname, class name and u want specifically 2 or any except first element
d.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys("abc@gmail.com")


