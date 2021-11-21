import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="QUIZ"
)

mycursor = mydb.cursor()
qid = input("Enter the qid to delete: ")

sql = "DELETE FROM qdata1 WHERE qid = %s"
val = (qid,)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record deleted")
