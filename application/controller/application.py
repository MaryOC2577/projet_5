"""Application controller."""

from application.controller.mainmenu import MainController
from application.view.category import CategoryMenu


class ApplicationControler:
    """Application controller."""

    def __init__(self):
        """Initialize application controller."""

    def show(self):
        """Show the application controller."""

        main_controller = MainController()
        category_menu = CategoryMenu()

        choice = main_controller.show()
        if choice == 1:
            category_menu.show()
