"""
=============================================================================
  CORRECTION TP — Calcul Scientifique : Termes et limites de suites
  Refactorisé avec NumPy
=============================================================================
"""

import math
import numpy as np


# ===========================================================================
# EXERCICE 1 ★★ — Suite d'ordre 2 : u_{n+2} = u_{n+1} + 2*u_n + (-1)^n
# ===========================================================================

def terme_suite_rec2(u0, u1, n):
    """
    Calcule u_n pour la suite définie par :
        u_{n+2} = u_{n+1} + 2*u_n + (-1)^n

    Avec NumPy : on précalcule le vecteur des (-1)^k d'un coup.
    """
    if n == 0:
        return u0
    if n == 1:
        return u1

    # Vecteur des signes (-1)^k pour k = 0 .. n-2  (n-1 valeurs)
    signes = (-1) ** np.arange(n - 1)   # np.arange évite la boucle sur k

    a, b = u0, u1
    for s in signes:
        c = b + 2 * a + s
        a, b = b, c

    return b


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

def agm_termes(a0, b0, n):
    """
    Calcule (a_n, b_n) des suites arithmético-géométriques.

    Avec NumPy : np.sqrt pour la moyenne géométrique (robuste, vectorisé).
    La mise à jour simultanée reste indispensable (suites couplées).
    """
    assert 0 < a0 < b0, "On doit avoir 0 < a0 < b0"

    # On stocke l'historique dans deux tableaux numpy
    a_hist = np.empty(n + 1)
    b_hist = np.empty(n + 1)
    a_hist[0], b_hist[0] = a0, b0

    a, b = a0, b0
    for i in range(n):
        a_new = np.sqrt(a * b)       # moyenne géométrique
        b_new = (a + b) / 2          # moyenne arithmétique
        a, b = a_new, b_new
        a_hist[i + 1] = a
        b_hist[i + 1] = b

    return a_hist[n], b_hist[n]


# --- TEST ---
print("=" * 60)
print("EXERCICE 2 — Moyennes arithmético-géométriques")
print("=" * 60)
a0, b0 = 1.0, 2.0
print(f"  Conditions initiales : a0 = {a0}, b0 = {b0}")
for n in range(8):
    a, b = agm_termes(a0, b0, n)
    print(f"  n={n} : a_n = {a:.10f}   b_n = {b:.10f}   |b-a| = {np.abs(b-a):.2e}")
print(f"\n  Convergence vers AGM({a0},{b0}) ≈ {agm_termes(a0, b0, 50)[0]:.10f}")
print()


# ===========================================================================
# EXERCICE 3 ★★ — Suite non-linéaire : u_{n+1} = 4 - u_n²/9, limite = 3
# ===========================================================================

def premier_rang_convergence(u0, eps):
    """
    Calcule le premier rang n tel que |u_n - 3| ≤ ε.

    Avec NumPy : np.abs à la place de abs().
    La boucle while reste nécessaire (condition d'arrêt adaptative).
    """
    assert -12 < u0 < 12, "u0 doit être dans ]-12 ; 12["
    assert eps > 0, "ε doit être strictement positif"

    u = np.float64(u0)
    n = 0
    while np.abs(u - 3) > eps:
        u = 4 - u ** 2 / 9
        n += 1

    return n


# --- TEST ---
print("=" * 60)
print("EXERCICE 3 — Premier rang de convergence")
print("=" * 60)
u0_test, eps_test = 0, 1e-3
rang = premier_rang_convergence(u0_test, eps_test)
print(f"  u0 = {u0_test}, ε = {eps_test}")
print(f"  Premier rang n tel que |u_n - 3| ≤ ε : n = {rang}")

u = np.float64(u0_test)
for i in range(rang + 1):
    if i >= rang - 2:
        print(f"  u_{i} = {u:.8f}  (|u_{i} - 3| = {np.abs(u-3):.2e})")
    u = 4 - u**2 / 9
