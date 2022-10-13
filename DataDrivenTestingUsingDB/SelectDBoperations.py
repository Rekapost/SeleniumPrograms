# select
import mysql.connector

con=mysql.connector.connect(host="localhost",port=3306,user="root",passwd="root",database="mydb")
curs=con.cursor()
curs.execute("select * from student")  # select cmd will return value which will be stored in cursor ,
# we dont how many data it is going to return , use loop to get data from cursor
for row in curs: # from cursor get first row and store
    print(row[0],row[1],row[2])
con.close()
print("finsihed")

"""
# if DB is down, not available and restarting,line 19 will throw exception when connecting to DB"connection error
# when down , program should display message connection is unsuccessful/db is down
# if no connection it should give exit my code without giving error
#EXCEPTTION HANDLING
try:
    con=mysql.connector.connect(host="localhost",port=3307,user="root",passwd="root",database="mydb")
    curs=con.cursor()
    curs.execute("select * from student")
    for row in curs: # from cursor get first row and store
        print(row[0],row[1],row[2])
    con.close()
except:  # dont need to specify ,as except block will handle all kind of exception
    print("connection unsuccessfull...")
print("finsihed")
"""