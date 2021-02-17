"""Controller of the product menu."""

from application.view.product import ProductMenu
from application.model.product import Product


class ProductMenuController:
    """Controller of the product menu."""

    def __init__(self):
        """Initializa the controller of the product menu."""
        self.product_menu = ProductMenu()
        self.choice = ""
        self.one_product = Product()

    def input(self):
        """Handle input user of the product menu."""
        self.choice = input()
        return self.choice

    def show_one(self, product_id):
        """Show one product with id."""
        self.product_menu.show_one(product_id)

    def show(self, products):
        """Handle the controller of the product menu."""
        self.product_menu.show(products)
