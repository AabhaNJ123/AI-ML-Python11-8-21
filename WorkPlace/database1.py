# import mysql.connector
# myconn=mysql.connector.connect(host="localhost",user="root",password="")
# print("\nDatabase connection established : ",myconn)
# cur=myconn.cursor()
# print("Cursor : ",cur)

import mysql.connector
# mydb=mysql.connector.connect(host="localhost",user="root",password="")
# mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE student")

mydb=mysql.connector.connect(host="localhost",user="root",password="",database="student")
mycursor=mydb.cursor()
# mycursor.execute("CREATE TABLE students(name VARCHAR(50),address VARCHAR(100))")

mycursor=mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

