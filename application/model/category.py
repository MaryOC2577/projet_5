"""Class Category."""

from application.model.connection import connection


class Category:
    """Class Category."""

    def __init__(self):
        """Initiate category class."""

    def id_category(self, name_category):
        """Returns the id according to the name."""
        cursor = connection.get_cursor()
        id_temp = int

        id_query = (
            "SELECT id FROM CATEGORY WHERE cat_name = '%(name_category)s'"
        )

        cursor.execute(id_query, name_category)

        for id in cursor:
            id_temp = id
        cursor.close()

        connection.db.commit()
        cursor.close()
        return id_temp

    @classmethod
    def save(cls, cleaned_product: list) -> bool:
        """Save categories in the database."""
        cursor = connection.get_cursor()

        add_categories = (
            "INSERT INTO CATEGORY (id, cat_name) VALUES (%(id)s, %(name)s)"
        )

        for product in cleaned_product:
            for cat_value in product.get("categories"):
                data_categories = {
                    "id": None,
                    "name": cat_value.replace("fr:", ""),
                }
                cursor.execute(add_categories, data_categories)

        connection.db.commit()
        cursor.close()
        return True
