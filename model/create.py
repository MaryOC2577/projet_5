"""Create database."""


import mysql.connector


class InitDatabase:
    """Initiate database."""

    def __init__(self):
        """Create database."""
        mydb = mysql.connector.connect(
            host="localhost", user="root", password="Ma25Bo77Yi181"
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE product")

    def executeScriptsFromFile(self, filename):
        fd = open(filename, "r")
        sqlFile = fd.read()
        sqlCommands = sqlFile.split(";")
        for command in sqlCommands:
            try:
                if command.strip() != "":
                    cursor.execute(command)
            except IOError as msg:
                print("Command skipped: "), msg
