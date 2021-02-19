"""Favorites controller menu."""

from application.view.favorites import Favorites


class FavoritesController:
    """Favorites controller menu."""

    def __init__(self):
        """Initialize favorites controller menu."""
        self.favorites = Favorites()

    def show(self, substitutes):
        """Show the favorites substitutes."""
        self.favorites.show(substitutes)