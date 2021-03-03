"""Substitute detail display menu."""


class SubstiDetail:
    """Substitute detail display menu."""

    def __init__(self):
        """Initialize substitute detail menu."""
        self.message = ""

    def save_confirmed(self):
        """Show a confirmation of substitute save."""
        print("Le substitut a été enregistré.")

    def get_message(self, message):
        """Get get a message based on user choice."""
        print(message)
        self.message = ""

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
                " - ",
                product[4],
            )
        print("Choisir le substitut à sauvegarder : ")
        print("0 puis entrée pour retourner au menu principal.")
