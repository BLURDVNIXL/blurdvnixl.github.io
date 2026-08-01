"""
=============================================================================
  CORRECTION TP — Matrices en Python (MP2I — INP-HB)
  Refactorisé avec NumPy
=============================================================================
"""

import numpy as np


# ===========================================================================
# FONCTIONS UTILITAIRES
# ===========================================================================

def afficher_matrice(A, nom="M"):
    """Affiche joliment une matrice NumPy avec son nom."""
    n, p = A.shape
    print(f"  {nom} ({n}x{p}) =")
    for ligne in A:
        print("   ", [round(float(x), 4) for x in ligne])
    print()


# ===========================================================================
# EXERCICE 1 — Opérations élémentaires sur les matrices
# ===========================================================================

# ---------------------------------------------------------------------------
# 1.1 ADDITION DE MATRICES
# ---------------------------------------------------------------------------
"""
(A + B)[i][j] = A[i][j] + B[i][j]
NumPy : l'opérateur + est surchargé → addition terme à terme native.
La vérification de dimensions est automatique (broadcast error sinon).
"""

def addition_matrices(A, B):
    assert A.shape == B.shape, "Dimensions incompatibles pour l'addition."
    return A + B      # surcharge NumPy : zéro boucle


# ---------------------------------------------------------------------------
# 1.2 MULTIPLICATION DE MATRICES
# ---------------------------------------------------------------------------
"""
C[i][j] = Σ_k A[i][k] * B[k][j]
NumPy : A @ B  (opérateur matmul, ou np.matmul)
"""

def multiplication_matrices(A, B):
    assert A.shape[1] == B.shape[0], \
        f"Dimensions incompatibles : {A.shape} × {B.shape}."
    return A @ B      # produit matriciel NumPy : zéro boucle


# ---------------------------------------------------------------------------
# 1.3 TRANSPOSÉE
# ---------------------------------------------------------------------------
"""
A^T[j][i] = A[i][j]
NumPy : attribut .T  (vue, pas copie)
"""

def transposee(A):
    return A.T        # attribut natif NumPy


# --- TESTS EXERCICE 1 ---
print("=" * 60)
print("EXERCICE 1 — Opérations matricielles")
print("=" * 60)

A1 = np.array([[1, 2, 3],
               [4, 5, 6]])
B1 = np.array([[7, 8, 9],
               [1, 2, 3]])

print(">>> Addition")
afficher_matrice(A1, "A"); afficher_matrice(B1, "B")
afficher_matrice(addition_matrices(A1, B1), "A + B")

A2 = np.array([[1, 2],
               [3, 4],
               [5, 6]])
B2 = np.array([[7, 8, 9],
               [1, 2, 3]])

print(">>> Multiplication")
afficher_matrice(A2, "A (3×2)"); afficher_matrice(B2, "B (2×3)")
afficher_matrice(multiplication_matrices(A2, B2), "A × B (3×3)")

print(">>> Transposée")
A3 = np.array([[1, 2, 3],
               [4, 5, 6]])
afficher_matrice(A3, "A (2×3)")
afficher_matrice(transposee(A3), "A^T (3×2)")


# ===========================================================================
# EXERCICE 2 — Matrice stochastique et nombres d'Armstrong
# ===========================================================================

# ---------------------------------------------------------------------------
# 2.1 MATRICE STOCHASTIQUE
# ---------------------------------------------------------------------------
"""
M stochastique ⟺  ∀i,j : 0 < M[i][j] < 1  ET  ∀i : Σ_j M[i][j] = 1

NumPy :
  • np.all(M > 0) et np.all(M < 1) → conditions (a) vectorisées
  • M.sum(axis=1)                   → vecteur des sommes de lignes
  • np.allclose(..., 1.0)           → comparaison flottante avec tolérance
"""

def est_stochastique(M):
    if not (np.all(M > 0) and np.all(M < 1)):
        return False
    return np.allclose(M.sum(axis=1), 1.0)


# ---------------------------------------------------------------------------
# 2.2 NOMBRES D'ARMSTRONG DANS UNE MATRICE
# ---------------------------------------------------------------------------
"""
n est Armstrong ⟺ Σ chiffre^d == n  (d = nombre de chiffres)

La logique de test reste scalaire (extraction de chiffres).
NumPy intervient pour :
  • np.unique(M.flatten()) → éléments uniques sans doublon en une ligne
  • np.int64              → type entier NumPy
"""

def est_armstrong(n):
    """Teste si l'entier positif n est un nombre d'Armstrong."""
    if n < 0:
        return False
    chiffres = []
    temp = int(n)
    if temp == 0:
        chiffres = [0]
    while temp > 0:
        chiffres.append(temp % 10)
        temp //= 10
    d = len(chiffres)
    return sum(c ** d for c in chiffres) == int(n)

def armstrong_dans_matrice(A):
    """
    Renvoie la liste des nombres d'Armstrong uniques dans A.
    np.unique(A.flatten()) donne les valeurs sans doublon d'un coup.
    """
    candidats = np.unique(A.flatten())       # éléments uniques, triés
    return [int(v) for v in candidats
            if isinstance(int(v), int) and int(v) >= 0 and est_armstrong(int(v))]


# --- TESTS EXERCICE 2 ---
print("=" * 60)
print("EXERCICE 2 — Stochastique et Armstrong")
print("=" * 60)

