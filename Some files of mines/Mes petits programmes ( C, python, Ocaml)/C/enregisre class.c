#include <stdio.h>

int main() {
    struct Etudiant
    {
        char nom[50];
        char prenom[50];
        int age;
    };//Etudiant (un alias /est le nom de la structure)
    struct Etudiant classe[50];//si on avait mis typedef dans la declaration de la structure on aurait pu ecrire juste Etudiant classe[50];

    for(int i=0; i<3; i++){
        printf("Entrez le nom de l'etudiant %d: \n", i+1);
        scanf("%s", classe[i].nom);
        printf("Entrez le prenom de l'etudiant %d: \n", i+1);
        scanf("%s", classe[i].prenom);
        printf("Entrez l'age de l'etudiant %d: \n", i+1);
        scanf("%d", &classe[i].age);
    }

    for(int i=0; i<3; i++){
        printf("~Le nom de l'etudiant %d est: %s\n", i+1, classe[i].nom);
        printf("~Le prenom de l'etudiant %d est: %s\n", i+1, classe[i].prenom);
        printf("~L'age de l'etudiant %d est: %d\n", i+1, classe[i].age);
        printf("\n============\n");
    }
    return 0;
}