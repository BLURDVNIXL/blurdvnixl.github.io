"""
════════════════════════════════════════════════════════════════
  OOP · Homme qui marche — Version Python + pygame
  Reproduction du jeu HTML en Python pur, architecture OOP
════════════════════════════════════════════════════════════════

  Architecture :
    AnimationMarcheur  ← gère l'animation (oscillation sin)
    Homme              ← personnage, compose AnimationMarcheur
    Marqueur           ← point de destination affiché
    HUD                ← affichage texte en temps réel
    Monde              ← fenêtre + boucle de jeu

  Lancer : pip install pygame && python jeu_oop.py
════════════════════════════════════════════════════════════════
"""

import pygame
import math
import sys


# ─────────────────────────────────────────────────────────────
# CLASSE 1 : AnimationMarcheur
# Responsabilité unique : gérer l'état de l'animation
# ─────────────────────────────────────────────────────────────
class AnimationMarcheur:
    """
    Gère UNIQUEMENT l'animation visuelle de la marche.
    Séparation des responsabilités : Homme délègue l'animation ici.
    """

    def __init__(self):
        self._active = False
        self.frame   = 0             # compteur de frame (avance si actif)
        self.VITESSE = 0.18          # vitesse d'oscillation

    # ── interface publique ──────────────────────────────────
    def jouer(self):
        """Démarre l'animation."""
        self._active = True

    def arreter(self):
        """Stoppe l'animation et remet le frame à 0."""
        self._active = False
        self.frame   = 0

    def update(self):
        """Appelée chaque frame — avance le compteur."""
        if self._active:
            self.frame += 1

    # ── calcul des angles ───────────────────────────────────
    def angle(self, phase: float = 0.0) -> float:
        """
        Retourne l'angle (degrés) d'un membre selon la phase.
        phase=0    → jambe gauche / bras droit
        phase=π    → jambe droite / bras gauche (opposé)
        """
        return math.sin(self.frame * self.VITESSE + phase) * 30

    def bob(self) -> float:
        """Petit effet de rebond vertical du corps."""
        return abs(math.sin(self.frame * self.VITESSE)) * 3

    # ── propriété ───────────────────────────────────────────
    @property
    def est_active(self) -> bool:
        return self._active

    def __repr__(self):
        return f"AnimationMarcheur(active={self._active}, frame={self.frame})"


