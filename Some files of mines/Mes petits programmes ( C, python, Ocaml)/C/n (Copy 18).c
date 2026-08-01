#include <stdio.h>
#include <stdlib.h>

// Définition de la structure demandée
struct Cellule {
    int info;
    struct Cellule* suiv;
};

int main() {
    int N, i;

    // --- a) Saisie du nombre d'éléments et remplissage du tableau ---
    printf("Entrez le nombre d'elements (N) : ");
    scanf("%d", &N);

    int tableau[N]; // Utilisation d'un tableau de taille N
    for (i = 0; i < N; i++) {
        printf("Entrez l'entier n%d : ", i + 1);
        scanf("%d", &tableau[i]);
    }

    // --- b) Construction de la liste chainee (ordre du tableau) ---
    struct Cellule *maListe = NULL;
    struct Cellule *dernier = NULL;// null est utilise par le compilateur pour reconnaitre la fin d'une liste

    for (i = 0; i < N; i++) {
        // Allocation d'un nouveau nœud
        struct Cellule *nouveau = (struct Cellule*)malloc(sizeof(struct Cellule));
        nouveau->info = tableau[i];
        nouveau->suiv = NULL;

        if (maListe == NULL) {
            // Premier élément de la liste
            maListe = nouveau;// la tete pointe sur le premier element de la liste
            dernier = nouveau;// le courant pointe le dernier
        } else {
            // Ajout à la fin pour conserver l'ordre du tableau
            dernier->suiv = nouveau; //le courant du precedent pointe sur le nouveau, pour donner la valeur
            dernier = nouveau; // le courant devient le nouveau et pointe sur le dernier, pour deplacer courant
        }
    }

    // --- c) Parcours de la liste et affichage des éléments ---
    printf("\nContenu de la liste chainee : \n");
    struct Cellule *temp = maListe;
    while (temp != NULL) {
        printf("[%d] -> ", temp->info);
        temp = temp->suiv;
    }
    printf("NULL\n");

    // Libération de la mémoire (Bonne pratique)
    temp = maListe;
    while (temp != NULL) {
        struct Cellule *aSupprimer = temp;
        temp = temp->suiv;
        free(aSupprimer);
    }

    return 0;
}