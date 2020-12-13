"""Procut cleaner."""


class ProductCleaner:
    """Product cleaner."""

    def clean_product(self, product: dict) -> dict:
        """Clean a product."""
        cleaned_product = {}
        cleaned_product["name"] = product.get("name")
        if not cleaned_product["name"]:
            return None
