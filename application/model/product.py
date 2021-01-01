"""Class Product."""

from application.model.connection import connection
from application.model.nutriscore import Nutriscore


class Product:
    """Class product."""

    def __init__(self):
        """Initiate product class."""

    def get_idproduct(self, name_product):
        """Returns the id according to the name."""
        cursor = connection.get_cursor()

        id_query = (
            "SELECT id FROM PRODUCT WHERE product_name ='%(name_product)s'"
        )

        cursor.execute(id_query, name_product)
        product_id = cursor.fetchone()

        connection.db.commit()
        cursor.close()
        return product_id

    @classmethod
    def save(cls, cleaned_product: list) -> bool:
        """Save products in the database."""
        cursor = connection.get_cursor()
        nutri_score = Nutriscore()

        add_products = (
            "INSERT INTO PRODUCT (id, product_name, shop, origin, substitute, nutri_id) "
            "VALUES (%(id)s, %(name)s, %(shop)s, %(origin)s, %(substitute)s, %(nutri_id)s)"
        )

        for product in cleaned_product:
            data_products = {
                "id": None,
                "name": product.get("name"),
                "shop": product.get("stores"),
                "origin": product.get("origin"),
                "substitute": None,
                "nutri_id": nutri_score.get_idnutriscore(
                    product.get("nutriscore")
                ),
            }
            cursor.execute(add_products, data_products)

        connection.db.commit()
        cursor.close()
        return True
