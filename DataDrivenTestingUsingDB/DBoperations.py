# insert, update, delete
import mysql.connector
"""
# establish connection to DB
#connect method to connect to DB based on connection details we provide    con is connectionobject
con=mysql.connector.connect(host="localhost",port=3306,user="root",passwd="root",database="mydb")
# create stmt/query to execute through this conection, we cannot do that directly
# we have to create cursor , which is basically a buffer area(temporary memory)
# with connection create cursor , through cursor we execute the stmt
curs=con.cursor()   # create cursor
curs.execute("insert into student values(107,'NV',90)")  # execute query through cursor
con.commit()    # commit transaction
con.close()
print("Finished")
"""
"""
insert_query="insert into student values(107,'NV',90)"
update_query="update student set sname='Vasantha' where sno=106"
delete_query="delete from student where sno=107"
con=mysql.connector.connect(host="localhost",port=3306,user="root",passwd="root",database="mydb")
curs=con.cursor()
curs.execute(delete_query)
con.commit()
con.close()
print("finsihed")
"""
# if DB is down, not available and restarting,line 19 will throw exception when connecting to DB"connection error
# when down , program should display message connection is unsuccessful/db is down
# if no connection it should give exit my code without giving error
#EXCEPTTION HANDLING
delete_query="delete from student where sno=107"
try:
    con=mysql.connector.connect(host="localhost",port=3307,user="root",passwd="root",database="mydb")
    curs=con.cursor()
    curs.execute(delete_query)
    con.commit()
    con.close()
except:  # dont need to specify ,as except block will handle all kind of exception
    print("connection unsuccessfull...")
print("finsihed")