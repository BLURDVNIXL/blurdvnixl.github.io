"""
=============================================================================
  CORRECTION TP — Calcul Scientifique : Termes et limites de suites
  Auteur : Daniel (MP2I — INP-HB)
=============================================================================

Ce TP couvre 6 exercices progressifs sur :
  - Suites définies par récurrence (linéaire, non-linéaire)
  - Moyennes arithmético-géométriques
  - Séries (cos, ln2)
  - Probabilités (paradoxe des anniversaires)

Pour chaque exercice : explication mathématique + code Python commenté + test.
"""

import math


# ===========================================================================
# EXERCICE 1 ★★ — Suite d'ordre 2 : u_{n+2} = u_{n+1} + 2*u_n + (-1)^n
# ===========================================================================
"""
ANALYSE MATHÉMATIQUE
--------------------
La relation de récurrence est d'ordre 2 : pour calculer u_n, on a besoin
des deux termes précédents u_{n-1} et u_{n-2}.

Stratégie : on itère depuis n=2 jusqu'au rang voulu, en ne conservant
que les deux derniers termes en mémoire (on n'a pas besoin de toute la liste).

    u_{k+2} = u_{k+1} + 2*u_k + (-1)^k

Cas de base : si n=0 → renvoyer u0 ; si n=1 → renvoyer u1.
"""

def terme_suite_rec2(u0, u1, n):
    """
    Calcule u_n pour la suite définie par :
        u_{n+2} = u_{n+1} + 2*u_n + (-1)^n,   n ∈ ℕ

    Paramètres
    ----------
    u0, u1 : float  — conditions initiales
    n      : int    — rang souhaité (n ≥ 1)

    Retourne
    --------
    float — valeur de u_n

    Complexité : O(n) en temps, O(1) en espace (seulement 2 variables)
    """
    if n == 0:
        return u0
    if n == 1:
        return u1

    # On fait "glisser" une fenêtre de taille 2
    a, b = u0, u1           # a = u_{k}, b = u_{k+1}
    for k in range(0, n - 1):
        # On calcule u_{k+2} = u_{k+1} + 2*u_k + (-1)^k
        c = b + 2 * a + (-1) ** k
        a, b = b, c         # décalage : (u_k, u_{k+1}) → (u_{k+1}, u_{k+2})

    return b   # après n-1 itérations, b = u_n


# --- TEST ---
print("=" * 60)
print("EXERCICE 1 — Suite d'ordre 2")
print("=" * 60)
u0, u1 = 1, 2
for n in range(8):
    print(f"  u_{n} = {terme_suite_rec2(u0, u1, n):.4f}")
print()


# ===========================================================================
# EXERCICE 2 ★★ — Moyennes arithmético-géométriques (AGM)
# ===========================================================================
"""
ANALYSE MATHÉMATIQUE
--------------------
On définit deux suites entrelacées :
    a_{n+1} = sqrt(a_n * b_n)   (moyenne géométrique)
    b_{n+1} = (a_n + b_n) / 2   (moyenne arithmétique)

Propriétés remarquables :
  • a_n < b_n pour tout n (car a_0 < b_0)
  • Les deux suites sont monotones et bornées → elles convergent
  • Elles convergent vers la MÊME limite : la moyenne arithmético-géométrique
    AGM(a_0, b_0), qui n'a pas d'expression analytique simple en général.
  • La convergence est TRÈS rapide (quadratique : le nombre de décimales
    exactes double à chaque itération).

IMPORTANT : on ne peut pas calculer a_n et b_n indépendamment —
les deux récurrences sont COUPLÉES. On les met à jour simultanément.
"""

def agm_termes(a0, b0, n):
    """
    Calcule (a_n, b_n) pour les suites arithmético-géométriques.

    Paramètres
    ----------
    a0, b0 : float  — valeurs initiales avec 0 < a0 < b0
    n      : int    — rang voulu

    Retourne
    --------
    (float, float) — (a_n, b_n)
    """
    assert 0 < a0 < b0, "On doit avoir 0 < a0 < b0"

    a, b = a0, b0
    for _ in range(n):
        # Mise à jour simultanée (crucial : ne pas utiliser le nouveau a
        # pour calculer le nouveau b)
        a_new = math.sqrt(a * b)     # moyenne géométrique
        b_new = (a + b) / 2          # moyenne arithmétique
        a, b = a_new, b_new

    return a, b


