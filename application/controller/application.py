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
        self.main_menu = MainController()
        self.category_menu = CatMenuController()
        self.product_menu = ProductMenuController()
        self.substitute_menu = SubstituteController()
        self.product = Product()
        self.category = Category()
        self.substitute = SubstiModel()
        self.substitute_list = []

    def run(self):
        """Run the application controller."""
        while self.running:
            self.get_main_choice()

    def get_main_choice(self):
        """Return user choice for the main menu."""
        self.main_menu.show()
        if self.main_menu.input() == "category_choice":
            self.get_category_choice()
        if self.main_menu.input() == "substitute":
            # self.get_main_choice()
            self.substitute_menu.substitute_view.show_save_substi(
                self.substitute_list
            )
        if self.main_menu.input() == "quit":
            self.running = False

    def get_category_choice(self):
        """Return user category choice."""
        self.category_menu.show()
        self.get_product_choice(self.category_menu.input())

    def get_product_choice(self, choice):
        """Return user product choice."""
        products = self.product.getin_onecategory(choice)
        self.product_menu.show(products)
        self.get_substitute_choice()

    def get_substitute_choice(self):
        """Return user substitute choice."""
        self.substitute.show(self.category.get_name(self.product_menu.input()))
        # ajouter une méthode qui affiche le produit sélectionné avec nutriscore
        # self.product_menu.show_one(int(self.product_menu.choice))
        self.substitute_menu.show(self.substitute.substitutes)
        self.save_substitute(self.product_menu.choice)

    def save_substitute(self, id_product):
        """Save substitute in database."""
        self.substitute.save_substitute(
            self.substitute_menu.input(), id_product
        )
        self.substitute_list = self.substitute.substi_list
