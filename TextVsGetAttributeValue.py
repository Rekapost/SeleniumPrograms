#<label for="RememberMe" xpath="1">Remember me?</label>
#Remember me?  ===> inner text

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #importing by class from module

serv_obj=Service('C://Users//Reka//Drivers//chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()

# email login box
#<input class="email valid" value="admin@yourstore.com" autofocus="autofocus" type="email" data-val="true" data-val-email="Wrong email" data-val-required="Please enter your email"
#id="Email" name="Email" aria-describedby="Email-error" aria-invalid="false" style="" xpath="1">
"""
enteremail=driver.find_element(By.ID,"Email")
print("login email already present defaultly: ",enteremail.get_attribute('value'))  #admin@yourstore.com
enteremail.clear()
enteremail.send_keys("abc@gmail.com")
print("inner text :",enteremail.text)    # it returns nothing as it does not have inner text
print("new email added after clearing default email:",enteremail.get_attribute('value'))   # it returns abc@gmail.com
"""

#login button
#<button type="submit" class="button-1 login-button" xpath="1">Log in</button>
login_button=driver.find_element(By.TAG_NAME,"button")
#login_button.click()
print(login_button.text)   #  LOG IN
print(login_button.get_attribute('type'))   #submit
print("result of get_attribute:",login_button.get_attribute('value'))   #         nothing as no attribute value