# --- TEST ---
print("=" * 60)
print("EXERCICE 2 — Moyennes arithmético-géométriques")
print("=" * 60)
a0, b0 = 1.0, 2.0
print(f"  Conditions initiales : a0 = {a0}, b0 = {b0}")
for n in range(8):
    a, b = agm_termes(a0, b0, n)
    print(f"  n={n} : a_n = {a:.10f}   b_n = {b:.10f}   |b-a| = {abs(b-a):.2e}")
print(f"\n  Convergence vers AGM({a0},{b0}) ≈ {agm_termes(a0, b0, 50)[0]:.10f}")
print()


# ===========================================================================
# EXERCICE 3 ★★ — Suite non-linéaire : u_{n+1} = 4 - u_n²/9, limite = 3
# ===========================================================================
"""
ANALYSE MATHÉMATIQUE
--------------------
La suite est définie par u_{n+1} = f(u_n) avec f(x) = 4 - x²/9.
On nous dit que u_n → 3 (point fixe : f(3) = 4 - 9/9 = 3 ✓).

On cherche le premier rang N tel que |u_N - 3| ≤ ε.
C'est une recherche d'un seuil de convergence : on itère jusqu'à
satisfaire la condition d'arrêt.

Subtilité : on utilise une boucle while (pas for) car on ne sait pas
à l'avance combien d'itérations seront nécessaires.
"""

def premier_rang_convergence(u0, eps):
    """
    Calcule le premier rang n tel que |u_n - 3| ≤ ε
    pour la suite u_{n+1} = 4 - u_n²/9, u_0 ∈ ]-12 ; 12[.

    Paramètres
    ----------
    u0  : float — valeur initiale dans ]-12, 12[
    eps : float — précision souhaitée (ε > 0)

    Retourne
    --------
    int — premier rang de convergence à ε près
    """
    assert -12 < u0 < 12, "u0 doit être dans ]-12 ; 12["
    assert eps > 0, "ε doit être strictement positif"

    u = u0
    n = 0
    # On itère TANT QUE la condition n'est pas satisfaite
    while abs(u - 3) > eps:
        u = 4 - u ** 2 / 9    # relation de récurrence
        n += 1

    return n


# --- TEST avec u0=0, ε=10^{-3} ---
print("=" * 60)
print("EXERCICE 3 — Premier rang de convergence")
print("=" * 60)
u0_test, eps_test = 0, 1e-3
rang = premier_rang_convergence(u0_test, eps_test)
print(f"  u0 = {u0_test}, ε = {eps_test}")
print(f"  Premier rang n tel que |u_n - 3| ≤ ε : n = {rang}")

# Vérification : affichage des derniers termes
u = u0_test
for i in range(rang + 1):
    if i >= rang - 2:
        print(f"  u_{i} = {u:.8f}  (|u_{i} - 3| = {abs(u-3):.2e})")
    u = 4 - u**2 / 9
print()


# ===========================================================================
# EXERCICE 4 ★★★ — Série de cos : S_n(x) = Σ_{k=0}^{n} (-1)^k x^{2k} / (2k)!
# ===========================================================================
"""
ANALYSE MATHÉMATIQUE
--------------------
On reconnaît le développement en série entière du COSINUS :
    cos(x) = Σ_{k=0}^{+∞} (-1)^k x^{2k} / (2k)!

Donc S_n(x) → cos(x) quand n → +∞.

Pour ne pas utiliser ** (puissance), on utilise la mise à jour incrémentale :
    terme_k = terme_{k-1} * (-x²) / ((2k)(2k-1))

En effet :
    terme_k = (-1)^k * x^{2k} / (2k)!
    terme_k / terme_{k-1} = (-1) * x² / ((2k) * (2k-1))
→ multiplication par (-x²) et division par (2k)(2k-1).

C'est la méthode de Horner adaptée aux séries alternées.
"""

def sommecos(x, n):
    """
    Calcule S_n(x) = Σ_{k=0}^{n} (-1)^k * x^{2k} / (2k)!
    SANS utiliser l'opérateur ** (puissance).

    Méthode : mise à jour incrémentale du terme général.

    Paramètres
    ----------
    x : float — point d'évaluation
    n : int   — ordre de troncature

    Retourne
    --------
    float — valeur approchée de cos(x)
    """
    terme = 1.0        # terme k=0 : (-1)^0 * x^0 / 0! = 1
    somme = terme
    x2 = x * x        # x² calculé UNE SEULE FOIS (pas de **)

    for k in range(1, n + 1):
        # terme_k = terme_{k-1} * (-x²) / ((2k)(2k-1))
        terme = terme * (-x2) / ((2 * k) * (2 * k - 1))
        somme += terme

    return somme


