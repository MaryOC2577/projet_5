"""Application controller."""

from application.controller.mainmenu import MainMenu


class ApplicationControler:
    """Application controller."""

    def __init__(self):
        """Initialize application controller."""

    def show(self):
        """Show the application controller."""
        main_menu = MainMenu()
        main_menu.show()