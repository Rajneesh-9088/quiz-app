import mysql.connector
from os import system, name

score = 0

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="QUIZ"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM qdata1")
myresult = mycursor.fetchall()
_ = system('cls')
n = 0
for x in myresult:
    print("\t" * 3, "*" * 60)
    print("\t" * 5, "Welcome to Rajneesh Quiz Program")
    print("\t" * 3, "*" * 60)
    print("\t" * 3, "     Question", str(n + 1) + ".", x[1], "\n")
    print("\t" * 3, "     Option 1. ", x[2])
    print("\t" * 3, "     Option 2. ", x[3])
    print("\t" * 3, "     Option 3. ", x[4])
    print("\t" * 3, "     Option 4. ", x[5], "\n")
    print("\t" * 3, "*" * 60)
    print("\t" * 3, "  Enter your answer :", end="")
    ans = int(input())
    if (ans == x[6]):
        score += 1
    print("\n")
    _ = system('cls')
    n += 1
print("\t" * 3, "*" * 60)
print("\t" * 4, "   You have successfully completed the Quiz \n")
print("\t" * 5, "   Your score is :", score, "/", n)
input("Press any key to Exit")
_ = system('cls')
