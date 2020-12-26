"""Procut cleaner."""

from application.model.getdata import OpenFoodFacts
from application.model.product import Product
from application.model.category import Category


class ProductCleaner:
    """Product cleaner."""

    def __init__(self):
        """Initialize."""
        self.cleaned_products = {}

    def clean_product(self, products: list):
        """Clean a product."""
        counter = 0
        for product in products:
            self.cleaned_products[counter] = list()
            if (
                not product.get("product_name_fr")
                or not product.get("stores")
                or not product.get("manufacturing_places")
                or not product.get("categories")
                or not product.get("nutrition_grade_fr")
            ):
                continue
            else:
                self.cleaned_products[counter].append(
                    product.get("product_name_fr")
                )
                self.cleaned_products[counter].append(product.get("stores"))
                self.cleaned_products[counter].append(
                    product.get("manufacturing_places")
                )
                self.cleaned_products[counter].append(
                    (product.get("categories")).split(",")
                )
                self.cleaned_products[counter].append(
                    (product.get("nutrition_grade_fr")).upper()
                )
                counter += 1

    def get_products_from_off(self):
        """Get the products from OFF and save them in the database."""
        off_products = OpenFoodFacts()
        product = Product()
        category = Category()
        off_products.get_product_page(10)
        self.clean_product(off_products.products)
        for key, value in self.cleaned_products.items():
            print(key, " / ", value)
            print()

        if self.cleaned_products:
            # category.save(self.cleaned_products)
            product.save(self.cleaned_products)
        else:
            print("There is a non complying product.")
