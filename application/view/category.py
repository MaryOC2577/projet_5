"""Category selection menu."""


class CategoryMenu:
    """Category selection menu."""

    def __init__(self):
        """Initialize category selection menu."""
        self.main_choice = {
            "1": "Eau minérale ",
            "2": "Yaourt ",
            "3": "Fromage ",
            "4": "Soda ",
            "13": "Menu principal",
        }

    def show(self):
        """Display the categories menu."""
        print("Bienvenue sur la page catégorie, faites votre choix :\n")
        for key, value in self.main_choice.items():
            print(key, " - ", value)
