"""Test."""

import requests

payload = {
    "search_terms": "",
    # "search_tag": "brands",
    "sort_by": "unique_scans_n",
    "page_size": 100,
    "json": 1,
}

res = requests.get(
    "https://fr.openfoodfacts.org/cgi/search.pl?", params=payload
)

result = res.json()
products = result["products"]


for product in products:
    print(product["product_name"])
