"""Application controller."""

from application.controller.mainmenu import MainController
from application.controller.categorymenu import CatMenuController
from application.controller.productmenu import ProductMenuController
from application.controller.substidetail import SubstiDetailController
from application.controller.favorites import FavoritesController
from application.model.product import Product
from application.model.substitute import SubstiModel


class ApplicationController:
    """Application Controller."""

    def __init__(self):
        """Initialize application controller."""
        self.running = True
        self.controller = MainController()
        self.product = Product()
        self.substitute = SubstiModel()

    def run(self):
        """Run the application controller."""
        while self.running:
            self.controller.show()
            command = self.controller.input()
            self.update(command)

    def update(self, command: str):
        """Update the application."""
        if command == "category_choice":
            self.controller = CatMenuController()
        if command.startswith("select-category"):
            category_name = command.split("-")[2]
            products = self.product.getin_onecategory(
                category_name.replace(" ", "%")
            )
            self.controller = ProductMenuController(products)
        if command.startswith("get-product"):
            product_id = command.split("-")[2]
            product = self.product.get_one(product_id)
            self.controller.show_one(product)
            self.controller = SubstiDetailController(product)
        if command.startswith("get-substitute"):
            substitute_id = command.split("-")[2:][0]
            product_id = command.split("-")[3:][0]
            self.substitute.save_substitute(substitute_id, product_id)
            self.controller.save_confirmed()
            self.controller = MainController()
        if command == "substitute":
            self.controller = FavoritesController()
        if command == "quit":
            self.running = False
        if command == "":
            self.controller = MainController()
