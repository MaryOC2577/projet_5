"""Application controller."""

from application.controller.mainmenu import MainMenu
from application.controller.categorymenu import CatMenuController
from application.controller.productmenu import ProductMenuController
from application.controller.substitute import Substitute
from application.model.product import Product
from application.model.category import Category


class ApplicationControler:
    """Application controller."""

    def __init__(self):
        """Initialize application controller."""
        self.running = True
        self.main_menu = MainMenu()
        self.category_menu = CatMenuController()
        self.product_menu = ProductMenuController()
        self.substitute_menu = Substitute()
        self.product = Product()
        self.category = Category()

    def main_choice(self):
        """Returns user choice."""
        self.main_menu.show()
        choice = input()
        if choice == "1":
            self.category_choice()
        if choice == "2":
            print("Menu indisponible.")
        if choice == "3":
            print("Vous avez quitté l'application.")
            self.running = False

    def category_choice(self):
        """Return user category choice."""
        self.category_menu.show()
        choice = input()
        self.product_choice(choice)

    def product_choice(self, choice):
        """Return user product choice."""
        products = self.product.getin_onecategory(
            self.category_menu.category_menu.main_choice[choice]
        )
        self.product_menu.show()

        for product in products:
            print(product[0], " - ", product[1], " - ", product[2], "\n")
        self.substitute_choice()

    def substitute_choice(self):
        """Return user substitute choice."""
        choice = input()
        self.substitute_menu.show()
        print(
            "La catégorie du produit sélectionné est : ",
            self.category.get_name(choice),
        )

    def show(self):
        """Show the application controller."""
        while self.running:
            self.main_choice()

        # afficher le menu principal
        # l'utilisateur fait un choix 1 ou 2
        # le controller menu principal retourne le choix de l'utilisateur
        # pour le choix 1 afficher menu catégories (controller category)
        # l'utilisateur choisi une catégorie
        # SQL sélectionne produits dans catégorie choisie
        # afficher menu prduits (résultats requête SQL)
