"""Category selection menu."""


class CategoryMenu:
    """Category selection menu."""

    def __init__(self):
        """Initialize category selection menu."""
        self.main_choice = {
            "1": "Boissons ",
            "2": "Biscuits ",
            "3": "Pâtisserie ",
            "4": "Conserves ",
            "5": "Apéritifs ",
            "6": "Surgelés ",
            "7": "Céréales petit déjeuner ",
            "8": "Yaourt ",
            "9": "Produits à tartiner ",
            "10": "Produits laitiers",
            "11": "Légumes ",
            "12": "Pâtes alimentaires ",
        }

    def show(self):
        """Display the categories menu."""
        print("Bienvenue sur la page catégorie, faites votre choix :\n")
        for key, value in self.main_choice.items():
            print(key, " - ", value)
