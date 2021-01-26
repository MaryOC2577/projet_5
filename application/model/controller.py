"""Controller."""

from application.view.mainmenu import Menu
from application.model.category import Category
from application.model.substitute import Substitute
from application.model.product import Product


class Controller:
    """Controls inputs from users."""

    def __init__(self):
        """Initialize the controller."""

    def show_substitute(self):
        """Return a product as a substitute."""
        menu = Menu()
        categories = Category()
        substitute = Substitute()
        product = Product()

        choice_one = input(menu.home())
        breakpoint()
        if choice_one == 1:
            menu.show_category()
            for cat in categories.get_all():
                print(cat.get("id") + " - " + cat.get("cat_name") + "\n")
            choice_cat = input()
            menu.show_product()
            for prod in product.get_fromcategory(choice_cat):
                print(prod.get("id") + " - " + prod.get("product_name" + "\n"))
            choice_prod = input()
            menu.show_substitute()
            print(substitute.get(choice_cat, choice_prod))
        else:
            if choice_one == 2:
                menu.show_substitute()

        # Requête SQL qui sélectionne toutes les catégories disponibles
        # L'utilisateur choisi une catégorie avec le numéro associé
        # Afficher les prduits de la catégorie sélectionnée
        # L'utilsateur choisi un produit avec le numéro associé
        # SQL sélectionne un substitut de même catégorie avec le meilleur nutriscore
        # Afficher le substitut
        # Demander à l'utilisateur s'il veut sauvegarder le substitut
        # Modifier produit d'origine avec id substitut dans champ subtitut de la table
