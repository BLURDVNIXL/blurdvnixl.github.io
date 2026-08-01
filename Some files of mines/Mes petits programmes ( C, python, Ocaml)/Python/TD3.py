"""
=============================================================================
  CORRECTION TP — Matrices en Python (MP2I — INP-HB)
  Auteur : Daniel
=============================================================================

REPRÉSENTATION CHOISIE
-----------------------
Une matrice est représentée comme une LISTE DE LISTES :
    A = [[a00, a01, ...],
         [a10, a11, ...],
         ...]

  • A[i]    → ligne i  (liste)
  • A[i][j] → coefficient (i, j)
  • len(A)     → nombre de lignes  (noté nb_lignes ou n)
  • len(A[0])  → nombre de colonnes (noté nb_cols  ou p)

NB : Conformément aux consignes, AUCUNE fonction prédéfinie sur les
matrices (numpy, etc.) n'est utilisée. Seules les listes Python de base.
"""


# ===========================================================================
# FONCTIONS UTILITAIRES (non demandées, mais utilisées partout)
# ===========================================================================

def nb_lignes(A):
    """Renvoie le nombre de lignes de A."""
    return len(A)

def nb_cols(A):
    """Renvoie le nombre de colonnes de A (on suppose A non vide)."""
    return len(A[0])

def afficher_matrice(A, nom="M"):
    """Affiche joliment une matrice avec son nom."""
    print(f"  {nom} ({nb_lignes(A)}x{nb_cols(A)}) =")
    for ligne in A:
        print("   ", [round(x, 4) for x in ligne])
    print()


# ===========================================================================
# EXERCICE 1 — Opérations élémentaires sur les matrices
# ===========================================================================

# ---------------------------------------------------------------------------
# 1.1 ADDITION DE MATRICES
# ---------------------------------------------------------------------------
"""
MATHÉMATIQUES
-------------
(A + B)[i][j] = A[i][j] + B[i][j]

Condition : A et B doivent avoir les MÊMES dimensions.
On construit la matrice résultat ligne par ligne, colonne par colonne.
"""

def addition_matrices(A, B):
    """
    Renvoie la somme C = A + B.

    Paramètres
    ----------
    A, B : list[list[float]] — matrices de mêmes dimensions

    Retourne
    --------
    list[list[float]] — matrice C = A + B
    """
    n, p = nb_lignes(A), nb_cols(A)
    assert nb_lignes(B) == n and nb_cols(B) == p, \
        "Les matrices doivent avoir les mêmes dimensions pour l'addition."

    # Construction de la matrice résultat (n lignes, p colonnes)
    C = []
    for i in range(n):
        ligne = []
        for j in range(p):
            ligne.append(A[i][j] + B[i][j])
        C.append(ligne)

    return C


# ---------------------------------------------------------------------------
# 1.2 MULTIPLICATION DE MATRICES
# ---------------------------------------------------------------------------
"""
MATHÉMATIQUES
-------------
Si A est (n×p) et B est (p×q), alors C = A×B est (n×q) avec :
    C[i][j] = Σ_{k=0}^{p-1} A[i][k] * B[k][j]

C'est le "produit scalaire" de la ligne i de A par la colonne j de B.

Condition : nb_cols(A) == nb_lignes(B)
"""

def multiplication_matrices(A, B):
    """
    Renvoie le produit C = A × B (produit matriciel usuel).

    Paramètres
    ----------
    A : list[list[float]] — matrice (n × p)
    B : list[list[float]] — matrice (p × q)

    Retourne
    --------
    list[list[float]] — matrice C = A × B de taille (n × q)
    """
    n = nb_lignes(A)
    p = nb_cols(A)
    q = nb_cols(B)

    assert nb_lignes(B) == p, \
        f"Dimensions incompatibles : A est {n}x{p}, B est {nb_lignes(B)}x{q}."

    # Initialisation de C à zéro (n lignes, q colonnes)
    C = [[0] * q for _ in range(n)]

    # Triple boucle classique i, j, k
    for i in range(n):          # ligne de A (et de C)
        for j in range(q):      # colonne de B (et de C)
            for k in range(p):  # indice de sommation
                C[i][j] += A[i][k] * B[k][j]

    return C


# ---------------------------------------------------------------------------
# 1.3 TRANSPOSÉE D'UNE MATRICE
# ---------------------------------------------------------------------------
"""
MATHÉMATIQUES
-------------
Si A est (n×p), sa transposée A^T est (p×n) avec :
    A^T[j][i] = A[i][j]

On "retourne" la matrice : les lignes deviennent des colonnes.
"""

