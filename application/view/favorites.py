"""Favorites substitutes display menu."""


class Favorites:
    """Favorites substitutes display menu."""

    def __init__(self):
        """Initialize favorites display menu."""

    def show(self, substitutes):
        """Show  substitutes in database."""
        print("Liste des aliments ayant des substituts enregistrés : ")
        for favorite in substitutes:
            print(
                "Produit d'origine :\n",
                favorite[0],
                " - ",
                favorite[1],
                " - ",
                favorite[2],
                " - ",
                favorite[3],
                "\n",
                "Substitut :\n",
                favorite[4],
                " - ",
                favorite[5],
                " - ",
                favorite[6],
                " - ",
                favorite[7],
            )
