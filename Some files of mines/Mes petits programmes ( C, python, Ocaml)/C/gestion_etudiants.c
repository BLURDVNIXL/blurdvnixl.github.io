#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_NAME 128

typedef struct Etudiant {
    char nom[MAX_NAME];
    int age;
    char sexe; // 'M' ou 'F'
    int nb_notes;
    float *notes; // dynamique, nb_notes éléments
    float moyenne;
} Etudiant;

// Utility: read a line and trim newline
static void read_line(char *buf, size_t size) {
    if (!fgets(buf, (int)size, stdin)) return;
    size_t len = strlen(buf);
    if (len && buf[len-1] == '\n') buf[len-1] = '\0';
}

void saisir_etudiants(Etudiant *tab, int n) {
    char tmp[64];
    for (int i = 0; i < n; ++i) {
        printf("\n--- Etudiant %d / %d ---\n", i+1, n);
        printf("Nom : ");
        read_line(tab[i].nom, sizeof(tab[i].nom));
        if (strlen(tab[i].nom) == 0) { strcpy(tab[i].nom, "(nom_non_renseigne)"); }

        while (1) {
            printf("Age : ");
            read_line(tmp, sizeof(tmp));
            if (sscanf(tmp, "%d", &tab[i].age) == 1 && tab[i].age >= 0) break;
            printf("Entrée invalide. Entrez un entier >= 0.\n");
        }

        while (1) {
            printf("Sexe (M/F) : ");
            read_line(tmp, sizeof(tmp));
            if (strlen(tmp) >= 1) {
                char c = toupper((unsigned char)tmp[0]);
                if (c == 'M' || c == 'F') { tab[i].sexe = c; break; }
            }
            printf("Entrée invalide. Tapez 'M' ou 'F'.\n");
        }

        while (1) {
            printf("Nombre de notes en informatique (M, entier >= 0) : ");
            read_line(tmp, sizeof(tmp));
            if (sscanf(tmp, "%d", &tab[i].nb_notes) == 1 && tab[i].nb_notes >= 0) break;
            printf("Entrée invalide. Entrez un entier >= 0.\n");
        }

        if (tab[i].nb_notes > 0) {
            tab[i].notes = malloc(sizeof(float) * tab[i].nb_notes);
            if (!tab[i].notes) { perror("malloc"); exit(EXIT_FAILURE); }
            for (int j = 0; j < tab[i].nb_notes; ++j) {
                while (1) {
                    printf("  Note %d : ", j+1);
                    read_line(tmp, sizeof(tmp));
                    float v;
                    if (sscanf(tmp, "%f", &v) == 1 && v >= 0.0f && v <= 20.0f) { tab[i].notes[j] = v; break; }
                    printf("Entrée invalide. Entrez une note entre 0 et 20.\n");
                }
            }
        } else {
            tab[i].notes = NULL;
        }
    }
}

void calculer_moyennes(Etudiant *tab, int n) {
    for (int i = 0; i < n; ++i) {
        if (tab[i].nb_notes == 0) { tab[i].moyenne = 0.0f; continue; }
        float s = 0.0f;
        for (int j = 0; j < tab[i].nb_notes; ++j) s += tab[i].notes[j];
        tab[i].moyenne = s / tab[i].nb_notes;
    }
}

int indice_meilleure_moyenne(const Etudiant *tab, int n) {
    if (n <= 0) return -1;
    int idx = 0;
    for (int i = 1; i < n; ++i) {
        if (tab[i].moyenne > tab[idx].moyenne) idx = i;
    }
    return idx;
}

float moyenne_generale(const Etudiant *tab, int n) {
    if (n <= 0) return 0.0f;
    float s = 0.0f;
    for (int i = 0; i < n; ++i) s += tab[i].moyenne;
    return s / n;
}

void afficher_au_moins_moyenne(const Etudiant *tab, int n, float moyClasse) {
    printf("\nEtudiants avec moyenne >= moyenne generale (%.2f) :\n", moyClasse);
    int count = 0;
    for (int i = 0; i < n; ++i) {
        if (tab[i].moyenne >= moyClasse) {
            printf(" - %s (moy=%.2f)\n", tab[i].nom, tab[i].moyenne);
            ++count;
        }
    }
    if (count == 0) printf("  Aucun étudiant ne satisfait cette condition.\n");
}

