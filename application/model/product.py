"""Class Product."""

# import mysql.connector
from application.model.connection import Connection


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
        Connection.set.mycursor.execute("SELECT * FORM Product;")

    def get(self):
        """Get a product."""

    def create(self):
        """Create a product."""
        Connection.set.mycursor.execute(
            "INSERT INTO TABLE Product VALUES("
            + id
            + ", "
            + product_name
            + ", "
            + shop
            + ", "
            + origin
            + ", "
            + substitute
            + ", "
            + nutriscore
            + ")"
        )

    def update(self):
        """Update a product."""

    def delete(self):
        """Delete a product."""

    @classmethod
    def save(cls, cleaned_product: dict) -> bool:
        mycursor = Connection()
        mycursor.get_cursor()
        mycursor.execute("INSERT INTO TABLE PRODUCT VALUES" + )
        mycursor.close()
        return true
