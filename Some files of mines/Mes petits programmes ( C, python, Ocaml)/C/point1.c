#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    // ============================================================
    // ALLOCATION DYNAMIQUE DE MÉMOIRE EN C
    // ============================================================
    
    // 1. ALLOCATION D'UN SEUL ENTIER
    // ============================================================
    // malloc() alloue de la mémoire sur le heap et retourne
    // un pointeur vers cette zone
    int *ptr_int = (int *)malloc(sizeof(int));
    
    // Vérification que l'allocation a réussi
    if (ptr_int == NULL) {
        printf("Erreur : allocation mémoire échouée\n");
        return 1;
    }
    
    // Utilisation du pointeur pour accéder à la mémoire allouée
    *ptr_int = 42;
    printf("Valeur stockée : %d\n", *ptr_int);
    
    // Libération de la mémoire avec free()
    // C'est obligatoire pour éviter une fuite mémoire
    free(ptr_int);
    ptr_int = NULL;  // Bonne pratique : mettre NULL après free()
    
    // 2. ALLOCATION D'UN TABLEAU
    // ============================================================
    int taille = 5;
    
    // Allocation d'un tableau de 5 entiers
    int *tableau = (int *)malloc(taille * sizeof(int));
    
    if (tableau == NULL) {
        printf("Erreur : allocation du tableau échouée\n");
        return 1;
    }
    
    // Remplissage du tableau
    for (int i = 0; i < taille; i++) {
        tableau[i] = i * 10;  // ou *(tableau + i) = i * 10;
    }
    
    // Affichage du tableau
    printf("Contenu du tableau : ");
    for (int i = 0; i < taille; i++) {
        printf("%d ", tableau[i]);
    }
    printf("\n");
    
    free(tableau);
    tableau = NULL;
    
    // 3. ALLOCATION D'UNE CHAÎNE DE CARACTÈRES
    // ============================================================
    char *chaine = (char *)malloc(50 * sizeof(char));
    
    if (chaine == NULL) {
        printf("Erreur : allocation de la chaîne échouée\n");
        return 1;
    }
    
    // Utilisation de la chaîne
    strcpy(chaine, "Bonjour allocation dynamique!");
    printf("Chaîne : %s\n", chaine);
    
    free(chaine);
    chaine = NULL;
    
    // 4. ALLOCATION D'UNE STRUCTURE
    // ============================================================
    // Définition d'une structure
    typedef struct {
        int age;
        float salaire;
        char nom[30];
    } Personne;
    
    // Allocation dynamique d'une structure
    Personne *personne = (Personne *)malloc(sizeof(Personne));
    
    if (personne == NULL) {
        printf("Erreur : allocation de la structure échouée\n");
        return 1;
    }
    
    // Initialisation de la structure via le pointeur
    personne->age = 25;
    personne->salaire = 2500.50f;
    strcpy(personne->nom, "Alice");
    
    printf("Personne : %s, %d ans, %.2f€\n", 
           personne->nom, personne->age, personne->salaire);
    
    free(personne);
    personne = NULL;
    
    // 5. RÉALLOCATION DE MÉMOIRE
    // ============================================================
    // realloc() permet de redimensionner une zone mémoire allouée
    int *nombres = (int *)malloc(3 * sizeof(int));
    
    if (nombres == NULL) {
        printf("Erreur : allocation échouée\n");
        return 1;
    }
    
    nombres[0] = 10;
    nombres[1] = 20;
    nombres[2] = 30;
    
    printf("Taille initiale : 3 éléments\n");
    
    // Augmentation de la taille à 5 éléments
    nombres = (int *)realloc(nombres, 5 * sizeof(int));
    
    if (nombres == NULL) {
        printf("Erreur : réallocation échouée\n");
        return 1;
    }
    
    nombres[3] = 40;
    nombres[4] = 50;
    
    printf("Nouvelle taille : 5 éléments\n");
    
    free(nombres);
    nombres = NULL;
    
    // ============================================================
    // RÉSUMÉ DES BONNES PRATIQUES
    // ============================================================
    // 1. Toujours vérifier si malloc/realloc ont réussi (!=NULL)
    // 2. Utiliser sizeof() pour la portabilité
    // 3. Libérer la mémoire avec free() quand elle n'est plus utile
    // 4. Mettre le pointeur à NULL après free()
    // 5. Ne pas accéder à la mémoire après free() (undefined behavior)
    
    printf("\nProgram terminé sans fuite mémoire\n");
    
    return 0;
}