"""Favorites substitutes display menu."""


class Favorites:
    """Favorites substitutes display menu."""

    def __init__(self):
        """Initialize favorites display menu."""

    def show(self, subsitutes):
        """Show  substitutes in database."""
        print("Liste des substituts enregistrés : ")
        for substitute in subsitutes:
            print(
                substitute[0],
                " - ",
                substitute[1],
                " - ",
                substitute[2],
                " - ",
                substitute[3],
            )
