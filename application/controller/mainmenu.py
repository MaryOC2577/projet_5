"""Controller of the main menu."""

from application.view.mainmenu import MainMenu


class MainController:
    """Controller of the main menu."""

    def __init__(self):
        """Initialize the main menu controller."""
        self.main_menu = MainMenu()
        self.choice = ""
        self.input_choice = ""

    def input(self):
        """Handle input user of the main menu."""
        self.choice = input()
        if self.choice == "1":
            self.input_choice = "category_choice"
        if self.choice == "2":
            self.main_menu.get_message("Menu indisponible.")
            self.input_choice = "substitute"
        if self.choice == "3":
            self.main_menu.get_message("Vous allez quitter l'application.")
            self.input_choice = "quit"
        return self.input_choice

    def show(self):
        """Handle the main menu controller."""
        self.main_menu.show()
        self.input()
