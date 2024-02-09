import mysql.connector
from mysql.connector import Error

def create_connection(hostname, uid, pwd, dbname):
    conn = None
    try:
        conn = mysql.connector.connect(
            host = hostname,
            user = uid,
            password = pwd,
            database = dbname
        )
        print("DB created successfully")
    except Error as e:
        print("Error is ", e)
    return conn

# this function is a generic read function to get data from DB (select)
def execute_read_query(myconn, sql):
    rows = None
    mycursor = myconn.cursor(dictionary=True)
    try:

        mycursor.execute(sql)
        rows = mycursor.fetchall()
        return rows
    except Error as e:
        print("Error is ", e)

# this function is a generic update function to update data into DB (insert, update)
def execute_update_query(myconn, sql):

    mycursor = myconn.cursor(dictionary=True)
    try:

        mycursor.execute(sql)
        myconn.commit()
        print("Query executed successfully")
    except Error as e:
        print("Error is ", e)