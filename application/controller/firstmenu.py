"""Controller of the first menu."""

from application.view.main import MainMenu


class FirstController:
    """Controller of the first menu."""

    def __init__(self):
        """Initialize the controller."""

    def first_controller(self):
        """Handle the first controller."""
        choice = input(MainMenu.display())
        if choice == 1:
            pass
