"""Create database."""

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Ma25Bo77Yi181"
)

print(mydb)
