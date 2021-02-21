"""Category selection menu."""


class CategoryMenu:
    """Category selection menu."""

    def __init__(self):
        """Initialize category selection menu."""
        self.main_choice = {
            "1": "Pain",
            "2": "Eau minérale",
            "3": "Soda",
            "4": "Jus de fruits",
            "5": "Biscuits",
            "6": "Apéritifs",
            "7": "Beuure",
            "8": "Céréales petit déjeuner",
            "9": "Yaourt",
            "10": "Produits laitiers",
            "11": "Produits à tartiner",
            "12": "Surgelé",
            "13": "Soupe",
            "14": "Conserve",
            "15": "Pâtes alimentaire",
        }

    def show(self):
        """Display the categories menu."""
        print("Bienvenue sur la page catégorie, faites votre choix :\n")
        for key, value in self.main_choice.items():
            print(key, " - ", value)
