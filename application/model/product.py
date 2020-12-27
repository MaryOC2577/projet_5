"""Class Product."""

from application.model.connection import connection


class Product:
    """Class product."""

    def __init__(self):
        """Initiate product class."""

    @classmethod
    def save(cls, cleaned_product: list) -> bool:
        """Save products in the database."""
        cursor = connection.get_cursor()

        add_products = (
            "INSERT INTO PRODUCT (id, product_name, shop, origin, substitute) ",
            "VALUES (%(id)s, %(name)s, %(shop)s, %(origin)s, %(substitute)s) ",
        )

        for product in cleaned_product:
            data_products = {
                "id": None,
                "name": product.get("name"),
                "shop": product.get("stores"),
                "origin": product.get("origin"),
                "substitute": None,
            }
            cursor.execute(add_products, data_products)

        connection.db.commit()
        cursor.close()
        connection.close()
        return True
