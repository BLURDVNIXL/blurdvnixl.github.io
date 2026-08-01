"""
=============================================================================
  CORRECTION TP — Représentation Graphique avec Matplotlib
  Sujet   : Étude de la suite de fonctions  S_n(x) = sum_{k=0}^{n} x^k / k!
  Auteur  : Daniel (MP2I — INP-HB)
  Objectif: Visualiser la convergence de S_n(x) vers exp(x) quand n → +∞
=============================================================================

RAPPEL MATHÉMATIQUE
-------------------
La suite S_n(x) = sum_{k=0}^{n} x^k / k!  est la somme partielle d'ordre n
du développement en série entière de exp(x).
On sait (résultat classique d'analyse) que :
    lim_{n → +∞} S_n(x) = e^x   pour tout réel x.

C'est ce que nous allons VÉRIFIER graphiquement.
"""

import numpy as np
import matplotlib.pyplot as plt
from math import factorial

# ===========================================================================
# FONCTION UTILITAIRE — calcul efficace de S_n(x)
# ===========================================================================

def S_n(x, n):
    """
    Calcule S_n(x) = sum_{k=0}^{n} x^k / k!

    Méthode retenue : méthode de Horner / accumulation itérative.
    On évite de recalculer x^k et k! à chaque étape en les mettant à jour
    de façon incrémentale :
        terme_k = terme_{k-1} * x / k
    C'est plus rapide et numériquement plus stable.

    Paramètres
    ----------
    x : float ou np.ndarray — point(s) d'évaluation
    n : int                 — ordre de troncature

    Retourne
    --------
    float ou np.ndarray     — valeur(s) de S_n(x)
    """
    terme = np.ones_like(np.asarray(x, dtype=float))  # terme k=0 : x^0/0! = 1
    somme = terme.copy()

    for k in range(1, n + 1):
        terme = terme * x / k   # mise à jour incrémentale : évite factorial(k)
        somme += terme

    return somme


# ===========================================================================
# PARAMÈTRES GLOBAUX DU SCRIPT
# ===========================================================================

# Valeurs de n utilisées dans le TP
N_MAX     = 100          # valeur maximale de n (axe des abscisses des nuages)
N_LISTE   = range(0, N_MAX + 1)   # n = 0, 1, 2, ..., 100

# Valeurs fixes de x demandées
X3 = 3
X6 = 6

# Palette de couleurs cohérente
COULEUR_Sn3  = "#2E86AB"   # bleu acier
COULEUR_Sn6  = "#E07B39"   # orange brûlé
COULEUR_D3   = "#E63946"   # rouge vif  (droite y = e^3)
COULEUR_D6   = "#6A0572"   # violet foncé (droite y = e^6)
COULEUR_FOND = "#F8F9FA"   # fond très léger

# Référence exacte
E3 = np.exp(3)   # ≈ 20.09
E6 = np.exp(6)   # ≈ 403.43


# ===========================================================================
# QUESTION 1 — Nuages de points : S_n(3) et S_n(6) en fonction de n
# ===========================================================================
# On fixe x et on fait varier n : la suite de fonctions devient une suite
# numérique.  On trace un NUAGE DE POINTS (pas de ligne) pour bien voir
# chaque terme.

# Calcul vectorisé : on évalue S_n(x) pour chaque n dans N_LISTE
valeurs_Sn3 = [S_n(X3, n) for n in N_LISTE]
valeurs_Sn6 = [S_n(X6, n) for n in N_LISTE]

fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
fig1.suptitle(
    r"Question 1 — Nuages de points : $S_n(3)$ et $S_n(6)$ pour $n \in [0, 100]$",
    fontsize=13, fontweight="bold"
)
fig1.patch.set_facecolor(COULEUR_FOND)

for ax in (ax1, ax2):
    ax.set_facecolor(COULEUR_FOND)
    ax.spines[["top", "right"]].set_visible(False)

# --- Graphe gauche : S_n(3) ---
ax1.scatter(list(N_LISTE), valeurs_Sn3,
            color=COULEUR_Sn3, s=18, alpha=0.8, label=r"$S_n(3)$", zorder=3)
ax1.axhline(E3, color=COULEUR_D3, linestyle="--", linewidth=1.4,
            label=rf"$e^3 \approx {E3:.2f}$")
ax1.set_xlabel("n", fontsize=11)
ax1.set_ylabel(r"$S_n(3)$", fontsize=11)
ax1.set_title(r"Suite $S_n(3)$", fontsize=11)
ax1.legend()
ax1.grid(True, linestyle=":", alpha=0.5)

# --- Graphe droite : S_n(6) ---
ax2.scatter(list(N_LISTE), valeurs_Sn6,
            color=COULEUR_Sn6, s=18, alpha=0.8, label=r"$S_n(6)$", zorder=3)
