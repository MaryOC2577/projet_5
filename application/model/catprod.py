"""Class Catprod."""

from application.model.connection import connection
from application.model.product import Product
from application.model.category import Category


class CatProd:
    """Class Catprod."""

    def __init__(self):
        """"Initialize catprod class."""

    @classmethod
    def save(cls, id_prod, ids_cat: list) -> bool:
        """Save Catprod in the database."""
        cursor = connection.get_cursor()

        sql = (
            "INSERT INTO CATPROD (id_cat, id_prod) "
            "VALUES (%(id_cat)s, %(id_prod)s)"
        )

        for id in ids_cat:
            data_catprod = {
                "id_cat": id,
                "id_prod": id_prod,
            }
            cursor.execute(sql, data_catprod)

        connection.db.commit()
        cursor.close()
