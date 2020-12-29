"""Class Product."""

from application.model.connection import connection


class Product:
    """Class product."""

    def __init__(self):
        """Initiate product class."""

    def id_product(self, name_product):
        """Returns the id according to the name."""
        cursor = connection.get_cursor()
        id_temp = int

        id_query = (
            "SELECT id FROM PRODUCT WHERE product_name ='%(name_product)s'"
        )

        cursor.execute(id_query, name_product)

        for id in cursor:
            id_temp = id
        cursor.close()

        connection.db.commit()
        cursor.close()
        return id_temp

    @classmethod
    def save(cls, cleaned_product: list) -> bool:
        """Save products in the database."""
        cursor = connection.get_cursor()

        add_products = (
            "INSERT INTO PRODUCT (id, product_name, shop, origin, substitute) "
            "VALUES (%(id)s, %(name)s, %(shop)s, %(origin)s, %(substitute)s)"
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
        return True