ax2.axhline(E6, color=COULEUR_D6, linestyle="--", linewidth=1.4,
            label=rf"$e^6 \approx {E6:.2f}$")
ax2.set_xlabel("n", fontsize=11)
ax2.set_ylabel(r"$S_n(6)$", fontsize=11)
ax2.set_title(r"Suite $S_n(6)$", fontsize=11)
ax2.legend()
ax2.grid(True, linestyle=":", alpha=0.5)

plt.tight_layout()
plt.savefig("q1_nuages_points.png", dpi=150, bbox_inches="tight")
plt.show()


# ===========================================================================
# QUESTION 2 — Droites horizontales D_3 : y = e^3  et  D_6 : y = e^6
# ===========================================================================
# Ces droites sont les valeurs limites vers lesquelles convergent les suites.
# On les trace seules, sur deux figures séparées.

n_axe = list(N_LISTE)   # abscisses = les indices n

fig2, (ax3, ax4) = plt.subplots(1, 2, figsize=(13, 4))
fig2.suptitle(
    r"Question 2 — Droites limites $D_3 : y = e^3$ et $D_6 : y = e^6$",
    fontsize=13, fontweight="bold"
)
fig2.patch.set_facecolor(COULEUR_FOND)

for ax in (ax3, ax4):
    ax.set_facecolor(COULEUR_FOND)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(True, linestyle=":", alpha=0.5)

# --- D_3 : y = e^3 (droite horizontale constante) ---
ax3.axhline(E3, color=COULEUR_D3, linewidth=2,
            label=rf"$D_3 : y = e^3 \approx {E3:.3f}$")
ax3.set_ylim(E3 - 5, E3 + 5)
ax3.set_xlabel("n")
ax3.set_title(r"$D_3 : y = e^3$", fontsize=11)
ax3.legend(fontsize=10)

# --- D_6 : y = e^6 ---
ax4.axhline(E6, color=COULEUR_D6, linewidth=2,
            label=rf"$D_6 : y = e^6 \approx {E6:.3f}$")
ax4.set_ylim(E6 - 50, E6 + 50)
ax4.set_xlabel("n")
ax4.set_title(r"$D_6 : y = e^6$", fontsize=11)
ax4.legend(fontsize=10)

plt.tight_layout()
plt.savefig("q2_droites_limites.png", dpi=150, bbox_inches="tight")
plt.show()


# ===========================================================================
# QUESTION 3 — Superposition droite + nuage  pour n=50 et n=100
# ===========================================================================
# On trace sur chaque sous-graphe  ENSEMBLE :
#   • le nuage de points S_n(x)  pour n ∈ [0, N_ref]
#   • la droite limite correspondante
# Cela permet de visualiser à quelle vitesse la suite rejoint sa limite.

def tracer_superposition(ax, N_ref, x_val, couleur_pts, couleur_droite, label_droite, e_val):
    """
    Trace sur l'axe `ax` le nuage S_n(x_val) pour n de 0 à N_ref
    + la droite horizontale y = e_val.

    Paramètres
    ----------
    ax           : axes matplotlib
    N_ref        : int    — valeur maximale de n
    x_val        : float  — valeur fixée de x (3 ou 6)
    couleur_pts  : str    — couleur des points
    couleur_droite : str  — couleur de la droite limite
    label_droite : str    — label LaTeX pour la droite
    e_val        : float  — valeur exacte e^x_val
    """
    n_range = list(range(0, N_ref + 1))
    valeurs = [S_n(x_val, n) for n in n_range]

    ax.scatter(n_range, valeurs, color=couleur_pts, s=14, alpha=0.75,
               label=rf"$S_n({x_val})$", zorder=3)
    ax.axhline(e_val, color=couleur_droite, linestyle="--", linewidth=1.6,
               label=label_droite, zorder=2)

    ax.set_xlabel("n", fontsize=10)
    ax.set_ylabel(rf"$S_n({x_val})$", fontsize=10)
    ax.legend(fontsize=9)
    ax.grid(True, linestyle=":", alpha=0.5)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_facecolor(COULEUR_FOND)


fig3, axes = plt.subplots(2, 2, figsize=(14, 9))
fig3.suptitle(
    r"Question 3 — Superposition $D_\alpha$ et $S_n(x)$ pour $n=50$ et $n=100$",
    fontsize=13, fontweight="bold"
)
fig3.patch.set_facecolor(COULEUR_FOND)

# Ligne 0 — n = 50
axes[0, 0].set_title(r"$n=50$ — $D_6$ et $S_n(6)$", fontsize=10)
tracer_superposition(axes[0, 0], 50, X6, COULEUR_Sn6, COULEUR_D6,
                     rf"$D_6 : y = e^6 \approx {E6:.1f}$", E6)

