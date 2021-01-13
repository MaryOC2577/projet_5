"""Procut cleaner."""

from application.model.getdata import OpenFoodFacts
from application.model.product import Product
from application.model.category import Category
from application.model.nutriscore import Nutriscore
from application.model.catprod import CatProd


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
                or not product.get("generic_name")
                or not product.get("stores")
                or not product.get("categories")
                or not product.get("nutrition_grade_fr")
                or not product.get("url")
            ):
                continue
            else:
                clean_product = {
                    "name": product.get("product_name_fr"),
                    "desciption": product.get("generic_name"),
                    "stores": product.get("stores"),
                    "categories": (
                        product.get("categories").replace("fr:", "")
                    ).split(","),
                    "nutriscore": (product.get("nutrition_grade_fr")).upper(),
                    "url": product.get("url"),
                }

                self.cleaned_products.append(clean_product)

    def get_products_from_off(self):
        """Get the products from OFF and save them in the database."""
        off_products = OpenFoodFacts()
        nutriscore = Nutriscore()
        category = Category()
        current_products = Product()
        catprod = CatProd()

        off_products.get_product_page(20)
        self.clean_product(off_products.products)

        for product in self.cleaned_products:
            print(
                product.get("name"),
                " / ",
                product.get("description"),
                " / ",
                product.get("shop"),
                " / ",
                product.get("categories"),
                " / ",
                product.get("nutriscore"),
                " / ",
                product.get("url"),
            )
            print()

        if self.cleaned_products:
            nutriscore.generate()
            category.save(self.cleaned_products)
            current_products.save(self.cleaned_products)
            catprod.save(self.cleaned_products)
        else:
            print("There is a non complying product.")