print()


# ===========================================================================
# EXERCICE 4 ★★★ — Série de cos : S_n(x) = Σ_{k=0}^{n} (-1)^k x^{2k} / (2k)!
# ===========================================================================

def sommecos(x, n):
    """
    Calcule S_n(x) = Σ_{k=0}^{n} (-1)^k * x^{2k} / (2k)!
    SANS opérateur ** sur x (mise à jour incrémentale du terme).

    Avec NumPy : on précalcule tous les factoriels avec np.cumprod,
    et les puissances de x² par accumulation vectorisée.

    terme_k = (-1)^k * x^{2k} / (2k)!

    → termes = signes * x2_powers / factoriels_pairs
    """
    x2 = np.float64(x) * np.float64(x)   # x² sans **

    k_vals = np.arange(n + 1)             # [0, 1, 2, ..., n]

    # (-1)^k
    signes = (-1.0) ** k_vals             # np.arange → opération vectorisée

    # x^{2k} sans ** sur x : produit cumulé de x²
    # x^0=1, x^2, x^4, ... = cumprod([1, x², x², ..., x²])
    x2_rep = np.ones(n + 1)
    x2_rep[1:] = x2                       # [1, x², x², ..., x²]
    x2_powers = np.cumprod(x2_rep)        # [1, x², x⁴, ..., x^{2n}]

    # (2k)! sans boucle : cumprod sur [1,1,2,3,4,5,...,2n-1,2n]
    indices_2k = np.arange(2 * n + 1)     # [0, 1, 2, ..., 2n]
    indices_2k[0] = 1                      # évite la division par 0 dans cumprod
    fact_pairs = np.cumprod(indices_2k)[::2]  # slicing pair : (0)!=1, (2)!=2, (4)!=24...

    termes = signes * x2_powers / fact_pairs
    return float(np.sum(termes))


# --- TEST ---
print("=" * 60)
print("EXERCICE 4 — Série du cosinus : sommecos(x, n)")
print("=" * 60)
print(f"  {'x':>6}  {'n':>4}  {'S_n(x)':>18}  {'cos(x)':>18}  {'erreur':>12}")
print("  " + "-" * 65)
test_cases = [(0.5, 5), (1.0, 8), (math.pi, 15), (3.14, 10), (10.0, 50)]
for x_val, n_val in test_cases:
    sn  = sommecos(x_val, n_val)
    ref = math.cos(x_val)
    err = np.abs(sn - ref)
    print(f"  {x_val:>6.2f}  {n_val:>4}  {sn:>18.10f}  {ref:>18.10f}  {err:>12.2e}")
print()


# ===========================================================================
# EXERCICE 5 ★★ — Série alternée : S_n = Σ_{k=1}^{n} (-1)^{k+1}/k → ln(2)
# ===========================================================================

def ln2(eps):
    """
    Calcule une valeur approchée de ln(2) à ε près.

    Avec NumPy : on construit le vecteur des termes d'un coup
    et on les somme avec np.sum.
    """
    n = math.ceil(1 / eps - 1)

    k = np.arange(1, n + 1, dtype=np.float64)    # [1, 2, 3, ..., n]
    termes = (-1.0) ** (k + 1) / k               # terme général vectorisé
    return float(np.sum(termes))


def rang_effectif_ln2(eps):
    """
    Calcule le PLUS PETIT rang n tel que |S_n - ln(2)| ≤ ε.

    Avec NumPy : np.abs pour l'écart, np.log(2) pour la référence exacte.
    La boucle while reste nécessaire (condition d'arrêt séquentielle).
    """
    ref   = np.log(2)                 # ln(2) via NumPy
    somme = np.float64(0.0)
    n     = 0

    while True:
        n += 1
        somme += (-1.0) ** (n + 1) / n
        if np.abs(somme - ref) <= eps:
            return n


