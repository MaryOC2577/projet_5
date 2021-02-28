"""Category selection menu."""


class CategoryMenu:
    """Category selection menu."""

    def __init__(self):
        """Initialize category selection menu."""
        self.main_choice = {
            "1": "Eau minérale ",
            "2": "Yaourt ",
            "3": "Fromage ",
            "4": "Poisson ",
            "5": "Confiture ",
            "6": "Sauce ",
            "7": "Conserve ",
            "8": "Biscuit ",
            "9": "Jambon ",
            "10": "Purée ",
            "11": "Riz",
            "12": "Apéritif ",
            "13": "Plat préparé ",
            "14": "Menu principal",
        }

    def show(self):
        """Display the categories menu."""
        print("Bienvenue sur la page catégorie, faites votre choix :\n")
        for key, value in self.main_choice.items():
            print(key, " - ", value)
