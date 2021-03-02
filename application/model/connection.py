"""Class connection."""

import mysql.connector
import requests
from config import PASSWORD, USER_NAME


class Connection:
    """Class connection."""

    def __init__(self):
        """Initialize."""
        self.db = mysql.connector.connect(
            host="localhost",
            user=USER_NAME,
            password=PASSWORD,
            database="product",
        )
        self.products = []

    def get_cursor(self):
        """Connect to database."""
        return self.db.cursor(buffered=True)

    def close(self):
        """Close the connection."""
        self.db.close()

    def get_product_page(self, number_of_page: int) -> list:
        """Return a list of products JSON."""
        payload = {
            "search_terms": "",
            "sort_by": "unique_scans_n",
            "page_size": 1000,
            "page": number_of_page,
            # "content-length": 3000,
            "json": 1,
        }
        res = requests.get(
            "https://fr.openfoodfacts.org/cgi/search.pl?", params=payload
        )

        result = res.json()
        self.products.extend(result["products"])


connection = Connection()
