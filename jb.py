# import to connect to DB
import mysql.connector
from mysql.connector import Error

# create the connection to the DB as shown in class
def create_connection(hostname, uid, pwd, dbname):
    conn = None
    try:
        conn = mysql.connector.connect(
            host = hostname,
            user = uid,
            password = pwd,
            database = dbname
        )
    except Error as e:
        print("Error is ", e)
    return conn

# create cursor to get DB info as shown in class
myconn = create_connection('db3368.c1o8w68m4pjb.us-east-1.rds.amazonaws.com','admin','1963711!', 'db3368')
mycursor = myconn.cursor(dictionary=True)

mycursor.execute("select * from boardgame")
bgamelst = mycursor.fetchall()

print(bgamelst)
for eachuser in bgamelst:
    print(eachuser)