import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="QUIZ"
)

mycursor = mydb.cursor()

n = input("Enter Name: ")
u = input("Enter Username:  ")
p = input("Enter Password:  ")

sql = 'INSERT into user (name,username, password) VALUES(%s,%s,%s)'
val = (n, u, p)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted")
