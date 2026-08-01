class Produit:
    def __init__(self, nom, prix, stock):
        # Attributs privés avec le préfixe _
        self._nom = nom
        self._prix = prix
        self._stock = stock

    # Accesseurs (Getters)
    def get_nom(self):
        return self._nom

    def get_prix(self):
        return self._prix

    def get_stock(self):
        return self._stock

    # Mutateurs (Setters)
    def set_prix(self, prix):
        self._prix = prix

    def set_stock(self, stock):
        self._stock = stock

    def afficher_info(self):
        print(f"Nom : {self._nom} | Prix : {self._prix}€ | Stock : {self._stock}")

class ProduitPerissable(Produit):
    def __init__(self, nom, prix, stock, date_expiration):
        # Extension correcte de la classe parente
        super().__init__(nom, prix, stock)
        self._date_expiration = date_expiration

    # Accesseur et Mutateur spécifique
    def get_date_expiration(self):
        return self._date_expiration

    def set_date_expiration(self, date):
        self._date_expiration = date

    def afficher_info(self):
        # Redéfinition pour inclure la date d'expiration
        super().afficher_info()
        print(f"Date d'expiration : {self._date_expiration}")

# --- Test du programme ---
yaourt = ProduitPerissable("Yaourt nature", 2.5, 15, "15/05/2024")
print("Informations initiales du produit :\n ");yaourt.afficher_info();print("\n")

# Modification via mutateurs
yaourt.set_prix(2.75)
yaourt.set_date_expiration("20/05/2024")

# Affichage des informations mises à jour
print("Informations mises à jour du produit :\n "); yaourt.afficher_info() ; print("\n")