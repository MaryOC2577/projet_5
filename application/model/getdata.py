"""Get data from OpenFoodFacts."""

import json
import requests


class OpenFoodFacts:
    """Handle open food facts requests."""

    def __init__(self):
        """Init."""
        self.products = {}

    def get_product_page(self, number_per_page: int) -> list:
        """Return a list of products JSON."""
        payload = {
            "search_terms": "",
            "sort_by": "unique_scans_n",
            "page_size": number_per_page,
            "json": 1,
        }
        res = requests.get(
            "https://fr.openfoodfacts.org/cgi/search.pl?", params=payload
        )
        with open("result.json", "w") as f:
            json.dump(res.text, f)

        result = res.json()
        self.products = result["poducts"]
