"""Controller of the product menu."""

from application.view.product import ProductMenu


class ProductMenuController:
    """Controller of the product menu."""

    def __init__(self):
        """Initializa the controller of the product menu."""
        self.product_menu = ProductMenu()
        self.choice = ""

    def input(self):
        """Handle input user of the category menu."""
        self.choice = input()
        return self.choice

    def show(self, products):
        """Handle the controller of the product menu."""
        self.product_menu.show(products)
