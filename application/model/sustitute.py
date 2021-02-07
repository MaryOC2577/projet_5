"""Handle substitute."""

from application.model.connection import connection


class Substitute:
    """Handle substitute."""

    def __init__(self):
        """Initialized substitute."""
        self.substitutes = []

    def show(self, category_name):
        """Return a substitute."""
        cursor = connection.get_cursor()

        sql = (
            "select product_name, product_description, nutriscore.nutri_value from product "
            "inner join catprod ON product.id = catprod.id_prod "
            "inner join category ON category.id = catprod.id_cat "
            "inner join nutriscore ON nutriscore.id = product.nutri_id "
            f"where category.cat_name like '{category_name}'"
            "order by nutriscore.nutri_value;"
        )

        cursor.execute(sql)
        substitutes = cursor.fetchall()
        for substitute in substitutes:
            self.substitutes.append(substitute)
        connection.db.commit()
        cursor.close()
        return self.substitutes