def transposee(A):
    """
    Renvoie la transposée A^T de la matrice A.

    Paramètres
    ----------
    A : list[list[float]] — matrice (n × p)

    Retourne
    --------
    list[list[float]] — matrice A^T de taille (p × n)
    """
    n, p = nb_lignes(A), nb_cols(A)

    # AT[j][i] = A[i][j]  →  p lignes, n colonnes
    AT = [[A[i][j] for i in range(n)] for j in range(p)]

    return AT


# --- TESTS EXERCICE 1 ---
print("=" * 60)
print("EXERCICE 1 — Opérations matricielles")
print("=" * 60)

A1 = [[1, 2, 3],
      [4, 5, 6]]

B1 = [[7, 8, 9],
      [1, 2, 3]]

print(">>> Addition")
afficher_matrice(A1, "A")
afficher_matrice(B1, "B")
afficher_matrice(addition_matrices(A1, B1), "A + B")

A2 = [[1, 2],
      [3, 4],
      [5, 6]]   # 3×2

B2 = [[7, 8, 9],
      [1, 2, 3]]  # 2×3

print(">>> Multiplication")
afficher_matrice(A2, "A (3×2)")
afficher_matrice(B2, "B (2×3)")
afficher_matrice(multiplication_matrices(A2, B2), "A × B (3×3)")

print(">>> Transposée")
A3 = [[1, 2, 3],
      [4, 5, 6]]
afficher_matrice(A3, "A (2×3)")
afficher_matrice(transposee(A3), "A^T (3×2)")


# ===========================================================================
# EXERCICE 2 — Matrice stochastique et nombres d'Armstrong
# ===========================================================================

# ---------------------------------------------------------------------------
# 2.1 MATRICE STOCHASTIQUE
# ---------------------------------------------------------------------------
"""
MATHÉMATIQUES
-------------
Une matrice M est stochastique si et seulement si :
  (a) Tous les coefficients sont STRICTEMENT positifs et STRICTEMENT < 1
        ∀i,j : 0 < M[i][j] < 1
  (b) La somme de chaque ligne vaut exactement 1
        ∀i : Σ_j M[i][j] = 1

Ce type de matrice modélise des chaînes de Markov (probabilités de
transition entre états).

Attention : comparaison de flottants → on tolère une petite erreur
numérique (epsilon = 1e-9) pour la somme.
"""

def est_stochastique(M):
    """
    Renvoie True si M est une matrice stochastique, False sinon.

    Paramètres
    ----------
    M : list[list[float]] — matrice carrée de réels

    Retourne
    --------
    bool
    """
    n, p = nb_lignes(M), nb_cols(M)
    EPS = 1e-9  # tolérance pour la comparaison des flottants

    for i in range(n):
        somme_ligne = 0
        for j in range(p):
            coeff = M[i][j]
            # Condition (a) : 0 < coeff < 1 (strictement)
            if not (0 < coeff < 1):
                return False
            somme_ligne += coeff
        # Condition (b) : somme = 1 (à EPS près)
        if abs(somme_ligne - 1) > EPS:
            return False

    return True


# ---------------------------------------------------------------------------
# 2.2 NOMBRES D'ARMSTRONG DANS UNE MATRICE
# ---------------------------------------------------------------------------
"""
MATHÉMATIQUES
-------------
Un nombre d'Armstrong (ou nombre narcissique) d'ordre d est un entier n
tel que la somme de ses chiffres, chacun élevé à la puissance d (nombre
de chiffres), est égale à n.

Exemples :
  153 = 1³ + 5³ + 3³         (3 chiffres)
  9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴  (4 chiffres)
  1, 2, ..., 9 sont tous Armstrong (1 chiffre)

Algorithme pour tester si n est Armstrong :
  1. Extraire les chiffres de n  (divisions successives par 10)
  2. d = nombre de chiffres
  3. Calculer Σ chiffre^d
  4. Comparer au nombre original

NB : On n'utilise PAS str() ni ** conformément à l'esprit du cours
(les puissances sont calculées avec une boucle multiplicative).
"""

def puissance(base, exp):
    """Calcule base^exp par multiplications successives (sans **)."""
    resultat = 1
    for _ in range(exp):
        resultat *= base
    return resultat

def est_armstrong(n):
    """
    Renvoie True si l'entier positif n est un nombre d'Armstrong.

    Méthode : extraction des chiffres par divisions successives.
    """
    if n < 0:
        return False

    # Étape 1 : extraire les chiffres et les stocker
    chiffres = []
    temp = n
    if temp == 0:
        chiffres = [0]
    while temp > 0:
        chiffres.append(temp % 10)   # dernier chiffre
        temp = temp // 10            # on supprime le dernier chiffre

    # Étape 2 : nombre de chiffres = ordre d
    d = len(chiffres)

    # Étape 3 : somme des chiffres^d
    somme = 0
    for c in chiffres:
        somme += puissance(c, d)

    return somme == n

