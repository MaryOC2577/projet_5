"""Controller of the category menu."""

from application.view.category import CategoryMenu


class CatMenuController:
    """Controller of the category menu."""

    def __init__(self):
        """Initialize the controller of the category menu."""

    def show(self):
        """Handle the category menu."""
        category_menu = CategoryMenu()
        category_menu.show()