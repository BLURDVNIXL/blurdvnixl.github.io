# %% [markdown]
# # ***EXERCICE 1***

# %%
import numpy as np

A=np.array([[1, -1, 2, 1, 2],
            [-1, 2, 3, -4, 1],
            [0, -1, 1, 0, 0]])

#1.Quel est le rang de la matrice A ?
rang_A = np.linalg.matrix_rank(A)
print("="*50);print("Le rang de la matrice A est :".upper(), rang_A);print("="*50)

# %%
import numpy as np

#On definit la matrice A et b
A = np.array([[1, -1, 2],
              [-1, 2, 3],
              [0, -1, 1]])
b = np.array([[3],
             [-7],
             [1]])
#2. Résoudre le système d'équations linéaires Ax = b
x = np.linalg.solve(A, b)
print("="*70);print("La solution du système d'équations linéaires Ax = b est :".upper(), x);print("="*70)

# %% [markdown]
# # ***EXERCICE 2***

# %%
import numpy as np

#(a) Définissons la matrice A comme un np.array
A = np.array([[4, 6, -2, 3],
              [2, -1, 0, 1],
              [-7, 0, 1, 12]],dtype=float)
#(b) Modifions la matrice A pour que ses deux premieres lignes soient multipliee par 2 et que sa derniere colonne soit divisee par 3
A[:2] *= 2  # Multiplie les deux premières lignes par 2
A[:, -1] = A[:, -1] / 3  # Divise la dernière colonne par 3
print("="*50);print("MATRICE A MODIFIEE :\n", A);print("="*50)

# %%
import numpy as np

#(c) Nouvelle matrice B avec
#ligne 1: suite arithmique de raison 1 de 4 a 6
#ligne 2: suite arithmique de raison 5 de 5 a 15
#ligne 3: suite de 3 éléments égaux à 1
B = np.array([[np.arange(4,7,1)],
              [np.arange(5,16,5)],
              [np.ones(3)]])
print("="*50);print("\t MATRICE B :\n", B);print("="*50)


# %%
import numpy as np

#Considerons le A de l' ennoncé
A = np.array([[4, 6, -2, 3],
              [2, -1, 0, 1],
              [-7, 0, 1, 12]],dtype=float)
#(d) Creer la matrice carre C d ordre 3 extraitee de A telle que pour 1 ≤ i, j ≤ 3, C[i][j] = A[i][j]
C = A[:3, :3]
print("="*50);print("\t MATRICE C :\n", C);print("="*50)

# %%
import numpy as np

#(e) Differents produits matriciels
#Realisons le produit matriciel D de B et A avec np.dot
D = np.dot(B, A)

print("="*50);print("\t PRODUIT MATRICIEL D = B * A :\n", D)
#Realisons le produit d'HADAMARD de B et C sachant qu il est defini par: Pour tout 1 ≤ i, j ≤ 3, E[i][j] = C[i][j] * B[i][j]
E = np.zeros((3,3))
E[0]=C[0] * B[0]
E[1]=C[1] * B[1]
E[2]=C[2] * B[2]

print("="*50);print("\t PRODUIT D'HADAMARD E = C * B :\n", E);print("="*50)


# %%
import numpy as np

#(f) Calculons la somme des elements de la matrice E et le vecteur colonne Y tel que Pour tout 1 ≤ i, j ≤ 3, yi= Somme des i de 1 a 4 de D[i][j]
somme_E = np.sum(E)
print("="*50);print("La somme des éléments de la matrice E est :".upper(), somme_E)
Y = np.zeros((3,1))
for i in range(3):
    Y[i] = np.sum(D[i,:])
print("="*50);print("\t LE VECTEUR COLONNE Y EST :\n", Y);print("="*50)


