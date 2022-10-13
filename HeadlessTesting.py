from selenium import webdriver

def headless_chrome():
    from selenium .webdriver.chrome.service import Service
    serv_obj=Service('C://Users//Reka//Drivers//chromedriver.exe')
    #before specifiying driver, we have to use chromeoptions Class
    ops=webdriver.ChromeOptions()
    ops.headless=True
    driver = webdriver.Chrome(service=serv_obj,options=ops)   # this makes headless
    return driver
driverobj=headless_chrome()
driverobj.get("https://demo.nopcommerce.com/")
driverobj.maximize_window()
print(driverobj.title)
print(driverobj.current_url)
driverobj.close()