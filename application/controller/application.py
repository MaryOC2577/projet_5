"""Application controller."""

from application.controller.mainmenu import MainController
from application.controller.categorymenu import CatMenuController
from application.controller.productmenu import ProductMenuController
from application.model.product import Product


class ApplicationControler:
    """Application controller."""

    def __init__(self):
        """Initialize application controller."""

    def show(self):
        """Show the application controller."""
        main_controller = MainController()
        category_menu = CatMenuController()
        product_menu = ProductMenuController()
        product_list = Product()

        main_controller.show()
        main_choice = int(input())

        if main_choice == 1:
            category_menu.show()
        if main_choice == 2:
            print("2 - indisponible.")

        cat_choice = int(input())

        if cat_choice == 1:
            product_menu.show()
            print(product_list.getin_onecategory("biscuit"))

        # afficher le menu principal
        # l'utilisateur fait un choix 1 ou 2
        # le controller menu principal retourne le choix de l'utilisateur
        # pour le choix 1 afficher menu catégories (controller category)
        # l'utilisateur choisi une catégorie
        # SQL sélectionne produits dans catégorie choisie
        # afficher menu prduits (résultats requête SQL)
