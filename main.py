"""Main."""

from application.controller.application import ApplicationController
from application.model.setup.cleaner import ProductCleaner
from application.model.setup.setupdb import initbase

RUNNING = True

while RUNNING:
    choice = input(
        "1- Installation de la base de données\n2- Application\n3- Quitter\n"
    )
    if choice == "1":
        # initbase.create_database()
        # initbase.use_database()
        print(
            "L'installation de la base de données peut prendre "
            "quelques minutes.\n"
            "Veuillez patienter..."
        )
        initbase.setup_database()
        productsCleaned = ProductCleaner()
        productsCleaned.get_products_from_off()
        print("La création de la base de données a bien été effectuée.")
    if choice == "2":
        application = ApplicationController()
        application.run()
    if choice == "3":
        RUNNING = False
    else:
        print("Veuillez saisir le numéro correspondant à l'option.")
