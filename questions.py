import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="QUIZ"
)

mycursor = mydb.cursor()

sql = "CREATE TABLE qdata (qid int(5) NOT NULL, question VARCHAR (150) NOT NULL, option1 VARCHAR(150) NOT NULL, option2 VARCHAR(150) NOT NULL, option3 VARCHAR(150) NOT NULL,option4 VARCHAR(150) NOT NULL, cans int(1) NOT NULL)"

mycursor.execute(sql)

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
