#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// --- Constantes de la Structure ---
#define TAILLE_NOM 50
#define TAILLE_CLASSE 50

// --- Définition de la Structure ---
typedef struct {
    int id;
    char nom[TAILLE_NOM];
    char prenom[TAILLE_NOM];
    float note_moyenne;
} Etudiant;

// --- Variables Globales pour l'exemple (la "Classe") ---
Etudiant Classe[TAILLE_CLASSE];
int nombre_actuel = 0; // Compteur du nombre d'étudiants effectivement dans la classe

// --- Fonctions de Gestion ---

/**
 * Ajoute un nouvel étudiant à la classe.
 * @param classe Le tableau de structures Etudiant.
 * @param actuel Un pointeur vers le nombre actuel d'étudiants.
 */
void ajouterEtudiant(Etudiant classe[], int *actuel) {
    if (*actuel >= TAILLE_CLASSE) {
        printf("\nErreur : La classe est pleine (capacité maximale atteinte : %d).\n", TAILLE_CLASSE);
        return;
    }

    printf("\n--- Enregistrement d'un nouvel étudiant ---\n");
    
    // Assigner un ID simple
    classe[*actuel].id = *actuel + 1;
    printf("ID attribué : %d\n", classe[*actuel].id);

    printf("Nom : ");
    // Note : scanf("%s", ...) peut causer un dépassement de tampon.
    // Pour une application réelle, utiliser fgets et supprimer le caractère '\n'.
    scanf("%s", classe[*actuel].nom); 

    printf("Prénom : ");
    scanf("%s", classe[*actuel].prenom);

    printf("Note moyenne (0.0 à 20.0) : ");
    // Boucle pour une validation basique de la saisie
    while (scanf("%f", &classe[*actuel].note_moyenne) != 1 || classe[*actuel].note_moyenne < 0 || classe[*actuel].note_moyenne > 20) {
        printf("Saisie invalide. Veuillez entrer une note entre 0 et 20 : ");
        // Nettoyer le buffer d'entrée
        while (getchar() != '\n');
    }

    (*actuel)++;
    printf("\nÉtudiant %s %s (ID: %d) ajouté avec succès.\n", classe[*actuel - 1].prenom, classe[*actuel - 1].nom, classe[*actuel - 1].id);
}

/**
 * Affiche tous les étudiants actuellement enregistrés dans la classe.
 * @param classe Le tableau de structures Etudiant.
 * @param actuel Le nombre actuel d'étudiants.
 */
void afficherEtudiants(const Etudiant classe[], int actuel) {
    if (actuel == 0) {
        printf("\nLa classe est vide. Aucun étudiant à afficher.\n");
        return;
    }

    printf("\n--- Liste des %d étudiants enregistrés ---\n", actuel);
    printf("----------------------------------------------------\n");
    printf("| ID | Nom           | Prénom        | Note Moyenne |\n");
    printf("----------------------------------------------------\n");

    for (int i = 0; i < actuel; i++) {
        printf("| %-2d | %-13s | %-13s | %-12.2f |\n", 
               classe[i].id, 
               classe[i].nom, 
               classe[i].prenom, 
               classe[i].note_moyenne);
    }
    printf("----------------------------------------------------\n");
}

// --- Fonction Principale ---
int main() {
    int choix;

    do {
        printf("\n\n=== Menu de Gestion de Classe ===\n");
        printf("1. Ajouter un étudiant\n");
        printf("2. Afficher la liste des étudiants\n");
        // Option 3. Quitter est toujours importante pour les boucles 'do-while'
        printf("3. Quitter\n"); 
        printf("Veuillez entrer votre choix : ");
        
        // Saisie du choix de l'utilisateur
        if (scanf("%d", &choix) != 1) {
            printf("\nSaisie invalide. Veuillez entrer un nombre.\n");
            // Nettoyer le buffer d'entrée
            while (getchar() != '\n');
            continue; 
        }
        
        // Exécution du choix
        switch (choix) {
            case 1:
                ajouterEtudiant(Classe, &nombre_actuel);
                break;
            case 2:
                afficherEtudiants(Classe, nombre_actuel);
                break;
            case 3:
                printf("\nProgramme terminé. Au revoir.\n");
                break;
            default:
                printf("\nChoix non valide. Veuillez sélectionner 1, 2 ou 3.\n");
                break;
        }
    } while (choix != 3);

    return 0;
}