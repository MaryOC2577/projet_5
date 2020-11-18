"""Create database."""


import mysql.connector


class InitDatabase:
    """Initiate database."""

    mydb = mysql.connector.connect(
        host="localhost", user="root", password="Ma25Bo77Yi181"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES")

    # for x in mycursor:
    # if x == "aliment":
    # print("La base existe déjà.")
    # else:
    # mycursor.execute("CREATE DATABASE aliment")

    file = open(myscript, "r")
    mycursor.execute(file)
