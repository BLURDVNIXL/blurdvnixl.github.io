#include <stdio.h>
#include <stdbool.h>
#include <math.h>


void saisir(float tab[], int taille) {
    printf("\n--- Saisie des nombres ---\n");
    for (int i = 0; i < taille; i++) {
        printf("Veuillez entrer le nombre numéro %d : ", i + 1);
        scanf("%f", &tab[i]);
    }
}

void afficher(float tab[], int taille) {
    printf("\n--- Les nombres saisis sont ---\n");
    for (int i = 0; i < taille; i++) {
        printf("Nombre %d : %.2f\n", i + 1, tab[i]);
    }
}

void maxmin(float tab[], int taille) {
    if (taille == 0) return;

    float max = tab[0];
    float min = tab[0];
    int pos_max = 0;
    int pos_min = 0;

    printf("\n--- Analyse du maximum et du minimum ---\n");
    for (int i = 1; i < taille; i++) {
        if (tab[i] > max) {
            max = tab[i];
            pos_max = i;
        }
        if (tab[i] < min) {
            min = tab[i];
            pos_min = i;
        }
    }
    printf("Le maximum de ce tableau est %.2f (à la position %d).\n", max, pos_max + 1);
    printf("Le minimum de ce tableau est %.2f (à la position %d).\n", min, pos_min + 1);
}

float Moy(float tab[], int taille) {
    if (taille == 0) return 0;
    float somme = 0;
    for (int i = 0; i < taille; i++) {
        somme += tab[i];
    }
    return somme / taille;
}

void moy(float tab[], int taille) {
    float moyenne = Moy(tab, taille);
    printf("\n--- Calculons la moyenne de ce tableau ---\n");
    printf("La moyenne de ce tableau est %.2f .\n", moyenne);
}

void ecartypvar(float tab[], int taille) {
    if (taille == 0) {
        printf("\n--- Calculons l'ecart type et la variance ---\n");
        printf("Le tableau est vide, impossible de calculer l'écart-type et la variance.\n");
        return;
    }

    float moyenne = Moy(tab, taille);
    float somme_carre_ecarts = 0;

    printf("\n--- Calculons l'ecart type et la variance ---\n");
    for (int i = 0; i < taille; i++) {
        float ecart = tab[i] - moyenne;
        somme_carre_ecarts += ecart * ecart;
    }

    float variance = somme_carre_ecarts / taille;
    float ecart_type = sqrt(variance);

    printf("L'écart-type de ce tableau est %.2f et la variance est %.2f .\n", ecart_type, variance);
}

int premier(int b) {
    if (b <= 1) return 0;
    if (b == 2) return 1;
    if (b % 2 == 0) return 0;
    for (int i = 3; i * i <= b; i += 2) {
        if (b % i == 0) return 0;
    }
    return 1;
}

void afficherpremier(float tab[], int taille) {
    printf("\n--- Les nombres d'indice premier saisis sont ---\n");
    for (int i = 0; i < taille; i++) {
        if (premier(i) == 1) {
            printf("Nombre %d (indice %d) : %.2f\n", i + 1, i, tab[i]);
        }
    }
}

int parfait(int n) {
    if (n <= 1) {
        return 0;
    }
    
    int somme_diviseurs = 1; 

    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            somme_diviseurs += i;
            if (i * i != n) {
                somme_diviseurs += (n / i);
            }
        }
    }

    return (somme_diviseurs == n) ? 1 : 0;
}

void afficherparfait(float tab[], int taille) {
    printf("\n--- Les nombres dont la partie entiere est un Nombre Parfait ---\n");
    for (int i = 0; i < taille; i++) {
        // Convertir le float en int pour vérifier la propriété du nombre parfait
        int valeur_entiere = (int)tab[i]; 

        if (valeur_entiere > 0 && parfait(valeur_entiere) == 1) {
            printf("Nombre %d (%.2f -> Partie Entiere %d) est Parfait.\n", 
                   i + 1, tab[i], valeur_entiere);
        }
    }
}

void trier(float tab[], int taille){
    for (int i = 0; i < taille; i++){
        
    }
}


int main(void) {
    int n;

    printf("Veuillez entrer le nombre de nombres à saisir : ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Erreur : La taille du tableau doit être un nombre entier positif.\n");
        return 1;
    }

    printf("Vous allez saisir %d nombres.\n", n);
    float tab[n];

    saisir(tab, n);
    afficher(tab, n);
    maxmin(tab, n);
    moy(tab, n);
    ecartypvar(tab, n);
    afficherpremier(tab, n);
    afficherparfait(tab, n); 
    return 0;
}