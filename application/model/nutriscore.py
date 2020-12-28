"""Class Nutriscore."""

from application.model.connection import connection


class Nutriscore:
    """Class Nutriscore."""

    def __init__(self):
        """Initiate Nutriscore."""

    @classmethod
    def save(cls) -> bool:
        """Save Nutriscore in database."""
        cursor = connection.get_cursor()

        add_nutriscore = (
            "INSERT INTO NUTRISCORE "
            "(id, nutri_value) VALUES (%(id)s, %(value)s)"
        )

        data_nutriscore = [
            {"id": None, "value": "A"},
            {"id": None, "value": "B"},
            {"id": None, "value": "C"},
            {"id": None, "value": "D"},
            {"id": None, "value": "E"},
        ]

        for score in data_nutriscore:
            one_nutriscore = {
                "id": None,
                "value": score.get("value"),
            }
            cursor.execute(add_nutriscore, one_nutriscore)

        connection.db.commit()
        cursor.close()
        return True
