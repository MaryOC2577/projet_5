"""Class Nutriscore."""

from application.model.connection import connection


class Nutriscore:
    """Class Nutriscore."""

    def __init__(self):
        """Initiate Nutriscore."""

    def get_id(self, nutri_value):
        """Return the id according to the name."""
        cursor = connection.get_cursor()

        id_query = (
            "SELECT id FROM NUTRISCORE WHERE nutri_value = '%s'" % nutri_value
        )

        cursor.execute(id_query)
        nutriscore_id = cursor.fetchone()[0]

        connection.db.commit()
        cursor.close()
        return nutriscore_id

    @classmethod
    def generate(cls) -> bool:
        """Save Nutriscore in database."""
        cursor = connection.get_cursor()

        add_nutriscore = (
            "INSERT IGNORE INTO NUTRISCORE "
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
