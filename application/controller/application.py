"""Application controller."""

from application.controller.mainmenu import MainController
from application.controller.categorymenu import CatMenuController
from application.controller.productmenu import ProductMenuController
from application.controller.substitute import Substitute
from application.model.product import Product
from application.model.category import Category
from application.model.sustitute import SubstiModel


class ApplicationControler:
    """Application controller."""

    def __init__(self):
        """Initialize application controller."""
        self.running = True
        self.main_menu = MainController()
        self.category_menu = CatMenuController()
        self.product_menu = ProductMenuController()
        self.substitute_menu = Substitute()
        self.product = Product()
        self.category = Category()
        self.substitute = SubstiModel()

    def run(self):
        """Run the application controller."""
        while self.running:
            self.get_main_choice()

    def get_main_choice(self):
        """Return user choice."""
        self.main_menu.show()
        if self.main_menu.input() == "category_choice":
            self.get_category_choice()
        if self.main_menu.input() == "substitute":
            self.get_main_choice()
        if self.main_menu.input() == "quit":
            self.running = False

        # if self.main_menu.choice == "1":
        #   self.get_category_choice()
        # if self.main_menu.choice == "2":
        #    print("Menu indisponible.")
        # if self.main_menu.choice == "3":
        #    print("Vous avez quitté l'application.")
        #    self.running = False

    def get_category_choice(self):
        """Return user category choice."""
        self.category_menu.show()
        choice = input()
        self.get_product_choice(choice)

    def get_product_choice(self, choice):
        """Return user product choice."""
        products = self.product.getin_onecategory(
            self.category_menu.category_menu.main_choice[choice]
        )
        self.product_menu.show()

        for product in products:
            print(product[0], " - ", product[1], " - ", product[2])
        self.get_substitute_choice()

    def get_substitute_choice(self):
        """Return user substitute choice."""
        self.substitute_menu.show()
        choice = input()
        self.category.get_name(choice)
        self.substitute.show(self.category.get_name(choice))
        for product in self.substitute.substitutes:
            print(product[0], " - ", product[1], " - ", product[2])
