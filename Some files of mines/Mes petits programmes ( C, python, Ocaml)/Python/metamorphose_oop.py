"""
=============================================================
 CONCEPT OOP : Un objet ne peut pas changer de classe
=============================================================

Un objet créé à partir d'une classe lui appartient pour toujours.
Ses attributs peuvent évoluer, mais sa classe reste fixe.

Métaphore : la chenille ne "devient" pas papillon au sens technique —
on crée un nouvel objet Papillon à partir des données de la chenille.
=============================================================
"""

# ─────────────────────────────────────────────
# CLASSE DE BASE : Insecte (héritage partagé)
# ─────────────────────────────────────────────
class Insecte:
    """Classe parente commune à Chenille et Papillon."""

    def __init__(self, nom: str):
        self.nom = nom

    def se_presenter(self):
        print(f"[{type(self).__name__}] Je m'appelle {self.nom}.")

    def verifier_classe(self):
        print(f"→ Je suis une instance de : {type(self).__name__}")
        print(f"→ isinstance(Insecte) : {isinstance(self, Insecte)}")


# ─────────────────────────────────────────────
# CLASSE : Chenille
# ─────────────────────────────────────────────
class Chenille(Insecte):
    """Une chenille qui peut évoluer, mais reste une Chenille."""

    def __init__(self, nom: str):
        super().__init__(nom)
        self.stade = "chenille"
        self.energie = 100

    def manger(self):
        self.energie += 20
        print(f"{self.nom} mange des feuilles. Énergie : {self.energie}")

    def se_transformer(self) -> "Papillon":
        """
        La chenille ne DEVIENT pas un papillon.
        Elle crée et retourne un NOUVEL objet Papillon.
        L'objet chenille reste intact et inchangé.
        """
        if self.energie < 80:
            print(f"{self.nom} n'a pas assez d'énergie pour se transformer !")
            return None

        print(f"\n🐛 {self.nom} tisse son cocon...")
        print(f"🫘 {self.nom} entre en chrysalide...")
        print(f"🦋 Un papillon émerge du cocon !\n")

        # On crée un NOUVEAU objet — la chenille ne change pas de classe
        return Papillon(nom=self.nom, origine=self)

    def verifier_classe(self):
        super().verifier_classe()
        print(f"→ isinstance(Chenille) : {isinstance(self, Chenille)}")
        print(f"→ isinstance(Papillon) : {isinstance(self, Papillon)}")


# ─────────────────────────────────────────────
# CLASSE : Papillon
# ─────────────────────────────────────────────
class Papillon(Insecte):
    """Un papillon né de la transformation d'une chenille."""

    def __init__(self, nom: str, origine: Chenille = None):
        super().__init__(nom)
        self.stade = "papillon"
        self.origine = origine  # référence à la chenille d'origine (optionnel)

    def voler(self):
        print(f"🦋 {self.nom} vole gracieusement dans le ciel !")

    def afficher_origine(self):
        if self.origine:
            print(f"{self.nom} était autrefois une chenille.")
            print(f"  Classe d'origine : {type(self.origine).__name__}")
            print(f"  Même objet ? {self is self.origine}")  # → False !
        else:
            print(f"{self.nom} n'a pas d'origine connue.")

    def verifier_classe(self):
        super().verifier_classe()
        print(f"→ isinstance(Chenille) : {isinstance(self, Chenille)}")
        print(f"→ isinstance(Papillon) : {isinstance(self, Papillon)}")


# ─────────────────────────────────────────────
# DÉMONSTRATION
# ─────────────────────────────────────────────
if __name__ == "__main__":

    separateur = "\n" + "=" * 55

    # 1. Création de la chenille
    print(separateur)
    print(" ÉTAPE 1 : Création de la chenille")
    print("=" * 55)
    chenille = Chenille("Caterpillar")
    chenille.se_presenter()
    chenille.verifier_classe()

    # 2. La chenille évolue (ses attributs changent, pas sa classe)
    print(separateur)
    print(" ÉTAPE 2 : La chenille évolue (mange)")
    print("=" * 55)
    chenille.manger()
    chenille.manger()
    print(f"Stade actuel : {chenille.stade}")
    chenille.verifier_classe()  # toujours une Chenille !

    # 3. Transformation → création d'un nouvel objet Papillon
    print(separateur)
    print(" ÉTAPE 3 : Transformation (nouvel objet créé)")
    print("=" * 55)
    papillon = chenille.se_transformer()

    # 4. Vérification que la chenille N'A PAS changé de classe
    print(separateur)
    print(" ÉTAPE 4 : La chenille existe toujours, inchangée")
    print("=" * 55)
    chenille.se_presenter()
    chenille.verifier_classe()
    print(f"Stade de la chenille : {chenille.stade}")  # toujours "chenille"

    # 5. Le papillon est un objet distinct
    print(separateur)
    print(" ÉTAPE 5 : Le papillon est un objet distinct")
    print("=" * 55)
    papillon.se_presenter()
    papillon.verifier_classe()
    papillon.afficher_origine()
    papillon.voler()

    # 6. Preuve finale
    print(separateur)
    print(" CONCLUSION : Ce sont deux objets différents")
    print("=" * 55)
    print(f"id(chenille)  = {id(chenille)}")
    print(f"id(papillon)  = {id(papillon)}")
    print(f"Même objet ?  {chenille is papillon}")  # → False
    print(f"\nLa chenille est toujours une Chenille : {isinstance(chenille, Chenille)}")
    print(f"Le papillon est toujours un Papillon  : {isinstance(papillon, Papillon)}")
