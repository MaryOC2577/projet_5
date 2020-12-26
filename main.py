"""Main."""


from application.model.productcleaner import ProductCleaner

productsCleaned = ProductCleaner()
productsCleaned.get_products_from_off()
