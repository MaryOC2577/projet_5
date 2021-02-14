"""Controller of the category menu."""

from application.view.category import CategoryMenu


class CatMenuController:
    """Controller of the category menu."""

    def __init__(self):
        """Initialize the controller of the category menu."""
        self.category_menu = CategoryMenu()
        self.choice = ""
        self.input_choice = ""

    def input(self):
        """Handle input user of the category menu."""
        self.choice = input()
        if self.choice in self.category_menu.main_choice:
            self.input_choice = self.category_menu.main_choice[self.choice]
        return self.input_choice

    def show(self):
        """Handle the category menu."""
        self.category_menu.show()
