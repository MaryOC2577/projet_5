"""Favorites controller menu."""

from application.view.favorites import Favorites
from application.model.substitute import SubstiModel


class FavoritesController:
    """Favorites controller menu."""

    def __init__(self):
        """Initialize favorites controller menu."""
        self.favorites = Favorites()
        self.substitutes = SubstiModel()

    def show(self):
        """Show the favorites substitutes."""
        self.favorites.show(self.substitutes.get_list())
