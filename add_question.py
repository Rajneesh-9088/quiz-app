import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="QUIZ"
)

q = input("Enter question: ")
a1 = input("Enter option1: ")
a2 = input("Enter option2: ")
a3 = input("Enter option3: ")
a4 = input("Enter option4: ")
cans = input("Enter correct answer: ")

mycursor = mydb.cursor()

sql = 'INSERT into qdata1 (question,option1,option2,option3,option4,cans) VALUES(%s,%s,%s,%s,%s,%s)'
val = (q, a1, a2, a3, a4, cans)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted")
