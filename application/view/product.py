"""Product selection menu."""


class ProductMenu:
    """Product selection menu."""

    def __init__(self):
        """Initialize product selection menu."""

    def show_one(self, product):
        """Show on prouct with id."""
        print("Le produit sélectionné est :")
        print(
            product[0], " - ", product[1], " - ", product[2], " - ", product[3]
        )

    def show(self, products):
        """Show the product selection menu."""
        print("Bienvenue sur la page produits, Sélectionnez l'aliment : ")
        for product in products:
            print(product[0], " - ", product[1], " - ", product[2])
