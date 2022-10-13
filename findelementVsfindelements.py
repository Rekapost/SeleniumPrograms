from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.chrome.service import Service

serv_obj=Service('C://Users//Reka//Drivers//chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
"""
#---------------------find_element---------------------    ===> returns single webelement
#1. locators matching with single webelement
singlelement=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
singlelement.send_keys("MAC BOOK")

# 2.locators matching with Multiple webelements
#a.footer is one element, inside footer many links  , //a directly jump to anchor tags
#b.footer to anchor tags, 23 anchor tags links are identified, each link is webelement,this xpath links 
#to multiple webelements

#c.locator shows multiple elements but find_element gives single element , the first element, 
#only one webelment will be wriiten
element=driver.find_element(By.XPATH,"//div[@class='footer']//a")

#capture the text of the element
print (element.text)   # Sitemap , it prints only one webelement
# we are printing the text of the element ,
#element.txt()  it is calling the element object, u cant print object, we have to call object from class, method

# 3.if element is not found , it will throw exception "NoSuchElementEception"
log_in=driver.find_element(By.LINK_TEXT,"Log in")
log_in.click()
log_in=driver.find_element(By.LINK_TEXT,"Log ")   # exception error
log_in.click()
"""
#------------------find elements-------------------------=====> return multiple web elements
#1. locators matching with single webelement
#input[@id='small-searchterms']==>locator is matching single web element(search box),
# but we have find_elemnets so it will return that single webelemnet, as list collection and not as webelement,
#  that single webelement will be apppeared as one of the item in the list, since elements we cant access send_keys,
"""
singlelements=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
print(len(singlelements))  # 1 element count how many items are in the list (extracted the element )

# how to capture that element
singlelements[0].send_keys("MAC BOOK")  # it is first place index 0 ,
# accessing the first element in the list ,(extracted the element and sending keys)"""

# 2.locators matching with Multiple webelements
"""
elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
print(len(elements))    #23
print(elements[0].text)   # print 1st element text value in 23 elements   #Sitemap
print(elements[10].text)   #  Compare products list
print(elements[21].text)  #YouTube
# to capture the text value of every element captured in elements=  we need to write loop statement
for ele in elements:
    print(ele.text)  # it prints text of all 23 elements"""
#text ===>it gives the value of the element

#3.if element is not found , it will not throw exception "NoSuchElementEception"
# it will not throw any exception , by default list has 0
log_in=driver.find_elements(By.LINK_TEXT,"Log in")
print("elements returned:",len(log_in))   # 1
# element not available , it will return 0
log_in=driver.find_elements(By.LINK_TEXT,"Log ")
print("elements returned:",len(log_in))   # 0     lenth of elemnet is 0, list contains 0 elements