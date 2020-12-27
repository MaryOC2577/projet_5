"""Class Nutriscore."""

from application.model.connection import connection


class Nutriscore:
    """Class Nutriscore."""

    def __init__(self):
        """Initiate Nutriscore."""

    @classmethod
    def save(cls, cleaned_product: list) -> bool:
        """Save Nutriscore in database."""
        cursor = connection.get_cursor()

        add_nutriscore = (
            "INSERT INTO NUTRISCORE ",
            "(id, nutri_value) ",
            "VALUES (%s, %s)",
        )

        for product in cleaned_product:
            data_nutriscore = {"id": None, "value": product.get("nutriscore")}
            cursor.execute(add_nutriscore, data_nutriscore)

        connection.db.commit()
        cursor.close()
        connection.close()
        return True
