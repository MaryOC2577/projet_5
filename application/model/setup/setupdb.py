"""Create database."""


import mysql.connector
from config import SCRIPTSQL


class InitDatabase:
    """Initiate database."""

    def setup_database(self):
        """Set the database."""
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ma25Bo77Yi181",
            database="product",
        )
        mycursor = mydb.cursor()
        # mycursor.execute("CREATE DATABASE product")
        # mycursor.execute("USE DATABASE product")

        fd = open(SCRIPTSQL, "r")
        sqlFile = fd.read()
        sqlCommands = sqlFile.split(";")
        for command in sqlCommands:
            try:
                if command.strip() != "":
                    mycursor.execute(command)
            except IOError as msg:
                msg = "Command skipped"
                print(msg)


initbase = InitDatabase()
