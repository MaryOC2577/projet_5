"""Main."""

from application.controller.application import ApplicationControler

# from application.model.setup.cleaner import ProductCleaner

# productsCleaned = ProductCleaner()
application = ApplicationControler()

# productsCleaned.get_products_from_off()
application.run()
