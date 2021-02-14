"""Substitute display menu."""


class SubstituteMenu:
    """Substitute display menu."""

    def __init__(self):
        """Initialize the substitute display menu."""

    def show(self, products):
        """Show a substitute."""
        print("Substituts disponibles pour le produit sélectionné : ")
        for product in products:
            print(product[0], " - ", product[1], " - ", product[2])