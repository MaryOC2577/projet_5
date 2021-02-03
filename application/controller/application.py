"""Application controller."""

from application.controller.mainmenu import MainMenu
from application.controller.categorymenu import CatMenuController


class ApplicationControler:
    """Application controller."""

    def __init__(self):
        """Initialize application controller."""
        self.running = True
        self.main_menu = MainMenu()
        self.category_menu = CatMenuController()

    def main_choice(self):
        """Returns user choice."""
        self.main_menu.show()
        choice = input()
        if choice == "1":
            self.category_menu.show()
        if choice == "2":
            print("Menu indisponible.")
        if choice == "3":
            print("L'application va être fermée.")
            self.running = False

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
