"""Main."""


from application.model.setup.cleaner import ProductCleaner
from application.model.controller import Controller

productsCleaned = ProductCleaner()
controller = Controller()

productsCleaned.get_products_from_off()
controller.substitute()