M_stoch = np.array([[0.5, 0.3, 0.2],
                    [0.1, 0.7, 0.2],
                    [0.4, 0.4, 0.2]])
M_non_stoch = np.array([[0.5, 0.6, 0.2],
                         [0.1, 0.7, 0.2],
                         [0.4, 0.4, 0.2]])

print(f"  M_stoch est stochastique     : {est_stochastique(M_stoch)}")
print(f"  M_non_stoch est stochastique : {est_stochastique(M_non_stoch)}")
print()

M_arm = np.array([[153, 370,   8],
                  [  9, 100, 407],
                  [  1,  13,   5]])
afficher_matrice(M_arm, "A")
print(f"  Nombres d'Armstrong dans A : {armstrong_dans_matrice(M_arm)}")
print()


# ===========================================================================
# EXERCICE 3 — Diagonale dominante et produit de Hadamard
# ===========================================================================

# ---------------------------------------------------------------------------
# 3.1 MATRICE À DIAGONALE DOMINANTE
# ---------------------------------------------------------------------------
"""
∀i : |A[i][i]| ≥ Σ_{j≠i} |A[i][j]|

NumPy :
  • np.abs(A)              → valeurs absolues terme à terme
  • np.diag(...)           → extrait la diagonale principale (vecteur)
  • .sum(axis=1)           → somme de chaque ligne
  • np.diag(np.abs(A))     → vecteur des |a_{ii}|
  • Σ_{j≠i} |a_{ij}| = somme_ligne_i - |a_{ii}|
"""

def est_diagonale_dominante(A):
    n = A.shape[0]
    assert A.shape == (n, n), "La matrice doit être carrée."

    abs_A         = np.abs(A)
    diag_vals     = np.diag(abs_A)              # vecteur |a_{ii}|
    sommes_lignes = abs_A.sum(axis=1)           # Σ_j |a_{ij}|
    hors_diag     = sommes_lignes - diag_vals   # Σ_{j≠i} |a_{ij}|

    return bool(np.all(diag_vals >= hors_diag))


# ---------------------------------------------------------------------------
# 3.2 PRODUIT DE HADAMARD
# ---------------------------------------------------------------------------
"""
C[i][j] = A[i][j] * B[i][j]
NumPy : l'opérateur * est le produit terme à terme natif sur les ndarray.
"""

def hadamard(A, B):
    assert A.shape == B.shape, "Dimensions incompatibles pour Hadamard."
    return A * B      # produit terme à terme NumPy : zéro boucle


# --- TESTS EXERCICE 3 ---
print("=" * 60)
print("EXERCICE 3 — Diagonale dominante et Hadamard")
print("=" * 60)

D1 = np.array([[ 4, -1,  0],
               [-1,  4, -1],
               [ 0, -1,  4]])
D2 = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])

print(f"  D1 est à diagonale dominante : {est_diagonale_dominante(D1)}")  # True
print(f"  D2 est à diagonale dominante : {est_diagonale_dominante(D2)}")  # False
print()

H_A = np.array([[1, 2, 3], [4, 5, 6]])
H_B = np.array([[7, 8, 9], [1, 2, 3]])
afficher_matrice(H_A, "A"); afficher_matrice(H_B, "B")
afficher_matrice(hadamard(H_A, H_B), "A ⊙ B (Hadamard)")


# ===========================================================================
# PROBLÈME — Matrice Magique
# ===========================================================================
"""
NumPy :
  • M.sum(axis=1)      → sommes des lignes
  • M.sum(axis=0)      → sommes des colonnes
  • np.trace(M)        → diagonale principale
  • np.trace(np.fliplr(M)) → diagonale anti-principale
  • np.all(... == c)   → vérification vectorisée
"""

def est_magique(M):
    n = M.shape[0]
    assert M.shape == (n, n), "La matrice doit être carrée."

    constante = M[0].sum()                          # somme ligne 0

    if not np.all(M.sum(axis=1) == constante):      # toutes les lignes
        return False
    if not np.all(M.sum(axis=0) == constante):      # toutes les colonnes
        return False
    if np.trace(M) != constante:                    # diagonale principale
        return False
    if np.trace(np.fliplr(M)) != constante:         # diagonale anti-principale
        return False

    return True


# --- TESTS PROBLÈME ---
print("=" * 60)
print("PROBLÈME — Matrice Magique")
print("=" * 60)

M_mag = np.array([[8, 1, 6],
                  [3, 5, 7],
                  [4, 9, 2]])
M_non_mag = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
M_mag4 = np.array([[16,  2,  3, 13],
                   [ 5, 11, 10,  8],
                   [ 9,  7,  6, 12],
                   [ 4, 14, 15,  1]])

afficher_matrice(M_mag,     "M_magique_3x3")
print(f"  est_magique(M_mag)     = {est_magique(M_mag)}")
print()
afficher_matrice(M_non_mag, "M_non_magique")
print(f"  est_magique(M_non_mag) = {est_magique(M_non_mag)}")
print()
afficher_matrice(M_mag4,    "M_magique_4x4 (Dürer)")
print(f"  est_magique(M_mag4)    = {est_magique(M_mag4)}")
print()
print("=" * 60)
print("Tous les exercices terminés.")
print("=" * 60)