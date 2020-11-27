"""Class connection."""

import mysql.connector


class Connection:
    """Class connection."""

    def set(self):
        """Connect to database."""
        cnx = mysql.connector.connect(
            host="localhost", user="root", password="Ma25Bo77Yi181"
        )
        mycursor = cnx.cursor()

    def close(self):
        """Close the connection."""
        cnx.close