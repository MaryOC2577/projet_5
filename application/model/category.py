"""Class Category."""

from application.model.connection import connection


class Category:
    """Class Category."""

    def __init__(self):
        """Initiate category class."""

    def get_name(self, product_id):
        """Return category name according to the product id."""
        cursor = connection.get_cursor()

        sql = (
            "SELECT cat_name FROM category "
            "INNER JOIN catprod ON catprod.id_cat = category.id "
            "INNER JOIN product ON product.id = catprod.id_prod "
            f"WHERE PRODUCT.id = {product_id}"
        )
        cursor.execute(sql)
        category_name = cursor.fetchone()[0]

        connection.db.commit()
        cursor.close()
        return category_name

    def get_id(self, name_category):
        """Return the id according to the name."""
        cursor = connection.get_cursor()

        sql = f"SELECT id FROM CATEGORY WHERE cat_name ='{name_category}'"
        cursor.execute(sql)
        category_id = cursor.fetchone()[0]

        connection.db.commit()
        cursor.close()
        return category_id

    def get_all(self):
        """Return id and name of all categories."""
        cursor = connection.get_cursor()

        sql = "SELECT id, cat_name FROM CATEGORY"

        cursor.execute(sql)
        cat_list = cursor.fetchone()
        connection.db.commit()
        cursor.close()
        return cat_list

    @classmethod
    def save(cls, categories: list) -> list:
        """Save categories in the database."""
        cursor = connection.get_cursor()

        sql = "INSERT IGNORE INTO CATEGORY (cat_name) VALUES (%s)"

        for name in categories:
            data_categories = (name,)
            cursor.execute(sql, data_categories)

        connection.db.commit()
        category_ids = []

        for name in categories:
            cursor.execute(
                "SELECT id, cat_name FROM category WHERE cat_name = %s ",
                (name,),
            )
            id = cursor.fetchone()[0]
            category_ids.append(id)
            # try:

            # except TypeError as error:
            #    breakpoint()

        cursor.close()
        return category_ids
