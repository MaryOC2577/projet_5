"""Main menu."""


class Menu:
    """Display the main menu."""

    def __init__(self):
        """Initialize menu."""

    def home(self):
        """Display the main menu."""
        print(
            "1 - Quel aliment souhaitez-vous remplacer ?\n"
            "2 - Retrouver mes alimments substitués."
        )

    def show_category(self):
        """Display the categories menu."""
        print("Sélectionnez une catégorie : ")

    def show_product(self):
        """Display the product menu."""
        print("Sélectionnez un produit : ")

    def show_substitute(self):
        """Display substitutes."""
        print("Liste des substituts disponibles : ")
