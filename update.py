import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="QUIZ"
)

mycursor = mydb.cursor()

qid = input("Enter Qid: ")
sql = "SELECT * from  qdata1 where qid=%s"
val = (qid,)
mycursor.execute(sql, val)

myresult = mycursor.fetchall()
for x in myresult:
    oq = x[1]
    oa1 = x[2]
    oa2 = x[3]
    oa3 = x[4]
    oa4 = x[5]
    oca = x[6]
print(oq, ",", oa1, ",", oa2, ",", oa3, ",", oa4, ",", oca)
q = input("Enter Question: ")
a1 = input("Enter option1: ")
a2 = input("Enter option2: ")
a3 = input("Enter option3: ")
a4 = input("Enter option4: ")
ca = input("Enter currect answer: ")

if (q == ""):
    q = oq
if (a1 == ""):
    a1 = oa1
if (a2 == ""):
    a2 = oa2
if (a3 == ""):
    a3 = oa3
if (a4 == ""):
    a4 = oa4
if (ca == ""):
    ca = oca

sql = "UPDATE qdata1 SET question=%s, option1=%s,option2=%s,option3=%s,option4=%s, cans=%s WHERE qid=%s"

val = (q, a1, a2, a3, a4, ca, qid)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record updated")
