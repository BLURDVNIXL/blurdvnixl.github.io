#include <stdio.h>

typedef struct Datedenaissance
{
    int jour;
    int mois;
    int annee;
} Date;

typedef struct Etudiant
    {
        char nom[50];
        char prenom[50];
        int matricule;
        char ecole[50];
        Date birth; 
    } Etudiant;
   
int main() {
    printf("Combien d'etudiants voulez-vous enregistrer? \n");
    int n;
    scanf("%d", &n);
    Etudiant classe[n];

    for(int i=0; i<n; i++){
        printf("Entrez le nom de l'etudiant %d: \n", i+1);scanf("%s", classe[i].nom);
        printf("Entrez le prenom de l'etudiant %d: \n", i+1);scanf("%s", classe[i].prenom);
        printf("Entrez le matricule de l'etudiant %d: \n", i+1);scanf("%d", &classe[i].matricule); //ne pas oublier le & pour les int vu que matricule est un int 
        //wow on mets aussi le & pour les int dans les struct
        printf("Entrez l'ecole de l'etudiant %d: \n", i+1);scanf("%s", classe[i].ecole);
        printf("Entrez la date de naissance (jj mm aaaa) de l'etudiant %d: \n", i+1);scanf("%d %d %d", &classe[i].birth.jour, &classe[i].birth.mois, &classe[i].birth.annee);
    }

    for(int i=0; i<n; i++){
        printf("~Le nom de l'etudiant %d est: %s\n", i+1, classe[i].nom);
        printf("~Le prenom de l'etudiant %d est: %s\n", i+1, classe[i].prenom);
        printf("~Le matricule de l'etudiant %d est: %d\n", i+1, classe[i].matricule);
        printf("~L'ecole de l'etudiant %d est: %s\n", i+1, classe[i].ecole);
        printf("~La date de naissance de l'etudiant %d est: %02d/%02d/%04d\n", i+1, classe[i].birth.jour, classe[i].birth.mois, classe[i].birth.annee); 
        printf("\n===========================\n");
    }
    return 0;
}