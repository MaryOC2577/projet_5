"""Application controller."""

from application.controller.mainmenu import MainMenu


class ApplicationControler:
    """Application controller."""

    def __init__(self):
        """Initialize application controller."""
        self.mainmenu = MainMenu()

    def show(self):
        """Show the application controller."""
        self.mainmenu.show()