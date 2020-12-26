"""Class Product."""

from application.model.connection import connection


class Product:
    """Class product."""

    def __init__(self):
        """Initiate product class."""

    @classmethod
    def save(cls, cleaned_product: dict) -> bool:
        """Save products in the database."""
        cursor = connection.get_cursor()

        add_nutriscore = (
            "INSERT INTO NUTRISCORE (id, nutri_value) VALUES (%s, %s)"
        )
        add_categories = (
            "INSERT INTO CATEGORY (id, cat_name) VALUES (%(id)s, %(name)s)"
        )
        add_products = "INSERT INTO PRODUCT (id, product_name, shop, origin, substitute) VALUES (%(id)s, %(name)s, %(shop)s, %(origin)s, %(substitute)s)"
        add_catprod = "INSERT INTO CATPROD (id_cat, id_prod) VALUES (%s, %s)"

        for _, product in cleaned_product.items():

            data_categories = {"id": None, "name": product[3]}

            data_products = {
                "id": None,
                "name": product[0],
                "shop": product[1],
                "origin": product[2],
                "substitute": None,
            }

            # cursor.execute(add_nutriscore, data_nutriscore)
            cursor.execute(add_categories, data_categories)
            cursor.execute(add_products, data_products)
            # cursor.execute(add_catprod)

        connection.db.commit()
        cursor.close()
        connection.close()
        return True
