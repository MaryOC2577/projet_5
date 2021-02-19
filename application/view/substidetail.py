"""Substitute detail display menu."""


class SubstiDetail:
    """Substitute detail display menu."""

    def __init__(self):
        """Initialize substitute detail menu."""

    def save_confirmed(self):
        """Show a confirmation of substitute save."""
        print("Le substitut a été enregistré.")

    def show(self, products):
        """Show a substitute."""
        print("Substituts disponibles pour le produit sélectionné : ")
        for product in products:
            print(
                product[0],
                " - ",
                product[1],
                " - ",
                product[2],
                " - ",
                product[3],
            )
        print("Choisir le substitut à sauvegarder : ")
