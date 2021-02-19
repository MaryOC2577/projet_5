"""Substitute detail controller menu."""

from application.view.substidetail import SubstiDetail


class SubstiDetailController:
    """Substitute detail controller menu."""

    def __init__(self):
        """Initialize substitute detail controller menu."""
        self.substidetail_view = SubstiDetail()
        self.choice = ""

    def input(self):
        """Handle input user of the substi detail menu."""
        self.choice = input()
        return self.choice

    def save_confirmed(self):
        """Save substitute confirmed."""
        self.substidetail_view.save_confirmed()

    def show(self, products):
        """Handle the substitute menu."""
        self.substidetail_view.show(products)