# --- TEST ---
print("=" * 60)
print("EXERCICE 5 — Série alternée vers ln(2)")
print("=" * 60)
eps5    = 1e-6
ref_ln2 = np.log(2)

print(f"  Référence : ln(2) = {ref_ln2:.10f}")
print()

approx = ln2(eps5)
n_theo = math.ceil(1 / eps5 - 1)
print(f"  Q1 — ε = {eps5}")
print(f"       Rang théorique suffisant : n = {n_theo}")
print(f"       Approximation S_n        = {approx:.10f}")
print(f"       Erreur réelle            = {np.abs(approx - ref_ln2):.2e}")
print()

n_reel = rang_effectif_ln2(eps5)
print(f"  Q2 — Plus petit rang effectif : n = {n_reel}")
print(f"       Commentaire : le rang effectif ({n_reel}) est INFÉRIEUR au rang")
print(f"       théorique ({n_theo}) car la borne 1/(n+1) est une majoration")
print(f"       PESSIMISTE. Le critère est souvent satisfait bien avant.")
print()


# ===========================================================================
# EXERCICE 6 ★★ — Paradoxe des anniversaires
# ===========================================================================

def proba_anniversaire(n):
    """
    Calcule p_n = probabilité qu'au moins 2 élèves sur n partagent
    un anniversaire.

    Avec NumPy : np.prod sur le vecteur des facteurs au lieu d'une boucle.
    """
    assert 1 <= n <= 365, "n doit être dans [1 ; 365]"

    k = np.arange(n, dtype=np.float64)          # [0, 1, 2, ..., n-1]
    facteurs = 1.0 - k / 365.0                  # [(1-0/365), (1-1/365), ...]
    return float(1.0 - np.prod(facteurs))        # 1 - P(tous différents)


def seuil_anniversaire(x):
    """
    Calcule le plus petit n tel que p_n ≥ x, via la récurrence.

    Avec NumPy : np.float64 + np.abs pour la gestion de précision.
    La récurrence reste séquentielle (état cumulatif).
    """
    assert 0 < x < 1, "x doit être dans ]0 ; 1["

    p = np.float64(0.0)
    n = 1

    while p < x and n <= 365:
        p = 1.0 - (1.0 - p) * (1.0 - n / 365.0)
        n += 1

    return n - 1


# --- TESTS ---
print("=" * 60)
print("EXERCICE 6 — Paradoxe des anniversaires")
print("=" * 60)

# Question 1 — vecteur de n, calcul groupé avec NumPy
n_vals = np.array([10, 20, 23, 30, 40, 50, 57, 70])
probas = np.array([proba_anniversaire(n) for n in n_vals])

print("  Q1 — Valeurs de p_n :")
for n_val, p in zip(n_vals, probas):
    print(f"    p_{n_val:3d} = {p:.4f}  ({p*100:.1f}%)")
print()

x_seuil = 0.99
n_seuil = seuil_anniversaire(x_seuil)
p_check = proba_anniversaire(n_seuil)
print(f"  Q2b — Plus petit n tel que p_n ≥ {x_seuil} :")
print(f"    n = {n_seuil}")
print(f"    Vérification : p_{n_seuil} = {p_check:.6f}")
print()
print("  COMMENTAIRE SUR LE PARADOXE :")
n_50 = seuil_anniversaire(0.5)
p_50 = proba_anniversaire(n_50)
print(f"  Il suffit de 23 élèves pour avoir plus de 50% de chances")
print(f"  que deux partagent un anniversaire (p_{n_50} ≈ {p_50:.4f}).")
print("  Ce résultat est contre-intuitif car notre cerveau pense")
print("  à UNE personne précise, alors qu'on compare toutes les paires.")
print(f"  Pour 99% de chances, il faut seulement {n_seuil} élèves.")
print()
print("=" * 60)
print("Tous les exercices terminés.")
print("=" * 60)