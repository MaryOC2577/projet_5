"""Class connection."""

import mysql.connector


class Connection:
    """Class connection."""

    def __init__(self):
        """Initialize."""
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ma25Bo77Yi181",
            database="product",
        )

    def get_cursor(self):
        """Connect to database."""
        return self.db.cursor()

    def close(self):
        """Close the connection."""
        self.db.close()


connection = Connection()
