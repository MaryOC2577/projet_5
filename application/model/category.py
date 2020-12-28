"""Class Category."""

from application.model.connection import connection


class Category:
    """Class Category."""

    def __init__(self):
        """Initiate category class."""

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
