import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="QUIZ"
)

mycursor = mydb.cursor()

sql = "CREATE TABLE admin(userid int(5) NOT NULL AUTO_INCREMENT, name VARCHAR(100) NOT NULL, username VARCHAR(100) NOT NULL, password VARCHAR(100) NOT NULL, PRIMARY KEY(userid))"

mycursor.execute(sql)
mycursor.execute("SHOW TABLES")
