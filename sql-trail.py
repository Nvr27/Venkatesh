import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="9989860557",
    database="world"
)

# mycursor = mydb.cursor()
#
# mycursor.execute("SELECT * FROM city")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)
