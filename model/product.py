"""Class Product."""

import mysql.connector
from create import InitDatabase


class Product:
    """Class product."""

    def __init__(self):
        """Initiate product class."""
        id = int
        name = ""
        shop = ""
        origin = ""
        substitute = ""
        nutriscore = ""

    def listp(self):
        """Add a product."""
        InitDatabase.set_connection.mycursor.execute("SELECT * FORM Product;")

    def get(self):
        """Get a product."""

    def create(self):
        """Create a product."""
        mydb = mysql.connector.connect(
            host="localhost", user="root", password="Ma25Bo77Yi181"
        )
        mycursor = mydb.cursor()
        mycursor.execute(
            "INSERT INTO TABLE Product VALUES("
            + id
            + ", "
            + product_name
            + ", "
            + shop
            + ", "
            + origin
            + ", "
            + substitue
            + ", "
            + nutriscore
            + ")"
        )

    def update(self):
        """Update a product."""

    def delete(self):
        """Delete a product."""
