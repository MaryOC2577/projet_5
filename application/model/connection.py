"""Class connection."""

import mysql.connector
import requests


class Connection:
    """Class connection."""

    def __init__(self):
        """Initialize."""
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ma25Bo77Yi181",
            database="product",
        )
        self.products = []

    def get_cursor(self):
        """Connect to database."""
        return self.db.cursor()

    def close(self):
        """Close the connection."""
        self.db.close()

    def get_product_page(self, number_per_page: int) -> list:
        """Return a list of products JSON."""
        payload = {
            "search_terms": "",
            "sort_by": "unique_scans_n",
            "page_size": number_per_page,
            "content-length": 3000,
            "json": 1,
        }
        res = requests.get(
            "https://fr.openfoodfacts.org/cgi/search.pl?", params=payload
        )

        result = res.json()
        self.products.extend(result["products"])


connection = Connection()
