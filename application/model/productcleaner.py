"""Procut cleaner."""

from application.model.getdata import OpenFoodFacts
from application.model.product import Product


class ProductCleaner:
    """Product cleaner."""

    def __init__(self):
        """Initialize."""
        self.cleaned_products = {}

    def clean_product(self, product: dict) -> dict:
        """Clean a product."""
        for key in product:
            if product[key] == "name":
                self.cleaned_products["name"] = product["name"]
            if product[key] == "stores":
                self.cleaned_products["stores"] = product["stores"]
            if product[key] == "manufacturing_places_tag":
                self.cleaned_products["manufacturing_places_tag"] = product[
                    "manufacturing_places_tag"
                ]
            if product[key] == "categories":
                self.cleaned_products["categories"] = product["categories"]
            if product[key] == "nutrition_grade_fr":
                self.cleaned_products["nutrition_grade_fr"] = product[
                    "nutrition_grade_fr"
                ]

    def get_products_from_off(self):
        """Get the products from OFF and save them in the database."""
        products = OpenFoodFacts()
        # product = Product()
        products.get_product_page(2)
        self.clean_product(products.products)
        print(self.cleaned_products)
        # if self.cleaned_products:
        # product.save(self.cleaned_products)
        # else:
        # print("There is a non complying product.")