# --- TEST comparatif S_n(x) vs cos(x) ---
print("=" * 60)
print("EXERCICE 4 — Série du cosinus : sommecos(x, n)")
print("=" * 60)
print(f"  {'x':>6}  {'n':>4}  {'S_n(x)':>18}  {'cos(x)':>18}  {'erreur':>12}")
print("  " + "-" * 65)
test_cases = [(0.5, 5), (1.0, 8), (math.pi, 15), (3.14, 10), (10.0, 50)]
for x_val, n_val in test_cases:
    sn   = sommecos(x_val, n_val)
    ref  = math.cos(x_val)
    err  = abs(sn - ref)
    print(f"  {x_val:>6.2f}  {n_val:>4}  {sn:>18.10f}  {ref:>18.10f}  {err:>12.2e}")
print()


# ===========================================================================
# EXERCICE 5 ★★ — Série alternée : S_n = Σ_{k=1}^{n} (-1)^{k+1}/k → ln(2)
# ===========================================================================
"""
ANALYSE MATHÉMATIQUE
--------------------
C'est la série harmonique alternée. On sait que :
    S_n = 1 - 1/2 + 1/3 - 1/4 + ... + (-1)^{n+1}/n → ln(2)

Et on dispose de l'encadrement : |S_n - ln(2)| ≤ 1/(n+1).

Donc pour avoir |S_n - ln(2)| ≤ ε, il SUFFIT d'avoir 1/(n+1) ≤ ε,
soit n ≥ 1/ε - 1.

QUESTION 1a — Rang théorique :
    n_théo = ceil(1/ε - 1)  = ceil(1/ε) - 1  (en pratique ⌊1/ε⌋ suffit)

QUESTION 1b — Fonction ln2(ε) :
    On calcule S_n pour ce rang théorique.

QUESTION 2 — Plus petit rang EFFECTIF :
    Le rang théorique est une borne SUFFISANTE mais pas nécessairement
    minimale. On cherche le vrai premier rang où |S_n - ln(2)| ≤ ε.
    Comme la série alterne, la convergence est oscillante mais
    l'encadrement garantit que le vrai rang ≤ rang théorique.
"""

def ln2(eps):
    """
    Calcule une valeur approchée de ln(2) à ε près.

    Méthode : utilise la borne |S_n - ln(2)| ≤ 1/(n+1) pour déterminer
    un rang n suffisant, puis calcule S_n.

    Paramètres
    ----------
    eps : float — précision souhaitée (ε > 0)

    Retourne
    --------
    float — valeur approchée de ln(2) à ε près
    """
    # Rang suffisant : 1/(n+1) ≤ ε  ⟺  n ≥ 1/ε - 1
    n = math.ceil(1 / eps - 1)

    # Calcul de S_n = Σ_{k=1}^{n} (-1)^{k+1} / k
    # Astuce : on accumule directement sans stocker les termes
    somme = 0.0
    for k in range(1, n + 1):
        somme += (-1) ** (k + 1) / k

    return somme


def rang_effectif_ln2(eps):
    """
    Calcule le PLUS PETIT rang n tel que |S_n - ln(2)| ≤ ε.

    Contrairement à ln2(), on ne se base pas sur la borne théorique
    mais on vérifie directement la condition à chaque pas.

    Paramètres
    ----------
    eps : float — précision souhaitée

    Retourne
    --------
    int — plus petit rang satisfaisant la condition
    """
    ref   = math.log(2)     # valeur exacte de ln(2)
    somme = 0.0
    n     = 0

    while True:
        n += 1
        somme += (-1) ** (n + 1) / n
        if abs(somme - ref) <= eps:
            return n


# --- TEST avec ε = 10^{-6} ---
print("=" * 60)
print("EXERCICE 5 — Série alternée vers ln(2)")
print("=" * 60)
eps5 = 1e-6
ref_ln2 = math.log(2)

print(f"  Référence : ln(2) = {ref_ln2:.10f}")
print()

# Question 1
approx = ln2(eps5)
n_theo = math.ceil(1 / eps5 - 1)
print(f"  Q1 — ε = {eps5}")
print(f"       Rang théorique suffisant : n = {n_theo}")
print(f"       Approximation S_n        = {approx:.10f}")
print(f"       Erreur réelle            = {abs(approx - ref_ln2):.2e}")
print()

# Question 2
n_reel = rang_effectif_ln2(eps5)
print(f"  Q2 — Plus petit rang effectif : n = {n_reel}")
print(f"       Commentaire : le rang effectif ({n_reel}) est INFÉRIEUR au rang")
print(f"       théorique ({n_theo}) car la borne 1/(n+1) est une majoration")
print(f"       PESSIMISTE. Le critère est souvent satisfait bien avant.")
print()


