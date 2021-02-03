"""Controller of the category menu."""

from application.view.category import CategoryMenu


class CatMenuController:
    """Controller of the category menu."""

    def __init__(self):
        """Initialize the controller of the category menu."""
        self.category_menu = CategoryMenu()

    def show(self):
        """Handle the category menu."""
        self.category_menu.show()