#include <stdio.h>
#include <stdbool.h>

int est_premier(int b) {
    if (b <= 1) {
        return 0;
    }
    if (b == 2 || b == 3) {
        return 1;
    }
    if (b % 2 == 0) {
        return 0; // Pair > 2 n'est pas premier
    }

    for (int i = 3; i * i <= b; i += 2) {
        if (b % i == 0) {
            return 0;
        }
    }

    return 1;
}

int main(void) {
    int n;
    int ch; // ch représente le choix de l'utilisateur
    int est_n_premier; // Variable pour stocker le résultat du test

    printf("Entrer un entier SVP : ");
    // Vérification de l'entrée pour une meilleure robustesse
    if (scanf("%d", &n) != 1) {
        printf("Erreur de saisie. Veuillez entrer un entier valide.\n");
        return 1; // Code d'erreur
    }

    printf("\nSi vous voulez la liste des nombres premiers inferieurs a %d, taper 1.\n", n);
    printf("Pour savoir si %d est premier, taper 2.\n", n);
    printf("Votre choix : ");

    if (scanf("%d", &ch) != 1) {
        printf("Erreur de saisie. Veuillez entrer un choix valide (1 ou 2).\n");
        return 1; // Code d'erreur
    }
    
    printf("\n--- Resultat ---\n");

    if (ch == 1) {
        printf("Nombres premiers inferieurs a %d :\n", n);
        // On commence à 2 (le premier nombre premier) et on va jusqu'à n-1
        for (int j = 2; j < n; j++) {
            if (est_premier(j) == 1) {
                printf("%d\n", j);
            }
        }
    } else if (ch == 2) {
        // Test de primalité une seule fois
        est_n_premier = est_premier(n); 

        if (est_n_premier == 1) {
            printf("%d est un nombre premier.\n", n);
        } else {
            printf("%d n'est pas un nombre premier.\n", n);
        }
    } else {
        printf("Choix non reconnu. Veuillez taper 1 ou 2.\n");
    }

    return 0; // Retourne 0 pour indiquer une exécution réussie
}