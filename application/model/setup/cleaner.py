"""Procut cleaner."""

from application.model.connection import Connection
from application.model.product import Product
from application.model.category import Category
from application.model.nutriscore import Nutriscore
from application.model.setup.catprod import CatProd


class ProductCleaner:
    """Product cleaner."""

    def __init__(self):
        """Initialize."""
        self.cleaned_products = []

    def clean_product(self, products: list):
        """Clean a product."""
        for product in products:
            if (
                not product.get("generic_name")
                or not product.get("product_name_fr")
                or not product.get("generic_name")
                or not product.get("stores")
                or not product.get("categories")
                or not product.get("nutrition_grade_fr")
                or not product.get("url")
            ):
                continue
            if not product.get("categories_lc") == "fr":
                continue
            clean_product = {
                "name": product.get("product_name_fr").strip(" "),
                "description": product.get("generic_name"),
                "stores": product.get("stores"),
                "categories": (product.get("categories").replace("fr:", ""))
                .split(",")
                .strip(" "),
                "nutriscore": (product.get("nutrition_grade_fr")).upper(),
                "url": product.get("url"),
            }
            self.cleaned_products.append(clean_product)

    def get_products_from_off(self):
        """Get the products from OFF and save them in the database."""
        connection = Connection()
        nutriscore = Nutriscore()
        category = Category()
        catprod = CatProd()

        number_page = 1
        max_page = range(5)
        for number_page in max_page:
            connection.get_product_page(number_page)
            self.clean_product(connection.products)
            number_page += 1

        if self.cleaned_products:
            nutriscore.generate()
            for product in self.cleaned_products:
                product_id = Product.save(product)
                category_ids = category.save(product["categories"])
                catprod.save(product_id, category_ids)
        else:
            print("There is a non complying product.")
