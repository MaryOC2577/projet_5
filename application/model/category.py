"""Class Category."""

from application.model.connection import connection


class Category:
    """Class Category."""

    def __init__(self):
        """Initiate category class."""

    def get_idcategory(self, name_category):
        """Return the id according to the name."""
        cursor = connection.get_cursor()

        id_query = (
            "SELECT id FROM CATEGORY WHERE cat_name ='%s'" % name_category
        )

        cursor.execute(id_query)
        category_id = cursor.fetchone()[0]

        connection.db.commit()
        cursor.close()
        return category_id

    @classmethod
    def save(cls, categories: list) -> list:
        """Save categories in the database."""
        cursor = connection.get_cursor()

        sql = "INSERT IGNORE INTO CATEGORY " "(cat_name) VALUES (%(name)s)"

        for name in categories:
            data_categories = {"name": name}
            cursor.execute(sql, data_categories)

        connection.db.commit()
        category_ids = []

        for name in categories:
            cursor.execute(
                "SELECT id, cat_name FROM category WHERE cat_name = %s", (name,)
            )
            id = cursor.fetchone()[0]
            category_ids.append(id)

        cursor.close()
        return category_ids