def armstrong_dans_matrice(A):
    """
    Renvoie la liste de tous les nombres d'Armstrong présents dans A.

    Paramètres
    ----------
    A : list[list[int]] — matrice d'entiers

    Retourne
    --------
    list[int] — nombres d'Armstrong trouvés (sans doublon)
    """
    resultats = []
    for ligne in A:
        for val in ligne:
            # On ne traite que les entiers positifs
            if isinstance(val, int) and val >= 0 and est_armstrong(val):
                if val not in resultats:   # éviter les doublons
                    resultats.append(val)
    return resultats


# --- TESTS EXERCICE 2 ---
print("=" * 60)
print("EXERCICE 2 — Stochastique et Armstrong")
print("=" * 60)

M_stoch = [[0.5, 0.3, 0.2],
           [0.1, 0.7, 0.2],
           [0.4, 0.4, 0.2]]

M_non_stoch = [[0.5, 0.6, 0.2],   # somme ligne 0 = 1.3 ≠ 1
               [0.1, 0.7, 0.2],
               [0.4, 0.4, 0.2]]

print(f"  M_stoch est stochastique     : {est_stochastique(M_stoch)}")    # True
print(f"  M_non_stoch est stochastique : {est_stochastique(M_non_stoch)}")  # False
print()

M_arm = [[153, 370,   8],
         [  9, 100, 407],
         [  1,  13,   5]]

print("  Matrice :")
afficher_matrice(M_arm, "A")
print(f"  Nombres d'Armstrong dans A : {armstrong_dans_matrice(M_arm)}")
# Attendu : 153, 370, 8, 9, 407, 1, 5 (370=3³+7³+0³, 407=4³+0³+7³)
print()


# ===========================================================================
# EXERCICE 3 — Diagonale dominante et produit de Hadamard
# ===========================================================================

# ---------------------------------------------------------------------------
# 3.1 MATRICE À DIAGONALE DOMINANTE
# ---------------------------------------------------------------------------
"""
MATHÉMATIQUES
-------------
Une matrice carrée A est à diagonale dominante si :
    ∀i ∈ [[1,n]] : |A[i][i]| ≥ Σ_{j≠i} |A[i][j]|

Autrement dit : chaque terme diagonal est supérieur OU ÉGAL (en module)
à la SOMME des modules de tous les autres termes de sa ligne.

Importance : critère de convergence pour les méthodes itératives
(Jacobi, Gauss-Seidel). Si la dominance est STRICTE (>), le système
Ax = b a une unique solution.
"""

def est_diagonale_dominante(A):
    """
    Renvoie True si la matrice carrée A est à diagonale dominante.

    Paramètres
    ----------
    A : list[list[float]] — matrice CARRÉE

    Retourne
    --------
    bool
    """
    n = nb_lignes(A)
    assert nb_cols(A) == n, "La matrice doit être carrée."

    for i in range(n):
        # Module du terme diagonal
        diag = abs(A[i][i])

        # Somme des modules des AUTRES termes de la ligne i
        somme_hors_diag = 0
        for j in range(n):
            if j != i:                        # on exclut le terme diagonal
                somme_hors_diag += abs(A[i][j])

        # Condition : |a_{i,i}| >= Σ_{j≠i} |a_{i,j}|
        if diag < somme_hors_diag:
            return False

    return True


# ---------------------------------------------------------------------------
# 3.2 PRODUIT DE HADAMARD
# ---------------------------------------------------------------------------
"""
MATHÉMATIQUES
-------------
Le produit de Hadamard (ou produit terme à terme) de deux matrices
A et B de MÊMES dimensions est la matrice C définie par :
    C[i][j] = A[i][j] * B[i][j]

C'est différent du produit matriciel usuel !
Propriétés : commutatif, associatif, distributif.
Utilisé notamment en traitement d'image (masquage), réseaux de neurones.
"""

def hadamard(A, B):
    """
    Renvoie le produit de Hadamard C = A ⊙ B (produit terme à terme).

    Paramètres
    ----------
    A, B : list[list[float]] — matrices de MÊMES dimensions

    Retourne
    --------
    list[list[float]] — matrice C de mêmes dimensions
    """
    n, p = nb_lignes(A), nb_cols(A)
    assert nb_lignes(B) == n and nb_cols(B) == p, \
        "Les matrices doivent avoir les mêmes dimensions pour Hadamard."

    C = []
    for i in range(n):
        ligne = []
        for j in range(p):
            ligne.append(A[i][j] * B[i][j])   # produit terme à terme
        C.append(ligne)

    return C


