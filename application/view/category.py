"""Category selection menu."""


class CategoryMenu:
    """Category selection menu."""

    def __init__(self):
        """Initialize category selection menu."""
        self.main_choice = {
            "1": "Biscuits",
            "2": "Boissons",
            "3": "Bonbons",
            "4": "Céréales",
            "5": "Charcuterie",
            "6": "Chcolats",
            "7": "Condiments",
            "8": "Desserts",
            "9": "Epices",
            "10": "Féculents",
            "11": "Fromages",
            "12": "Fruits",
            "13": "Glaces",
            "14": "Légumes",
            "15": "Pains",
            "16": "Pâtisseries",
            "17": "Poissons",
            "18": "Sauces",
            "19": "Snacks",
            "20": "Soupes",
            "21": "Surgelés",
        }

    def show(self):
        """Display the categories menu."""
        print("Bienvenue sur la page catégorie, faites votre choix :\n")
        for key, value in self.main_choice.items():
            print(key, " - ", value, "\n")
