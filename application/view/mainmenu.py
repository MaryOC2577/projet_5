"""Main menu."""


class MainMenu:
    """Main menu."""

    def __init__(self):
        """Initialize the main menu."""
        self.main_menu = {
            "1": "Quel aliment souhaitez-vous remplacer ?",
            "2": "Retrouvez mes aliments substitués",
            "3": "Quitter",
        }

    def show(self):
        """Show the main menu."""
        for key, value in self.main_menu:
            print(key, " - ", value, "\n")
