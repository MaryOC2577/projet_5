"""Main."""


# from application.model.getdata import OpenFoodFacts
from application.model.productcleaner import ProductCleaner

# data_raw = OpenFoodFacts()
# data_raw.get_product_page(10)

# product_clean = ProductCleaner()
# product_clean.clean_product(data_raw.products)
# print(product_clean.cleaned_products)

productsCleaned = ProductCleaner()
productsCleaned.get_products_from_off()
