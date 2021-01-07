"""Display a subtitute from the user's product choice."""

from application.model.category import Category
from application.model.product import Product
from application.model.connection import Connection


class substitute:
    """Display a substitute."""

    def __init__(self):
        """Initialize a substitute."""
        self.substitute = {}

    def get_substitute(self, category_name, product_name):
        """Display a subtitute from the user's product choice."""

        category = Category()
        product = Product()
        connection = Connection()
        id_category = category.get_idcategory(category_name)
        id_product = product.get_idproduct(product_name)

        cursor = connection.get_cursor()

        id_query = (
            "SELECT id, product_name, shop FROM PRODUCT "
            "INNER JOIN catprod "
            "ON product.id = catprod.id_product"
            "WHERE catprod.id_cat='%s' "
            & id_category
            & "AND catprod.id_prod='%s'"
            & id_product
        )

        cursor.execute(id_query)
        self.substitute = cursor.fetchone()

        connection.db.commit()
        cursor.close()
        return self.substitute
