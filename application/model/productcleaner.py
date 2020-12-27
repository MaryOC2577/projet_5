"""Procut cleaner."""

from application.model.getdata import OpenFoodFacts
from application.model.product import Product
from application.model.category import Category
from application.model.nutriscore import Nutriscore


class ProductCleaner:
    """Product cleaner."""

    def __init__(self):
        """Initialize."""
        self.cleaned_products = []

    def clean_product(self, products: list):
        """Clean a product."""
        for product in products:
            if (
                not product.get("product_name_fr")
                or not product.get("stores")
                or not product.get("manufacturing_places")
                or not product.get("categories")
                or not product.get("nutrition_grade_fr")
            ):
                continue
            clean_product = {
                "name": product.get("product_name_fr"),
                "stores": product.get("stores"),
                "origin": product.get("manufacturing_places"),
                "categories": product.get("categories"),
                "nutriscore": product.get("nutrition_grade_fr"),
            }
            self.cleaned_products.append(clean_product)

    def get_products_from_off(self):
        """Get the products from OFF and save them in the database."""
        off_products = OpenFoodFacts()
        nutriscore = Nutriscore()
        # current_products = Product()
        # category = Category()

        off_products.get_product_page(10)
        self.clean_product(off_products.products)

        for product in self.cleaned_products:
            print(
                product.get("name"),
                " / ",
                product.get("stores"),
                " / ",
                product.get("origin"),
                " / ",
                product.get("categories"),
                " / ",
                product.get("nutriscore"),
            )
            print()

        if self.cleaned_products:
            # category.save(self.cleaned_products)
            # current_products.save(self.cleaned_products)
            nutriscore.save(self.cleaned_products)
        else:
            print("There is a non complying product.")
