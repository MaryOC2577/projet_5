"""Controller of the category menu."""

from application.view.category import CategoryMenu


class CatMenuController:
    """Controller of the category menu."""

    def __init__(self):
        """Initialize the controller of the category menu."""
        self.category_menu = CategoryMenu()

    def input(self):
        """Handle input user of the category menu."""
        choice = input()
        if choice in self.category_menu.main_choice:
            category_name = self.category_menu.main_choice[choice]
            return "select-category-" + category_name
        return ""

    def show(self):
        """Handle the category menu."""
        self.category_menu.show()
