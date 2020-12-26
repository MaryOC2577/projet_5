"""Class Category."""

from application.model.connection import connection


class Category:
    """Class Category."""

    def __init__(self):
        """Initiate category class."""

    @classmethod
    def save(cls, cleaned_product: dict) -> bool:
        """Save categories in the database."""
        cursor = connection.get_cursor()

        add_categories = (
            "INSERT INTO CATEGORY (id, cat_name) VALUES (%(id)s, %(name)s)"
        )

        for value in cleaned_product.values():
            for cat_value in value[3]:
                data_categories = {"id": None, "name": cat_value}
                cursor.execute(add_categories, data_categories)

        connection.db.commit()
        cursor.close()
        connection.close()
        return True
