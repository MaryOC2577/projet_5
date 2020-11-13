""" Create database """

import mysql.connector

class database :

    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ma25Bo77Yi181"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
        print(x)