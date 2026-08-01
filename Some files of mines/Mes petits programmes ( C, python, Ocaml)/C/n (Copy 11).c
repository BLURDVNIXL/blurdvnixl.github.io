#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define MAX_ETUDIANTS 50
#define MAX_NOTES 20

/* ===== Structure ===== */
typedef struct {
    char nom[50];
    int age;
    char sexe;
    int nbNotes;
    float notes[MAX_NOTES];
    float moyenne;
} Etudiant;

/* ===== Mise en majuscules ===== */
void to_upper(char *s)
{
    for (int i = 0; s[i]; i++)
        s[i] = (char) toupper((unsigned char)s[i]);
}

/* ===== Saisie d’un étudiant ===== */
Etudiant saisirEtudiant()
{
    Etudiant e;

    printf("Nom : ");
    scanf("%49s", e.nom);
    to_upper(e.nom);

    printf("Age : ");
    scanf("%d", &e.age);

    printf("Sexe (M/F) : ");
    scanf(" %c", &e.sexe);
    e.sexe = (char) toupper(e.sexe);

    do {
        printf("Nombre de notes (max %d) : ", MAX_NOTES);
        scanf("%d", &e.nbNotes);
    } while (e.nbNotes < 1 || e.nbNotes > MAX_NOTES);

    for (int i = 0; i < e.nbNotes; i++) {
        printf("Note %d : ", i + 1);
        scanf("%f", &e.notes[i]);
    }

    return e;
}

/* ===== Moyenne étudiant ===== */
float moyenneEtudiant(Etudiant e)
{
    float somme = 0.0f;
    for (int i = 0; i < e.nbNotes; i++)
        somme += e.notes[i];
    return somme / e.nbNotes;
}

/* ===== Moyenne générale ===== */
float moyenneClasse(Etudiant classe[], int n)
{
    float somme = 0.0f;
    for (int i = 0; i < n; i++)
        somme += classe[i].moyenne;
    return somme / n;
}

/* ===== Indices ===== */
int indiceMeilleureMoyenne(Etudiant classe[], int n)
{
    int idx = 0;
    for (int i = 1; i < n; i++)
        if (classe[i].moyenne > classe[idx].moyenne)
            idx = i;
    return idx;
}

int indicePlusAge(Etudiant classe[], int n)
{
    int idx = 0;
    for (int i = 1; i < n; i++)
        if (classe[i].age > classe[idx].age)
            idx = i;
    return idx;
}

/* ===== Affichages ===== */
void afficherMoyennes(Etudiant classe[], int n)
{
    for (int i = 0; i < n; i++)
        printf("%s : %.2f\n", classe[i].nom, classe[i].moyenne);
}

void afficherSupMoyClasse(Etudiant classe[], int n, float moyClasse)
{
    for (int i = 0; i < n; i++)
        if (classe[i].moyenne >= moyClasse)
            printf("%s\n", classe[i].nom);
}

void compterSexeSupMoyClasse(Etudiant classe[], int n, float moyClasse)
{
    int m = 0, f = 0;

    for (int i = 0; i < n; i++)
        if (classe[i].moyenne >= moyClasse) {
            if (classe[i].sexe == 'M') m++;
            else if (classe[i].sexe == 'F') f++;
        }

    printf("Masculins >= moyenne : %d\n", m);
    printf("Feminins >= moyenne : %d\n", f);
}

/* ===== Pourcentage admis ===== */
float pourcentageAdmis(Etudiant classe[], int n)
{
    int admis = 0;
    for (int i = 0; i < n; i++)
        if (classe[i].moyenne >= 10.0f)
            admis++;
    return (100.0f * admis) / n;
}

/* ===== MAIN ===== */
int main(void)
{
    int N;
    Etudiant classe[MAX_ETUDIANTS];

    do {
        printf("Nombre d'etudiants (max %d) : ", MAX_ETUDIANTS);
        scanf("%d", &N);
    } while (N < 1 || N > MAX_ETUDIANTS);

    for (int i = 0; i < N; i++) {
        printf("\n--- Etudiant %d ---\n", i + 1);
        classe[i] = saisirEtudiant();
        classe[i].moyenne = moyenneEtudiant(classe[i]);
    }

    printf("\nMoyennes des etudiants :\n");
    afficherMoyennes(classe, N);

    int idxMax = indiceMeilleureMoyenne(classe, N);
    printf("\nMeilleure moyenne : %s (%.2f)\n",
           classe[idxMax].nom, classe[idxMax].moyenne);

    float moyClasse = moyenneClasse(classe, N);
    printf("\nMoyenne generale : %.2f\n", moyClasse);

    printf("\nEtudiants >= moyenne generale :\n");
    afficherSupMoyClasse(classe, N, moyClasse);

    compterSexeSupMoyClasse(classe, N, moyClasse);

    int idxAge = indicePlusAge(classe, N);
    printf("\nEtudiant le plus age : %s | Age : %d | Moyenne : %.2f\n",
           classe[idxAge].nom, classe[idxAge].age, classe[idxAge].moyenne);

    printf("\nPourcentage d'admis : %.2f %%\n",
           pourcentageAdmis(classe, N));

    return 0;
}
