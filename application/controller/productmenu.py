"""Controller of the product menu."""

from application.view.product import ProductMenu
from application.model.product import Product


class ProductMenuController:
    """Controller of the product menu."""

    def __init__(self, products):
        """Initializa the controller of the product menu."""
        self.product_menu = ProductMenu()
        self.choice = ""
        self.one_product = Product()
        self.products = products

    def input(self):
        """Handle input user of the product menu."""
        self.choice = input()
        check_products = []

        for product in self.products:
            check_products.append(product[0])

        if self.choice not in str(check_products):
            self.product_menu.get_message("Erreur de saisie")
            return "category-menu"
        if self.choice == "":
            return "category-menu"
        if self.choice == "0":
            return "main-menu"
        else:
            return "get-product-" + self.choice

    def show_one(self, product_id):
        """Show one product with id."""
        self.product_menu.show_one(product_id)

    def show(self):
        """Handle the controller of the product menu."""
        self.product_menu.show(self.products)
