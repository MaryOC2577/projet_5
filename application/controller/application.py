"""Application controller."""

from application.controller.mainmenu import MainController
from application.controller.categorymenu import CatMenuController


class ApplicationControler:
    """Application controller."""

    def __init__(self):
        """Initialize application controller."""

    def show(self):
        """Show the application controller."""

        main_controller = MainController()
        category_menu = CatMenuController()

        choice = main_controller.show()

        if choice == 1:
            print("Test condition.")
            category_menu.show()
            input()