# ===========================================================================
# EXERCICE 6 ★★ — Paradoxe des anniversaires
# ===========================================================================
"""
ANALYSE MATHÉMATIQUE
--------------------
Dans une classe de n élèves, la probabilité qu'au moins deux élèves
partagent le même anniversaire est :

    p_n = 1 - ∏_{k=0}^{n-1} (1 - k/365)

Interprétation : (1 - k/365) est la probabilité que le (k+1)-ième élève
ait un anniversaire DIFFÉRENT de tous les précédents.
Le produit donne la probabilité que TOUS soient différents.
p_n = 1 - P(tous différents).

QUESTION 2a — Relation de récurrence :
    p_{n+1} = 1 - (1 - p_n)(1 - n/365)

Preuve :
    (1 - p_{n+1}) = ∏_{k=0}^{n} (1 - k/365)
                  = [∏_{k=0}^{n-1} (1 - k/365)] * (1 - n/365)
                  = (1 - p_n) * (1 - n/365)
    Donc p_{n+1} = 1 - (1 - p_n)(1 - n/365)  ✓

Cette formulation récurrente est PLUS EFFICACE pour la question 2b car
elle évite de recalculer tout le produit à chaque étape.
"""

def proba_anniversaire(n):
    """
    Calcule p_n = probabilité qu'au moins 2 élèves sur n partagent
    un anniversaire.

    Méthode directe : produit cumulé.

    Paramètres
    ----------
    n : int — nombre d'élèves ∈ [1 ; 365]

    Retourne
    --------
    float — p_n ∈ [0, 1]
    """
    assert 1 <= n <= 365, "n doit être dans [1 ; 365]"

    # P(tous différents) = ∏_{k=0}^{n-1} (1 - k/365)
    produit = 1.0
    for k in range(n):
        produit *= (1 - k / 365)

    return 1 - produit


def seuil_anniversaire(x):
    """
    Calcule le plus petit n ∈ [1;365] tel que p_n ≥ x,
    en utilisant la relation de récurrence p_{n+1} = 1-(1-p_n)(1-n/365).

    Paramètres
    ----------
    x : float — seuil de probabilité dans ]0 ; 1[

    Retourne
    --------
    int — plus petit n tel que p_n ≥ x
    """
    assert 0 < x < 1, "x doit être dans ]0 ; 1["

    p = 0.0       # p_1 = 0 (avec 1 seul élève, impossible d'avoir un doublon)
    n = 1

    # On utilise la récurrence : plus besoin de recalculer tout le produit
    while p < x and n <= 365:
        # p_{n+1} = 1 - (1 - p_n)(1 - n/365)
        p = 1 - (1 - p) * (1 - n / 365)
        n += 1

    return n - 1   # n a été incrémenté une fois de trop après la condition


# --- TESTS ---
print("=" * 60)
print("EXERCICE 6 — Paradoxe des anniversaires")
print("=" * 60)

# Question 1 : quelques valeurs de p_n
print("  Q1 — Valeurs de p_n :")
for n_val in [10, 20, 23, 30, 40, 50, 57, 70]:
    p = proba_anniversaire(n_val)
    print(f"    p_{n_val:3d} = {p:.4f}  ({p*100:.1f}%)")

print()

# Question 2b : seuil x = 0.99
x_seuil = 0.99
n_seuil = seuil_anniversaire(x_seuil)
p_check  = proba_anniversaire(n_seuil)
print(f"  Q2b — Plus petit n tel que p_n ≥ {x_seuil} :")
print(f"    n = {n_seuil}")
print(f"    Vérification : p_{n_seuil} = {p_check:.6f}")
print()
print("  COMMENTAIRE SUR LE PARADOXE :")
print("  Il suffit de 23 élèves pour avoir plus de 50% de chances")
n_50 = seuil_anniversaire(0.5)
p_50 = proba_anniversaire(n_50)
# Note : seuil_anniversaire(0.5) renvoie 23 car p_22≈47.6% < 50% et p_23≈50.7% ≥ 50%
print(f"  que deux partagent un anniversaire (p_{n_50} ≈ {p_50:.4f}).")
print("  Ce résultat est contre-intuitif car notre cerveau pense")
print("  à UNE personne précise, alors qu'on compare toutes les paires.")
print(f"  Pour 99% de chances, il faut seulement {n_seuil} élèves.")
print()
print("=" * 60)
print("Tous les exercices terminés.")
print("=" * 60)