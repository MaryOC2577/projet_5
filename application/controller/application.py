"""Application controller."""

from application.controller.mainmenu import MainController
from application.controller.categorymenu import CatMenuController
from application.controller.productmenu import ProductMenuController
from application.controller.substitute import SubstituteController
from application.model.product import Product
from application.model.category import Category
from application.model.sustitute import SubstiModel


class ApplicationControler:
    """Application controller."""

    def __init__(self):
        """Initialize application controller."""
        self.running = True
        self.controller = MainController()

        self.main_menu = MainController()
        self.category_menu = CatMenuController()
        self.product_menu = ProductMenuController()
        self.substitute_menu = SubstituteController()
        self.product = Prget_oneoduct()
        self.category = Category()
        self.substitute = SubstiModel()
        self.substitute_list = []

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

        # on part du principe qu'on a une command avec les ids de substituts dedans: ex "substitute-base123-12-123-432-124"
        if command.startswith("substitute"):
            # splitted = command.split("-")
            # base_product_id = splitted[1].replace("base", "")
            # substitutes_ids = command.split("-")[2:]
            # substitutes_ids = [int(pk) for pk in substitutes_ids]
            # substitutes = [self.product.get_one(pk=pk) for pk in substitutes_ids]
            # breakpoint()
            # self.substitute_menu.substitute_view.show_save_substi(
            #     self.substitute_list
            # )
            self.controller = SubstituteController(substitutes=substitutes)

        if command.startswith("select-category"):
            category_name = command.split("-")[2]
            products = self.product.getin_onecategory(category_name)
            self.controller = ProductMenuController(products=products)

        if command.startswith("get-product"):
            product_id = command.split("-")[2]
            product = self.product.get_one(product_id)
            self.controller = SubstituteController(product)  # gérer cette partie


        if command == "quit":
            self.running = False

    def get_substitute_choice(self, choice):
        """Return user substitute choice."""
        self.substitute.show(self.category.get_name(choice))
        self.substitute_menu.show(self.substitute.substitutes)
        self.save_substitute(self.product_menu.choice)

    def save_substitute(self, id_product):
        """Save substitute in database."""
        self.substitute.save_substitute(
            self.substitute_menu.input(), id_product
        )
        self.substitute_list = self.substitute.substi_list
