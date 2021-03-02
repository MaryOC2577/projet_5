"""Handle substitute."""

from application.model.connection import connection


class SubstiModel:
    """Handle substitute."""

    def __init__(self):
        """Initialize substitute."""
        self.substitutes = []

    def get_list(self):
        """Get a list of all substitutes."""
        cursor = connection.get_cursor()

        sql = (
            "select substituted.id, substituted.product_name, "
            "substituted.product_description, "
            "nutri_ted.nutri_value, substi.id, substi.product_name, "
            "substi.product_description, "
            "substi.nutri_value from product as substituted "
            "inner join nutriscore as nutri_ted on nutri_ted.id = substituted.nutri_id "
            "inner join "
            "(select substitute.id, substitute.product_name, "
            "substitute.product_description, "
            "nutri_te.nutri_value from product as substitute "
            "inner join nutriscore as nutri_te on nutri_te.id = substitute.nutri_id) "
            "as substi on substituted.substitute = substi.id;"
        )
        cursor.execute(sql)
        substi_list = []
        for substitut in cursor.fetchall():
            substi_list.append(substitut)
        connection.db.commit()
        cursor.close()
        return substi_list

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
            "nutriscore.nutri_value, product_url from product "
            "inner join catprod ON product.id = catprod.id_prod "
            "inner join category ON category.id = catprod.id_cat "
            "inner join nutriscore ON nutriscore.id = product.nutri_id "
            f"where category.cat_name='{category_name}' "
            "order by nutriscore.nutri_value "
            "limit 10;"
        )

        cursor.execute(sql)
        substitutes = cursor.fetchall()
        for substitute in substitutes:
            self.substitutes.append(substitute)
        connection.db.commit()
        cursor.close()
        return self.substitutes
