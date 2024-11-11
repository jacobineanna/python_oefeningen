import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",  #port erbij indien mac
  user="root",
  password="",
  database="oefen_database"
)


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM hp_characters")

myresult = mycursor.fetchall()

for x in myresult:
    if x[5] == "None":
        print(x[1] + " is verliefd op niemand")
    else:
        print(x[1] + " is verliefd op " + x[5])

var_voornaam = input("vul voornaam in ")
var_achternaam = input("vul achternaam in ")
sql = "INSERT INTO hp_characters (voornaam, achternaam) VALUES (%s, %s)"
val = (var_voornaam,var_achternaam)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")