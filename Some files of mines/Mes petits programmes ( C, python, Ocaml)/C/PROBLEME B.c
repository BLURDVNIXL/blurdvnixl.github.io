#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define MAX_ETUDIANTS 50
#define MAX_NOTES 20

/* ===== QUESTION 1 ===== */
typedef struct {
    char nom[50];
    int age;
    int matricule;
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

    printf("NOM : ");
    scanf("%49s", e.nom);
    to_upper(e.nom);

    printf("AGE : ");
    scanf("%d", &e.age);

    printf("MATRICULE : ");
    scanf(" %d", &e.matricule);
   

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

void ChercherEtudiant(Etudiant classe[] , int matricule, int N){
    for (int i = 0; i < N; i++)
    {
        if (matricule == classe[i].matricule)
        {
            printf("L'etudiant existe et son nom est %s ", classe[i].nom);break;
        }
        
    }
    
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





/* ===== MAIN ===== */
int main(void)
{
    int N;int ID;
    

    do {
        printf("Nombre d'etudiants (max %d) : ", MAX_ETUDIANTS);
        scanf("%d", &N);
    } while (N < 1 || N > MAX_ETUDIANTS);Etudiant classe[N];

    for (int i = 0; i < N; i++) {
        printf("\n--- Etudiant %d ---\n", i + 1);
        classe[i] = saisirEtudiant();
        classe[i].moyenne = moyenneEtudiant(classe[i]);
    }
    printf("Entre le matricule de l'etudiant que vous chercher (rien ne sera affiché dans le cas ou ce matricule ne corresponds a aucun etudiant)");scanf("%d",&ID);
    ChercherEtudiant(classe, ID, N);

    printf("\nMoyennes des etudiants :\n");
    afficherMoyennes(classe, N);

    int idxMax = indiceMeilleureMoyenne(classe, N);
    printf("\nMeilleure moyenne : %s (%.2f)\n",
           classe[idxMax].nom, classe[idxMax].moyenne);

    float moyClasse = moyenneClasse(classe, N);
    printf("\nMoyenne generale : %.2f\n", moyClasse);

    printf("\nEtudiants >= moyenne generale :\n");
    afficherSupMoyClasse(classe, N, moyClasse);

    int h=0;
    while (h!=6)
{
        printf(" \t MENU : \n 1- Ajouter un étudiant \n 2- Afficher la liste des etudiants \n 3- Rechercher un étudiant par matricule \n 4- Afficher l'etudiant ayant la meilleure moyenne \n 5-Trier les étudiants par moyenne \n 6-Quitter le programme \n CHOISISSEZ UNE OPTION \n");
    int h;scanf("%d",&h);
    switch (h)
    {
    case 1:
        printf("FONCTION INDISPONIBLE\n");
        break;
    case 2:
    printf("\nles etudiants et leurs moyenne:\n");
    afficherMoyennes(classe, N);
       break;
    case 3:
    printf("Entre le matricule de l'etudiant que vous chercher (rien ne sera affiché dans le cas ou ce matricule ne corresponds a aucun etudiant)");scanf("%d",&ID);
    ChercherEtudiant(classe, ID, N); break;
    case 4:
    int idxMax = indiceMeilleureMoyenne(classe, N);
    printf("\nMeilleure moyenne : %s (%.2f)\n",
           classe[idxMax].nom, classe[idxMax].moyenne); break;
    case 5:
    int idxxMax = indiceMeilleureMoyenne(classe, N);
    printf("\nMeilleure moyenne : %s (%.2f)\n",
           classe[idxxMax].nom, classe[idxMax].moyenne); break;
    
    default:
        break;
    }
}



    return 0;
}