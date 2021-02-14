"""Product selection menu."""


class ProductMenu:
    """Product selection menu."""

    def __init__(self):
        """Initialize product selection menu."""

    def show(self, products):
        """Show the product selection menu."""
        print("Bienvenue sur la page prouits, Sélectionnez l'aliment : ")
        for product in products:
            print(product[0], " - ", product[1], " - ", product[2])
