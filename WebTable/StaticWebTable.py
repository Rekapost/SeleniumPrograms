from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj=Service("C://Users//Reka//Drivers//chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1.how to count no of rows and columns from the table
# capture all tr from table and count no of rows
noOfRows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
print("no of rows including header:",noOfRows)   #7

# 2.capture all the headers which shows no of coulmns from table and count no of columns
#in first tr , th header is there, if we count header ,it will show no of coulmns
noOfColumns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print("no of columns is no of header:",noOfColumns)   #4
"""
# 3. stataiccally Read value from specific row and column data
# capture (master in selenium) in 5th row and column 1
row5column1data=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]").text  # (text) to capture text
print(row5column1data)
"""
"""
#4. Dynamically Read all Rows  r and all columns c
# write loop statement , know no of rows and coulmns and
# write 2 loop statemnet one for incrementing row ad another for incrementing column
# each row has multiple columns, go to first row , read all columns
for r in range (2,noOfRows+1):
    for c in range(1,noOfColumns+1):
        allRowsAllColumns=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
        # dynamically adding values to tr and td is called parameterising data into XPATH
        # passing paramters or arguments into XPATH, then XPATH becomes dynamic XPATH
        # inject r and c into the XPATH  (tr[r]/td[c]) ,but  r and c are varaiables , u cant specify in the index
        # xpath cannot takes variables
        # so u have to follow syntax tr["+str(r)+"]/td["+str(c)+"]
#       print(allRowsAllColumns)
        print(allRowsAllColumns,end=' ')
        # to print all coulumn data in single row (side by side)
    print()   # to print set by set
"""
# 5. read data based on the condition(list books name whose author is mukesh)
# author column is first column and bookname is second column , only 2 column needed
for r in range (2,noOfRows+1):    # td[2] author column , same row
    getAuthorMukesh=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    #td[2] author shows columns , tr[] selects each row in that td[2] column
    #column no td is same(constant) , by changing row no , we can compare each author in row to mukesh
    if getAuthorMukesh=="Mukesh":
        # If author name is Mukesh , capture the book name which is in the same row  td[1] column book name
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        # also getting the price of the book , if author name is mukesh   price coulumn is td[4]
        bookprice = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td[4]").text

        print(bookName,"   ",bookprice,"       " ,getAuthorMukesh)

driver.close()