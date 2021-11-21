import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="QUIZ"
)

mycursor = mydb.cursor()

sql = "CREATE TABLE qdata1 (qid int(5) NOT NULL AUTO_INCREMENT, question VARCHAR (500) NOT NULL  , option1 VARCHAR(250) NOT NULL, option2 VARCHAR(250) NOT NULL, option3 VARCHAR(250) NOT NULL,option4 VARCHAR(250) NOT NULL, cans int(1) NOT NULL,PRIMARY KEY(qid))"

mycursor.execute(sql)

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
