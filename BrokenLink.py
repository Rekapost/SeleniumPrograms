# we need to install requests package for brokenlink
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.chrome.service import Service
import requests as requests

serv_obj=Service('C://Users//Reka//Drivers//chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://deadlinkcity.com/")
driver.maximize_window()

links=driver.find_elements(By.TAG_NAME,'a')
print(len(links))   #48
count=0
for link in links:  # to read each link
    url=link.get_attribute('href')  # capture href value, it gives url
    try:   # network related exception may come when working bet client and server
        res=requests.head(url) # hit this url to server in the backend and server will respond ,
                               # store that respond in res, head is method
    except:
        None
    if res.status_code>=400:
        print(url, ": it is broken link")
        count=count+1
    else:
        print(url,":it is valid link")

print("Total no of broken links:", count)  #40

