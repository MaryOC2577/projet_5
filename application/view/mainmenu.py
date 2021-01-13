"""Main menu."""


class menu:
    """Display the main menu."""

    def __init__(self):
        """Initialize menu."""

    def display_menu(self):
        """Display the main menu."""
        choice_one = input(
            "1 - Quel aliment souhaitez-vous remplacer ?"
            "2 - Retrouver mes alimments substitués."
        )

        if choice_one == 1:
            choice_two = input(
                "Sélectionnez une catégorie : "
                "1 - Boissons"
                "2 - Surgelés"
                "3 - Fruits"
            )

        # afficher les produits correspondant à la catégorie choisit par l'utilisateur
        # enregister l'aliment choisit et la catégorie
