"""Main."""


from application.model.setup.cleaner import ProductCleaner

productsCleaned = ProductCleaner()
productsCleaned.get_products_from_off()