# --- TESTS EXERCICE 3 ---
print("=" * 60)
print("EXERCICE 3 — Diagonale dominante et Hadamard")
print("=" * 60)

D1 = [[ 4, -1,  0],
      [-1,  4, -1],
      [ 0, -1,  4]]   # diagonale dominante : 4 >= |-1|+|0| = 1 ✓

D2 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]      # non dominante : ligne 1 : 1 < 2+3 = 5

print(f"  D1 est à diagonale dominante : {est_diagonale_dominante(D1)}")  # True
print(f"  D2 est à diagonale dominante : {est_diagonale_dominante(D2)}")  # False
print()

H_A = [[1, 2, 3],
       [4, 5, 6]]

H_B = [[7, 8, 9],
       [1, 2, 3]]

afficher_matrice(H_A, "A")
afficher_matrice(H_B, "B")
afficher_matrice(hadamard(H_A, H_B), "A ⊙ B (Hadamard)")
# Attendu : [[7,16,27],[4,10,18]]


# ===========================================================================
# PROBLÈME — Matrice Magique
# ===========================================================================
"""
MATHÉMATIQUES
-------------
Une matrice carrée n×n est MAGIQUE si toutes les sommes suivantes
sont ÉGALES (à la "constante magique") :
  • Somme de chaque ligne  (n valeurs)
  • Somme de chaque colonne (n valeurs)
  • Somme de la diagonale principale   (M[0][0] + M[1][1] + ... + M[n-1][n-1])
  • Somme de la diagonale anti-principale (M[0][n-1] + M[1][n-2] + ...)

Pour une matrice n×n contenant les entiers 1..n², la constante magique
vaut n(n²+1)/2. Par exemple pour n=3 : 3(9+1)/2 = 15.

STRATÉGIE
---------
1. On calcule la constante magique = somme de la première ligne.
2. On vérifie TOUTES les autres lignes.
3. On vérifie TOUTES les colonnes.
4. On vérifie la diagonale principale.
5. On vérifie la diagonale anti-principale.
→ Dès qu'une somme diffère, on renvoie False immédiatement.
"""

def est_magique(M):
    """
    Renvoie True si la matrice carrée M est une matrice magique.

    Paramètres
    ----------
    M : list[list[float]] — matrice CARRÉE

    Retourne
    --------
    bool
    """
    n = nb_lignes(M)
    assert nb_cols(M) == n, "La matrice doit être carrée."

    # Étape 1 : constante magique = somme de la première ligne
    constante = 0
    for j in range(n):
        constante += M[0][j]

    # Étape 2 : vérification de TOUTES les lignes
    for i in range(1, n):         # on part de 1, la ligne 0 est déjà la référence
        somme = 0
        for j in range(n):
            somme += M[i][j]
        if somme != constante:
            return False

    # Étape 3 : vérification de TOUTES les colonnes
    for j in range(n):
        somme = 0
        for i in range(n):
            somme += M[i][j]
        if somme != constante:
            return False

    # Étape 4 : diagonale principale (haut-gauche → bas-droite)
    # M[0][0], M[1][1], ..., M[n-1][n-1]
    somme_diag1 = 0
    for i in range(n):
        somme_diag1 += M[i][i]
    if somme_diag1 != constante:
        return False

    # Étape 5 : diagonale anti-principale (haut-droite → bas-gauche)
    # M[0][n-1], M[1][n-2], ..., M[n-1][0]
    somme_diag2 = 0
    for i in range(n):
        somme_diag2 += M[i][n - 1 - i]
    if somme_diag2 != constante:
        return False

    # Toutes les conditions sont satisfaites
    return True


# --- TESTS PROBLÈME ---
print("=" * 60)
print("PROBLÈME — Matrice Magique")
print("=" * 60)

# Exemple du sujet (3×3, constante = 15)
M_mag = [[8, 1, 6],
         [3, 5, 7],
         [4, 9, 2]]

# Exemple non magique
M_non_mag = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

# Matrice magique 4×4 connue (constante = 34)
M_mag4 = [[16,  2,  3, 13],
          [ 5, 11, 10,  8],
          [ 9,  7,  6, 12],
          [ 4, 14, 15,  1]]

afficher_matrice(M_mag, "M_magique_3x3")
print(f"  est_magique(M_mag)     = {est_magique(M_mag)}")      # True
print()
afficher_matrice(M_non_mag, "M_non_magique")
print(f"  est_magique(M_non_mag) = {est_magique(M_non_mag)}")  # False
print()
afficher_matrice(M_mag4, "M_magique_4x4 (Dürer)")
print(f"  est_magique(M_mag4)    = {est_magique(M_mag4)}")     # True
print()
print("=" * 60)
print("Tous les exercices terminés.")
print("=" * 60)