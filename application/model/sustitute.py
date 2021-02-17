"""Handle substitute."""

from application.model.connection import connection


class SubstiModel:
    """Handle substitute."""

    def __init__(self):
        """Initialize substitute."""
        self.substitutes = []
        self.substi_list = []

    def get_list(self):
        """Get a list of all substitutes."""
        cursor = connection.get_cursor()

        sql = "select * from product where substitute is not null;"

        cursor.execute(sql)
        self.substi_list = cursor.fetchall()
        connection.db.commit()
        cursor.close()
        return self.substi_list

    def save_substitute(self, id_substitut, id_product):
        """Save a substitute for a product in database."""
        cursor = connection.get_cursor()

        sql = (
            "UPDATE product "
            f"SET substitute = '{id_substitut}' "
            f"WHERE id = '{id_product}';"
        )

        cursor.execute(sql)
        connection.db.commit()
        cursor.close()

    def show(self, category_name):
        """Return a substitute."""
        cursor = connection.get_cursor()

        sql = (
            "select distinct product.id, product_name, product_description, "
            "nutriscore.nutri_value from product "
            "inner join catprod ON product.id = catprod.id_prod "
            "inner join category ON category.id = catprod.id_cat "
            "inner join nutriscore ON nutriscore.id = product.nutri_id "
            f"where category.cat_name='{category_name}' "
            "order by nutriscore.nutri_value "
            "limit 4;"
        )

        cursor.execute(sql)
        substitutes = cursor.fetchall()
        for substitute in substitutes:
            self.substitutes.append(substitute)
        connection.db.commit()
        cursor.close()
