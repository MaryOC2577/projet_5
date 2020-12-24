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
        self.mycursor = Connection()

    def listp(self):
        """ a product."""
        # Connection.set.mycursor.execute("SELECT * FORM Product;")

    def get(self):
        """Get a product."""

    def create(self):
        """Create a product."""

    def update(self):
        """Update a product."""

    def delete(self):
        """Delete a product."""

    def save(self, cleaned_product: dict) -> bool:
        """Save products in the database."""
        cursor = self.mycursor.get_cursor()

        add_categories = "INSERT INTO CATEGORY (id, cat_name) VALUES (%s, %s);"

        # add_catprod = "INSERT INTO CATPROD (id_cat, id_prod) VALUES (%s, %s);"

        for key, value in cleaned_product.items():
            cursor.execute(add_categories, key, value)
        cursor.close()
        return True
