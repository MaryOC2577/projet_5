"""Class Product."""

from application.model.connection import connection
from application.model.nutriscore import Nutriscore


class Product:
    """Class product."""

    def __init__(self):
        """Initiate product class."""

    def get_id(self, name_product):
        """Returns the id according to the name."""
        cursor = connection.get_cursor()

        id_query = (
            "SELECT id FROM PRODUCT WHERE product_name ='%s'" % name_product
        )
        cursor.execute(id_query)
        product_id = cursor.fetchone()[0]

        connection.db.commit()
        cursor.close()
        return product_id

    @classmethod
    def save(cls, product: dict) -> int:
        """Save products in the database."""
        cursor = connection.get_cursor()
        nutri_score = Nutriscore()

        sql = (
            "INSERT IGNORE INTO PRODUCT "
            "(product_name, product_description, shop, substitute, nutri_id, product_url) "
            "VALUES (%(name)s, %(description)s, %(shop)s, "
            "%(substitute)s, %(nutri_id)s, %(url)s)"
        )

        data_products = {
            "name": product.get("name"),
            "description": product.get("description"),
            "shop": product.get("stores"),
            "substitute": None,
            "nutri_id": nutri_score.get_id(product.get("nutriscore")),
            "url": product.get("url"),
        }
        cursor.execute(sql, data_products)

        cursor.execute(
            "SELECT id, product_name FROM product WHERE product_name = %s",
            (product["name"],),
        )
        id = cursor.fetchone()[0]
        connection.db.commit()
        cursor.close()
        return id
