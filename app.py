from flask import Flask
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/schip_aanmaken/<schipnaam>/<thuishaven>/<lengte_schip>")
def hello_world(schipnaam, thuishaven, lengte_schip):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="haven_db"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM schip")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    # Naam = input("naam schip: ")
    # Thuishaven = input("Thuishaven: ")
    # Lengte_Schip = input("Lengte van schip: ")
    sql = "INSERT INTO schip (Naam, Thuishaven, Lengte_Schip) VALUES (%s, %s, %s)"
    # val = (Naam, Thuishaven, Lengte_Schip)
    val = (schipnaam, thuishaven, lengte_schip)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

    # query = ("SELECT Naam, Thuishaven, Lengte_Schip FROM schip"
    #    "WHERE "
    # )

    return "<p>Hello, World!</p>"

@app.route("/toon_alle_schepen")
def toon_alle_schepen():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="haven_db"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM schip")

    myresult = mycursor.fetchall()
    print(myresult)

    keys = [i[0] for i in mycursor.description]

    data = [
        dict(zip(keys, row)) for row in myresult
    ]
    return data





