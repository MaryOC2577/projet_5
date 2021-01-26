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

            clean_product = {
                "name": product.get("product_name_fr"),
                "description": product.get("generic_name"),
                "stores": product.get("stores"),
                "categories": (
                    product.get("categories_lc").replace("fr:", "")
                ).split(","),
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

        connection.get_product_page(1000)
        self.clean_product(connection.products)

        if self.cleaned_products:
            nutriscore.generate()
            for product in self.cleaned_products:
                product_id = Product.save(product)
                category_ids = category.save(product["categories"])
                catprod.save(product_id, category_ids)
        else:
            print("There is a non complying product.")
