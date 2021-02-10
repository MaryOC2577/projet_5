"""Main."""

from application.controller.application import ApplicationControler
from application.model.setup.cleaner import ProductCleaner
from application.model.setup.setupdb import initbase

RUNNING = True

while RUNNING:
    choice = input(
        "1- Création et installation de la base\n2- Application\n3- Quitter\n"
    )
    if choice == "1":
        initbase.setup_database()
        productsCleaned = ProductCleaner()
        productsCleaned.get_products_from_off()
    if choice == "2":
        application = ApplicationControler()
        application.run()
    if choice == "3":
        RUNNING = False
    else:
        print("Veuillez saisir le numéro correspondant à l'option.")
