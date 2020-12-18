"""Test."""

import json
import requests

payload = {
    "search_terms": "",
    "sort_by": "unique_scans_n",
    "page_size": 1,
    "json": 1,
}

res = requests.get(
    "https://fr.openfoodfacts.org/cgi/search.pl?", params=payload
)

with open("result.json", "w") as f:
    json.dump(res.text, f)

result = res.json()
products = result["products"]


for product in products:
    print(product["name"])
