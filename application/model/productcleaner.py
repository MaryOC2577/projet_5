"""Procut cleaner."""

from application.model.getdata import OpenFoodFacts
from application.model.product import Product


class ProductCleaner:
    """Product cleaner."""

    def __init__(self):
        """Initialize."""
        self.cleaned_products = {}

    def clean_product(self, products: list):
        """Clean a product."""
        x = 0
        for product in products:
            self.cleaned_products[x] = list()
            if (
                not product.get("product_name_fr")
                or not product.get("stores")
                or not product.get("manufacturing_places")
                or not product.get("categories")
                or not product.get("nutrition_grade_fr")
            ):
                continue
            else:
                self.cleaned_products[x].append(product.get("product_name_fr"))
                self.cleaned_products[x].append(
                    (product.get("stores")).split(",")
                )
                self.cleaned_products[x].append(
                    product.get("manufacturing_places")
                )
                self.cleaned_products[x].append(
                    (product.get("categories")).split(",")
                )
                self.cleaned_products[x].append(
                    (product.get("nutrition_grade_fr")).upper()
                )
                x += 1

    def get_products_from_off(self):
        """Get the products from OFF and save them in the database."""
        off_products = OpenFoodFacts()
        product = Product()
        off_products.get_product_page(15)
        self.clean_product(off_products.products)
        for key, value in self.cleaned_products.items():
            print(key, " / ", value)
            print()

        if self.cleaned_products:
            product.save(self.cleaned_products)
        else:
            print("There is a non complying product.")
