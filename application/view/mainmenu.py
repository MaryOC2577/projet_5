"""Main menu."""


class MainMenu:
    """Main menu."""

    def __init__(self):
        """Initialize the main menu."""
        self.main_choice = {
            "1": "Quel aliment souhaitez-vous remplacer ?",
            "2": "Retrouvez mes aliments substitués",
            "3": "Menu principal",
        }
        self.message = ""

    def get_message(self, message):
        """Get get a message based on user choice."""
        print(message)
        self.message = ""

    def show(self):
        """Show the main menu."""
        print("Bienvenue sur la page d'acceuil, faites votre choix :\n")
        for key, value in self.main_choice.items():
            print(key, " - ", value)
