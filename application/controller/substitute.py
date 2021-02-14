"""Display a subtitute from the user's product choice."""

from application.view.substitute import SubstituteMenu


class Substitute:
    """Display a substitute."""

    def __init__(self):
        """Initialize a substitute."""
        self.substitute_menu = SubstituteMenu()
        self.choice = ""

    def input(self):
        """Handle input user of the substitute menu."""
        self.choice = input()
        return self.choice

    def show(self):
        """Handle the substitute menu."""
        self.substitute_menu.show()