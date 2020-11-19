"""Create database."""


import mysql.connector
from projet_5.config import SCRIPTSQL


class InitDatabase:
    """Initiate database."""

    mydb = mysql.connector.connect(
        host="localhost", user="root", password="Ma25Bo77Yi181"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
        print(x)
    # if x == "aliment":
    # print("La base existe déjà.")
    # else:
    # mycursor.execute("CREATE DATABASE aliment")

    # file = open(SCRIPTSQL, "r")
    # mycursor.execute(file)
