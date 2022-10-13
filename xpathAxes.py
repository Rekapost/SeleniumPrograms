from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service('C://Users//Reka//Drivers//chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

# self keyword:  from which elemnet u want to navigate
text_msg=driver.find_element(By.XPATH, "//a[contains(text(),'Indian Bank')]/self::a").text
#text will copy the text  element ,  "//a[contains(text(),'Indian Bank')]  this is self node
#text method, whatever element this satement is identified,
# from that element it will capture the text from this element and store it in variable
print("self web element/node:",text_msg)   #Indian Bank

#parent node : want to capture parent node (td) of the self node (a)
text_msg=driver.find_element(By.XPATH, "//a[contains(text(),'Indian Bank')]/parent::td").text
print("parent of self a:",text_msg)     #Indian Bank  since parent has no text  , it takes selfs text Indian Bank
#for single web element we can capture text

#child element : since 'a' does not have child element , we can go to ancestor of 'a' (tr) and
# find the child (td) of ancestor (tr)   , capturing all the child tags of ancestor
#for multiple child use elements, for multiple webelement we cant capture text, it will list all the childs
childs=driver.find_elements(By.XPATH, "//a[contains(text(),'Indian Bank')]/ancestor::tr/child::td")
print("no of childs for the ancestor tr:",len(childs))   # to count no of  childs ie actually no of web elements    #  5

#ancestor:
text_msg=driver.find_element(By.XPATH, "//a[contains(text(),'Indian Bank')]/ancestor::tr").text
print("ancestor of self:",text_msg)   #Indian Bank A 168.15 174.85 + 3.98
# it prints all the text of the ancestor row

# descendant:  since parent (td) does not have grandchild/descendant ,
# we can go to ancestor (tr) and find the descendant/grandchilds of ancestor (tr)
descendants=driver.find_elements(By.XPATH, "//a[contains(text(),'Indian Bank')]/ancestor::tr/descendant::*")
print("no of descendants for ancestor tr:",len(descendants))    #7
# since we dont know the descendant we can put * as it will show all descendant of ancestor tr

#following nodes:
followings=driver.find_elements(By.XPATH, "//a[contains(text(),'Indian Bank')]/ancestor::tr/following::*")
print("no of followings for the ancestor:",len(followings))   #1687

#following sibling:   it will be subset of 1687
followingsiblings=driver.find_elements(By.XPATH, "//a[contains(text(),'Indian Bank')]/ancestor::tr/following-sibling::*")
print("no of following siblings for the ancestor:",len(followingsiblings))  #  191
# if u want only followings which have tr tag
followingsiblings=driver.find_elements(By.XPATH, "//a[contains(text(),'Indian Bank')]/ancestor::tr/following-sibling::tr")
print("no of following siblings for the ancestor having tr element:",len(followingsiblings))   #191

#preceding node:
precedings =driver.find_elements(By.XPATH, "//a[contains(text(),'Indian Bank')]/ancestor::tr/preceding::*")
print("no of precedings for the ancestor:",len(precedings))    #258

#preceding siblings:
precedingsiblings =driver.find_elements(By.XPATH, "//a[contains(text(),'Indian Bank')]/ancestor::tr/preceding-sibling::*")
print("no of preceding siblings for the ancestor:",len(precedingsiblings))   # 13
# if u want only preceding which have tr tag
precedingsiblings =driver.find_elements(By.XPATH, "//a[contains(text(),'Indian Bank')]/ancestor::tr/preceding-sibling::tr")
print("no of preceding siblings for the ancestor having only  tr :",len(precedingsiblings))    #13
"""
self web element/node: Indian Bank
parent of self a: Indian Bank
no of childs for the ancestor tr: 5
ancestor of self: Indian Bank A 168.15 174.85 + 3.98
no of descendants for ancestor tr: 7
no of followings for the ancestor: 1692
no of following siblings for the ancestor: 191
no of following siblings for the ancestor having tr element: 191
no of precedings for the ancestor: 278
no of preceding siblings for the ancestor: 13
no of preceding siblings for the ancestor tr : 13"""
