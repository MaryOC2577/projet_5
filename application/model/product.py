"""Class Product."""

from application.model.connection import connection
from application.model.nutriscore import Nutriscore


class Product:
    """Class product."""

    def __init__(self):
        """Initiate product class."""
        self.product_cat = []
        self.product_in_category = []

    def get_one(self, product_id):
        """Get one product with nutriscore."""
        cursor = connection.get_cursor()

        sql = (
            "select product.id, product_name, product_description, "
            "nutriscore.nutri_value "
            "from product "
            "INNER JOIN nutriscore ON nutriscore.id = product.nutri_id "
            f"where product.id ='{product_id}';"
        )

        cursor.execute(sql)
        product = cursor.fetchone()
        connection.db.commit()
        cursor.close()
        return product

    def getin_onecategory(self, category):
        """Get a list of proucts in one category."""
        cursor = connection.get_cursor()

        sql = (
            "SELECT distinct product.id, product_name, "
            "product_description from product "
            "INNER JOIN catprod ON product.id = catprod.id_prod "
            "INNER JOIN category ON category.id = catprod.id_cat "
            f"where category.cat_name LIKE '%{category}%' "
            "limit 40;"
        )
        cursor.execute(sql)
        products = cursor.fetchall()
        self.product_in_category = []
        for product in products:
            self.product_in_category.append(product)
        connection.db.commit()
        cursor.close()
        return self.product_in_category

    def get_id(self, name_product):
        """Return the id according to the name."""
        cursor = connection.get_cursor()

        sql = "SELECT id FROM PRODUCT WHERE product_name ='%s'" % name_product
        cursor.execute(sql)
        product_id = cursor.fetchone()[0]

        connection.db.commit()
        cursor.close()
        return product_id

    def get_fromcategory(self, id_cat):
        """Return all products of one category."""
        cursor = connection.get_cursor()

        sql = (
            "SELECT id, product_name FROM PRODUCT "
            "INNER JOIN CATPROD "
            "ON product.id = catprod.id_product"
            "WHERE catprod.id_cat='%s' " & id_cat
        )

        cursor.execute(sql)
        self.product_cat = cursor.fetchone()

        connection.db.commit()
        cursor.close()
        return self.product_cat

    @classmethod
    def save(cls, product: dict) -> int:
        """Save products in the database."""
        cursor = connection.get_cursor()
        nutri_score = Nutriscore()

        sql = (
            "INSERT IGNORE INTO PRODUCT "
            "(product_name, product_description, shop, "
            "substitute, nutri_id, product_url) "
            "VALUES (%(name)s, %(description)s, %(shop)s, "
            "%(substitute)s, %(nutri_id)s, %(url)s)"
        )

        data_products = {
            "name": product.get("name"),
            "description": product.get("description"),
            "shop": product.get("stores"),
            "substitute": None,
            "nutri_id": nutri_score.get_id(product.get("nutriscore")),
            "url": product.get("url"),
        }
        cursor.execute(sql, data_products)

        cursor.execute(
            "SELECT id, product_name FROM product WHERE product_name = %s",
            (product["name"],),
        )
        id = cursor.fetchone()[0]
        connection.db.commit()
        cursor.close()
        return id
