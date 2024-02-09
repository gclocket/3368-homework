import creds
import sql
from sql import create_connection
from sql import execute_read_query
from sql import execute_update_query
import mysql.connector

mycreds = creds.creds()

myconn = create_connection(mycreds.myhostname, mycreds.uname, mycreds.passwd, mycreds.dbname)

mysqlst = "select * from users"
print("hello")
userlist = execute_read_query(myconn, mysql)

print(userlist)
for eachuser in userlist:
    print(eachuser)

# inserting data into DB
mysqlst = "insert into users(firstname, lastname, email) values ('Zahabiya', 'Khandwawala', 'zahabiya10@gmail.com'))"
execute_update_query(myconn, mysqlst)

# updating data in DB
mysqlst = " update users set firstname='Zai', lastname='K' where id=3"
execute_update_query(myconn, mysqlst)

# Deleting Data From DB
uid = 4
mysqlst = "delete from users where id=%s" %(uid)
execute_update_query(myconn,mysqlst)