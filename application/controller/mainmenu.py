"""Controller of the main menu."""

from application.view.mainmenu import MainMenu
from application.controller.application import ApplicationControler


class MainController:
    """Controller of the main menu."""

    def __init__(self):
        """Initialize the main menu controller."""
        self.main_menu = MainMenu()
        self.application = ApplicationControler()
        self.choice = ""

    def input(self):
        """Handle input user of the main menu."""
        self.choice = input()
        if self.choice == "1":
            self.application.get_category_choice()
        if self.choice == "2":
            self.main_menu.get_message("Menu indisponible.")
        if self.choice == "3":
            self.main_menu.get_message("Vous allez quitter l'application.")
            self.application.running = False

    def show(self):
        """Handle the main menu controller."""
        self.main_menu.show()
        self.input()