void compter_par_genre_au_moins(const Etudiant *tab, int n, float moyClasse, int *mMasculin, int *mFeminin) {
    *mMasculin = *mFeminin = 0;
    for (int i = 0; i < n; ++i) {
        if (tab[i].moyenne >= moyClasse) {
            if (tab[i].sexe == 'M') ++(*mMasculin);
            else ++(*mFeminin);
        }
    }
}

int indice_plus_age(const Etudiant *tab, int n) {
    if (n <= 0) return -1;
    int idx = 0;
    for (int i = 1; i < n; ++i) {
        if (tab[i].age > tab[idx].age) idx = i;
    }
    return idx;
}

float pourcentage_admis(const Etudiant *tab, int n) {
    if (n <= 0) return 0.0f;
    int cnt = 0;
    for (int i = 0; i < n; ++i) if (tab[i].moyenne >= 10.0f) ++cnt;
    return (100.0f * cnt) / n;
}

void liberer_etudiants(Etudiant *tab, int n) {
    for (int i = 0; i < n; ++i) free(tab[i].notes);
}

int main(void) {
    printf("=== Gestion des Etudiants MP2I ===\n");
    int N;
    char tmp[64];
    while (1) {
        printf("Nombre d'etudiants N (entier > 0) : ");
        read_line(tmp, sizeof(tmp));
        if (sscanf(tmp, "%d", &N) == 1 && N > 0) break;
        printf("Entrée invalide.\n");
    }

    Etudiant *classe = malloc(sizeof(Etudiant) * N);
    if (!classe) { perror("malloc"); return 1; }

    // initialize pointers to NULL
    for (int i = 0; i < N; ++i) { classe[i].notes = NULL; classe[i].moyenne = 0.0f; classe[i].nb_notes = 0; classe[i].sexe = 'M'; classe[i].age = 0; classe[i].nom[0] = '\0'; }

    saisir_etudiants(classe, N);
    calculer_moyennes(classe, N);

    // Affichage des moyennes individuelles
    printf("\nMoyennes des etudiants :\n");
    for (int i = 0; i < N; ++i) {
        printf("%s : %.2f\n", classe[i].nom, classe[i].moyenne);
    }

    // 4. Etudiant ayant la meilleure moyenne
    int idxBest = indice_meilleure_moyenne(classe, N);
    if (idxBest >= 0) {
        printf("\nEtudiant ayant la meilleure moyenne : %s (%.2f)\n", classe[idxBest].nom, classe[idxBest].moyenne);
    }

    // 5. Moyenne generale de la classe
    float moyClasse = moyenne_generale(classe, N);
    printf("\nMoyenne generale de la classe : %.2f\n", moyClasse);

    // 6. Afficher noms >= moyenne generale
    afficher_au_moins_moyenne(classe, N, moyClasse);

    // 7. Nombre d'etudiants M/F >= moyenne generale
    int nM=0, nF=0;
    compter_par_genre_au_moins(classe, N, moyClasse, &nM, &nF);
    printf("\nNombre d'etudiants de sexe Masculin avec moyenne >= moyenne generale : %d\n", nM);
    printf("Nombre d'etudiants de sexe Feminin  avec moyenne >= moyenne generale : %d\n", nF);

    // 8. Etudiant le plus age
    int idxOld = indice_plus_age(classe, N);
    if (idxOld >= 0) {
        printf("\nEtudiant le plus age : %s, age=%d, moyenne=%.2f\n", classe[idxOld].nom, classe[idxOld].age, classe[idxOld].moyenne);
    }

    // 9. Pourcentage admits (moy >= 10)
    float pctAdmis = pourcentage_admis(classe, N);
    printf("\nPourcentage d'etudiants admis (moy >= 10) : %.2f%%\n", pctAdmis);

    liberer_etudiants(classe, N);
    free(classe);

    return 0;
}
