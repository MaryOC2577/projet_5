"""Controller of the first menu."""

from application.view.main import MainMenu


class FirstController:
    """Controller of the first menu."""

    def __init__(self):
        """Initialize the controller."""

    @classmethod
    def first_controller(cls):
        """Handle the first controller."""
        choice = input(MainMenu.display())