# ─────────────────────────────────────────────────────────────
# CLASSE 2 : Homme
# Personnage principal — COMPOSE une AnimationMarcheur
# ─────────────────────────────────────────────────────────────
class Homme:
    """
    Personnage qui peut se déplacer de (a, b) vers (c, d).
    Délègue l'animation à AnimationMarcheur (composition has-a).
    """

    # attribut de classe — couleur partagée par toutes les instances
    COULEUR       = (0, 255, 200)
    COULEUR_SOMBRE = (0, 140, 110)
    VITESSE_PX    = 3               # pixels / frame

    def __init__(self, x: int, y: int):
        # attributs d'instance
        self.pos     = [x, y]       # position actuelle [px]
        self._marche = False
        self._cible  = None         # [cx, cy] destination

        # COMPOSITION : Homme "a" une AnimationMarcheur
        self.anim = AnimationMarcheur()

    # ── méthode principale ─────────────────────────────────
    def marcher(self, cx: int, cy: int) -> bool:
        """
        Ordonne le déplacement vers (cx, cy).
        Retourne False si déjà en déplacement (protection).
        Retourne True si le déplacement est lancé.
        """
        if self._marche:
            return False                   # déjà en marche → refus

        self._cible  = [cx, cy]
        self._marche = True
        self.anim.jouer()                  # délégation à AnimationMarcheur
        return True

    # ── mise à jour (appelée chaque frame) ────────────────
    def update(self):
        """Déplace progressivement l'homme vers la cible."""
        self.anim.update()

        if not self._marche:
            return

        dx   = self._cible[0] - self.pos[0]
        dy   = self._cible[1] - self.pos[1]
        dist = math.hypot(dx, dy)

        if dist <= self.VITESSE_PX:
            # arrivée
            self.pos     = self._cible[:]
            self._marche = False
            self.anim.arreter()            # délégation : stop animation
        else:
            # avance d'un pas normalisé
            self.pos[0] += int(dx / dist * self.VITESSE_PX)
            self.pos[1] += int(dy / dist * self.VITESSE_PX)

    # ── rendu ──────────────────────────────────────────────
    def dessiner(self, ecran: pygame.Surface):
        """Dessine le personnage avec membres animés."""
        x, y  = self.pos
        bob   = int(self.anim.bob())
        c     = self.COULEUR
        cs    = self.COULEUR_SOMBRE

        # helper : calcule le point d'arrivée d'un membre
        def membre_pt(angle_deg, ox, oy, longueur):
            rad = math.radians(angle_deg)
            return (
                int(x + ox + math.sin(rad) * longueur),
                int(y + oy + math.cos(rad) * longueur)
            )

        a1 = self.anim.angle(0)        # jambe G / bras D
        a2 = self.anim.angle(math.pi)  # jambe D / bras G (inversé)

        # ombre au sol
        pygame.draw.ellipse(ecran, (0, 60, 55),
                            (x - 15, y + 3, 30, 8))

        # ─ jambes
        pygame.draw.line(ecran, cs,
                         (x - 3, y - bob),
                         membre_pt(a1, -4, -bob, 30), 5)
        pygame.draw.line(ecran, c,
                         (x + 3, y - bob),
                         membre_pt(a2,  4, -bob, 30), 5)

        # ─ corps
        pygame.draw.line(ecran, c,
                         (x, y - bob),
                         (x, y - 32 - bob), 5)

        # ─ bras
        pygame.draw.line(ecran, c,
                         (x, y - 20 - bob),
                         membre_pt(a2, 0, -20 - bob, 22), 4)
        pygame.draw.line(ecran, cs,
                         (x, y - 20 - bob),
                         membre_pt(a1, 0, -20 - bob, 22), 4)

        # ─ tête
        pygame.draw.circle(ecran, c, (x, y - 42 - bob), 10)
        # yeux
        pygame.draw.circle(ecran, (10, 10, 20), (x - 3, y - 44 - bob), 2)
        pygame.draw.circle(ecran, (10, 10, 20), (x + 3, y - 44 - bob), 2)

    # ── propriétés ─────────────────────────────────────────
    @property
    def marche(self) -> bool:
        return self._marche

    @property
    def x(self) -> int:
        return self.pos[0]

    @property
    def y(self) -> int:
        return self.pos[1]

    def __repr__(self):
        return f"Homme(pos={self.pos}, marche={self._marche})"


# ─────────────────────────────────────────────────────────────
# CLASSE 3 : Marqueur
# Affiche le point de destination
# ─────────────────────────────────────────────────────────────
class Marqueur:
    """Indicateur visuel de la destination cible."""

    def __init__(self):
        self.pos   = None
        self.pulse = 0

    def placer(self, x: int, y: int):
        self.pos   = (x, y)
        self.pulse = 0

    def update(self):
        if self.pos:
            self.pulse += 0.08

    def dessiner(self, ecran: pygame.Surface):
        if not self.pos:
            return
        x, y   = self.pos
        rayon  = int(6 + math.sin(self.pulse) * 3)
        alpha  = int(180 + math.sin(self.pulse) * 60)
        couleur = (255, 100, 50)
        pygame.draw.circle(ecran, couleur, (x, y), rayon, 2)
        pygame.draw.circle(ecran, couleur, (x, y), 3)

    def effacer(self):
        self.pos = None


