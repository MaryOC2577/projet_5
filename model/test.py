"""Test."""

import mysql.connector

# from config import SCRIPTSQL


mydb = mysql.connector.connect(
    host="localhost", user="root", password="Ma25Bo77Yi181"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE product")

fd = open("scriptsql.sql", "r")
sqlFile = fd.read()
sqlCommands = sqlFile.split(";")
for command in sqlCommands:
    try:
        if command.strip() != "":
            mycursor.execute(command)
    except IOError as msg:
        msg = "Command skipped"
        print(msg)