axes[0, 1].set_title(r"$n=50$ — $D_3$ et $S_n(3)$", fontsize=10)
tracer_superposition(axes[0, 1], 50, X3, COULEUR_Sn3, COULEUR_D3,
                     rf"$D_3 : y = e^3 \approx {E3:.2f}$", E3)

# Ligne 1 — n = 100
axes[1, 0].set_title(r"$n=100$ — $D_6$ et $S_n(6)$", fontsize=10)
tracer_superposition(axes[1, 0], 100, X6, COULEUR_Sn6, COULEUR_D6,
                     rf"$D_6 : y = e^6 \approx {E6:.1f}$", E6)

axes[1, 1].set_title(r"$n=100$ — $D_3$ et $S_n(3)$", fontsize=10)
tracer_superposition(axes[1, 1], 100, X3, COULEUR_Sn3, COULEUR_D3,
                     rf"$D_3 : y = e^3 \approx {E3:.2f}$", E3)

plt.tight_layout()
plt.savefig("q3_superposition.png", dpi=150, bbox_inches="tight")
plt.show()


# ===========================================================================
# QUESTION 4 — Commentaire : limite de S_n(3) quand n → 100
# ===========================================================================
# Vérification numérique : à quel point S_100(3) est-il proche de e^3 ?

val_S50_3  = S_n(X3, 50)
val_S100_3 = S_n(X3, 100)

print("=" * 60)
print("QUESTION 4 — Analyse numérique de S_n(3)")
print("=" * 60)
print(f"  e^3                   = {E3:.10f}")
print(f"  S_50(3)               = {val_S50_3:.10f}")
print(f"  |S_50(3)  - e^3|      = {abs(val_S50_3 - E3):.2e}")
print(f"  S_100(3)              = {val_S100_3:.10f}")
print(f"  |S_100(3) - e^3|      = {abs(val_S100_3 - E3):.2e}")
print()
print("CONCLUSION :")
print("  Graphiquement, les points S_n(3) rejoignent rapidement la droite")
print("  D_3 : y = e^3.  Dès n ≈ 15, la convergence est visuellement")
print("  indiscernable.  Numériquement, l'erreur est < 10^-10 dès n=50.")
print(f"  => lim_{{n→100}} S_n(3) ≈ e^3 ≈ {E3:.6f}")
print()


# ===========================================================================
# QUESTION 5 — Limite de S_n(x) quand n → +∞
# ===========================================================================
# Illustration sur une plage de x continus pour plusieurs valeurs de n.

print("=" * 60)
print("QUESTION 5 — Limite de S_n(x) quand n → +∞")
print("=" * 60)
print("  Par définition du développement en série entière,")
print("  la fonction exponentielle admet le DL entier :")
print()
print("      exp(x) = sum_{k=0}^{+∞} x^k / k!")
print()
print("  Cette série converge pour TOUT réel x (rayon de convergence = +∞).")
print("  Donc :  lim_{n → +∞} S_n(x) = exp(x) = e^x,  ∀x ∈ ℝ")
print()

# Graphe illustratif : S_n(x) pour x ∈ [-3, 6] et différentes valeurs de n
x_cont = np.linspace(-3, 6, 500)
ordres  = [1, 3, 5, 10, 20, 50]

fig5, ax5 = plt.subplots(figsize=(10, 6))
fig5.patch.set_facecolor(COULEUR_FOND)
ax5.set_facecolor(COULEUR_FOND)
ax5.spines[["top", "right"]].set_visible(False)

# Courbe exacte exp(x) — référence
ax5.plot(x_cont, np.exp(x_cont), color="black", linewidth=2.5,
         linestyle="-", label=r"$e^x$ (exacte)", zorder=10)

# Approximations successives S_n(x)
palette = plt.cm.plasma(np.linspace(0.15, 0.85, len(ordres)))

for n, col in zip(ordres, palette):
    y = S_n(x_cont, n)
    # On clippe pour ne pas écraser le graphe quand S_n diverge loin de e^x
    ax5.plot(x_cont, np.clip(y, -50, 500), color=col,
             linewidth=1.4, alpha=0.85, label=rf"$S_{{n={n}}}(x)$")

ax5.set_ylim(-10, 120)
ax5.set_xlim(-3, 6)
ax5.set_xlabel("x", fontsize=12)
ax5.set_ylabel(r"$S_n(x)$", fontsize=12)
ax5.set_title(
    r"Question 5 — Convergence de $S_n(x)$ vers $e^x$ quand $n \to +\infty$",
    fontsize=12, fontweight="bold"
)
ax5.legend(fontsize=9, ncol=2, loc="upper left")
ax5.grid(True, linestyle=":", alpha=0.5)

plt.tight_layout()
plt.savefig("q5_convergence_globale.png", dpi=150, bbox_inches="tight")
plt.show()

print("Tous les graphes ont été générés et sauvegardés.")