# ─────────────────────────────────────────────────────────────
# CLASSE 4 : HUD (Head-Up Display)
# Affiche les informations OOP en temps réel
# ─────────────────────────────────────────────────────────────
class HUD:
    """Affiche l'état des objets OOP à l'écran."""

    COULEUR_LABEL = (80, 180, 160)
    COULEUR_TRUE  = (100, 220, 100)
    COULEUR_FALSE = (180, 80, 60)
    COULEUR_VAL   = (220, 160, 60)

    def __init__(self, font: pygame.font.Font):
        self.font = font

    def dessiner(self, ecran: pygame.Surface, homme: "Homme"):
        x, y   = homme.pos
        marche = homme.marche

        # ligne de statut
        statut_couleur = self.COULEUR_TRUE if marche else self.COULEUR_FALSE
        statut_txt     = "true" if marche else "false"

        self._texte(ecran, f"pos = ({x}, {y})", 12, 12, self.COULEUR_LABEL)
        self._texte(ecran, f"marcher() = {statut_txt}", 12, 30, statut_couleur)
        self._texte(ecran, "← [CLIC GAUCHE] pour déplacer   [ESPACE] reset",
                    12, 48, (60, 100, 90))

        # bloc OOP
        self._texte(ecran, "OBJET : homme", 12, 80, (180, 180, 180))
        self._texte(ecran, f"  .anim.est_active = {homme.anim.est_active}",
                    12, 96, statut_couleur)
        self._texte(ecran, f"  .anim.frame      = {homme.anim.frame}",
                    12, 112, self.COULEUR_VAL)

    def _texte(self, ecran, txt, x, y, couleur):
        surf = self.font.render(txt, True, couleur)
        ecran.blit(surf, (x, y))


# ─────────────────────────────────────────────────────────────
# CLASSE 5 : Monde
# Gère la fenêtre pygame et la boucle principale
# ─────────────────────────────────────────────────────────────
class Monde:
    """
    Classe principale du jeu.
    Compose : Homme + Marqueur + HUD.
    Gère : événements, mise à jour, rendu.
    """

    LARGEUR = 900
    HAUTEUR = 500
    FPS     = 60
    SOL_Y   = 390    # ordonnée du sol

    COULEUR_BG    = (10, 10, 20)
    COULEUR_GRILLE = (22, 22, 42)
    COULEUR_SOL   = (0, 220, 200)

    def __init__(self):
        pygame.init()
        self.ecran  = pygame.display.set_mode((self.LARGEUR, self.HAUTEUR))
        pygame.display.set_caption("OOP · Homme qui marche — Python + pygame")
        self.clock  = pygame.time.Clock()

        # COMPOSITION — le monde possède ces objets
        self.homme   = Homme(80, self.SOL_Y)
        self.marqueur = Marqueur()
        self.hud     = HUD(pygame.font.SysFont("monospace", 13))

    # ── boucle de jeu ──────────────────────────────────────
    def boucle(self):
        """Boucle principale : events → update → render."""
        while True:
            self._gerer_evenements()
            self._update()
            self._rendu()
            self.clock.tick(self.FPS)

    def _gerer_evenements(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, _  = event.pos
                # déplacer l'homme vers (mx, SOL_Y)
                if self.homme.marcher(mx, self.SOL_Y):
                    self.marqueur.placer(mx, self.SOL_Y)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # reset : nouvel objet Homme
                    self.homme    = Homme(80, self.SOL_Y)
                    self.marqueur.effacer()

    def _update(self):
        self.homme.update()
        self.marqueur.update()

        # effacer le marqueur quand l'homme est arrivé
        if not self.homme.marche:
            self.marqueur.effacer()

    def _rendu(self):
        # fond
        self.ecran.fill(self.COULEUR_BG)

        # grille
        for i in range(0, self.LARGEUR, 60):
            pygame.draw.line(self.ecran, self.COULEUR_GRILLE,
                             (i, 0), (i, self.HAUTEUR))
        for j in range(0, self.HAUTEUR, 60):
            pygame.draw.line(self.ecran, self.COULEUR_GRILLE,
                             (0, j), (self.LARGEUR, j))

        # sol lumineux
        pygame.draw.line(self.ecran, self.COULEUR_SOL,
                         (0, self.SOL_Y), (self.LARGEUR, self.SOL_Y), 2)

        # marqueur de destination
        self.marqueur.dessiner(self.ecran)

        # personnage
        self.homme.dessiner(self.ecran)

        # HUD OOP
        self.hud.dessiner(self.ecran, self.homme)

        pygame.display.flip()


# ─────────────────────────────────────────────────────────────
# POINT D'ENTRÉE
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("════════════════════════════════════════")
    print("  OOP · Homme qui marche — Python")
    print("════════════════════════════════════════")
    print(f"Classe Homme instanciée      : {Homme(0,0)}")
    print(f"Classe AnimationMarcheur     : {AnimationMarcheur()}")
    print("Lancement du jeu...")
    print("[CLIC GAUCHE] déplacer | [ESPACE] reset")
    print("════════════════════════════════════════")

    Monde().boucle()