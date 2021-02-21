"""Category selection menu."""


class CategoryMenu:
    """Category selection menu."""

    def __init__(self):
        """Initialize category selection menu."""
        self.main_choice = {
            "1": "Barre de céréales ",
            "2": "Eau minérale ",
            "3": "Pâtisserie ",
            "4": "Conserve ",
            "5": "Biscuits",
            "6": "Apéritifs",
            "7": "Surgelé ",
            "8": "Céréales petit déjeuner",
            "9": "Yaourt",
            "10": "Produits laitiers",
            "11": "Produits à tartiner",
        }

    def show(self):
        """Display the categories menu."""
        print("Bienvenue sur la page catégorie, faites votre choix :\n")
        for key, value in self.main_choice.items():
            print(key, " - ", value)
