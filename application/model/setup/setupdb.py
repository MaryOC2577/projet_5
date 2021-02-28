"""Create database."""


import mysql.connector
from config import SCRIPTSQL


class InitDatabase:
    """Initiate database."""

    def __init__(self):
        """Initialisze database."""
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ma25Bo77Yi181",
            # database="product",
        )

    def create_database(self):
        """Create the database."""
        mycursor = self.mydb.cursor()
        mycursor.execute("CREATE DATABASE product;")

    def use_database(self):
        """Use the database."""
        mycursor = self.mydb.cursor()
        mycursor.execute("USE product;")

    def setup_database(self):
        """Set the database."""
        mycursor = self.mydb.cursor()

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
        mycursor.close()


initbase = InitDatabase()
