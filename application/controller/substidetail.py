"""Substitute detail controller menu."""

from application.view.substidetail import SubstiDetail
from application.model.substitute import SubstiModel
from application.model.category import Category


class SubstiDetailController:
    """Substitute detail controller menu."""

    def __init__(self, product):
        """Initialize substitute detail controller menu."""
        self.product = product
        self.subsittutes = SubstiModel()
        self.substidetail_view = SubstiDetail()
        self.cat_name = Category()

    def input(self):
        """Handle input user of the substi detail menu."""
        choice = input()
        return "get-substitute-" + choice + "-" + str(self.product[0])

    def save_confirmed(self):
        """Save substitute confirmed."""
        self.substidetail_view.save_confirmed()

    def show(self):
        """Handle the substitute menu."""
        self.substidetail_view.show(
            self.subsittutes.show(self.cat_name.get_name(self.product[0]))
        )
