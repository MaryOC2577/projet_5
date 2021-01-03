"""Class Catprod."""

from application.model.connection import connection
from application.model.product import Product
from application.model.category import Category


class CatProd:
    """Class Catprod."""

    def __init__(self):
        """"Initialize catprod class."""

    @classmethod
    def save(cls, cleaned_product: list) -> bool:
        """Save Catprod in the database."""
        cursor = connection.get_cursor()

        temp_prod = []
        productclass = Product()
        catclass = Category()

        add_catprod = (
            "INSERT INTO CATPROD (id_cat, id_prod) "
            "VALUES (%(id_cat)s, %(id_prod)s)"
        )

        for product in cleaned_product:
            for category in product.get("categories"):
                select_product = {
                    "prod_name": product.get("name"),
                    "cat_name": category,
                }
            temp_prod.append(select_product)

        for product in temp_prod:
            data_catprod = {
                "id_cat": catclass.get_idcategory(product.get("cat_name")),
                "id_prod": productclass.get_idproduct(product.get("prod_name")),
            }

            cursor.execute(add_catprod, data_catprod)

        connection.db.commit()
        cursor.close()
