"""Controller of the main menu."""

from application.view.mainmenu import MainMenu


class MainMenu:
    """Controller of the main menu."""

    def __init__(self):
        """Initialize the main menu controller."""
        self.main_menu = MainMenu()

    def mainmenu(self):
        """Handle the main menu controller."""
        choice = input(self.main_menu.show())
        return choice