#include <stdio.h>


int nombreMatieres, nombreEtudiants, indexinformatique;

void correspondancenomEtudiantNUmero(int nombreEtudiants,char tabnomsEtundiants[][50]) { 
    for (int i = 0; i < nombreEtudiants; i++) {
        printf("Entrez le nom de l'etudiant %d: ", i + 1);
        scanf("%s", tabnomsEtundiants[i]);
    }
}

void correspondancenomMatiereNUmero(int nombreMatiere,char tabnomsMatiere[][50]) { 
    for (int i = 0; i < nombreMatiere; i++) {
        printf("Entrez le nom de la matiere %d: ", i + 1);
        scanf("%s", tabnomsMatiere[i]);
    }
}

void saisirNotes( int nombreEtudiants, int nombreMatieres ,int notes[nombreEtudiants][nombreMatieres], char tabnomsEtundiants[][50], char tabnomsMatiere[][50]) {
    for (int i = 0; i < nombreEtudiants; i++) {
        printf("Entrez les notes de l'etudiant %s:\n", tabnomsEtundiants[i]);
        for (int j = 0; j < nombreMatieres; j++) {
            printf("Note pour la matiere %s: ", tabnomsMatiere[j]);
            scanf("%d", &notes[i][j]);
        }
    }
}
void afficherMoyennesgenerale( int nombreEtudiants, int nombreMatieres, int notes[nombreEtudiants][nombreMatieres], char tabnomsEtundiants[][50]) {
    for (int i = 0; i < nombreEtudiants; i++) {
        int somme = 0;
        for (int j = 0; j < nombreMatieres; j++) {
            somme += notes[i][j];
        }
        float moyenne = (float)somme / nombreMatieres;
        printf("La moyenne generale de l'etudiant %s est: %.2f\n", tabnomsEtundiants[i] , moyenne);
    }
}

void affircherMoyenneMaxInformatique( int nombreEtudiants, int nombreMatieres, int notes[nombreEtudiants][nombreMatieres], int indexinformatique, char tabnomsEtundiants[][50]) {
    int maxNote = -1;
    char nomEtudiantMax[50];
    for (int i = 0; i < nombreEtudiants; i++) {
        if (notes[i][indexinformatique] > maxNote) {
            maxNote = notes[i][indexinformatique];
            snprintf(nomEtudiantMax, sizeof(nomEtudiantMax), "%s", tabnomsEtundiants[i]);//l'effet final est que le nom de l'étudiant (la chaîne stockée à l'index i dans le tableau des noms) est copié dans la variable locale nomEtudiantMax, de manière sécurisée.
        }
    }
    printf("L'etudiant avec la note maximale en informatique est %s avec une note de %d\n", nomEtudiantMax, maxNote);
}






int main() {
    printf("Entrez le nombre de Etudiants et de matieres\n");scanf("%d %d", &nombreEtudiants, &nombreMatieres);
    int notes[nombreEtudiants][nombreMatieres];
    char tabnomsEtundiants[nombreEtudiants][50]; char tabnomsMatiere[nombreMatieres][50];
    correspondancenomEtudiantNUmero(nombreEtudiants, tabnomsEtundiants);correspondancenomMatiereNUmero(nombreMatieres, tabnomsMatiere);
    saisirNotes(nombreEtudiants, nombreMatieres, notes, tabnomsEtundiants, tabnomsMatiere);
    afficherMoyennesgenerale(nombreEtudiants, nombreMatieres, notes, tabnomsEtundiants);
    affirchermoyenneparmatiere(nombreEtudiants, nombreMatieres, notes, tabnomsMatiere);
    printf("Ecrivez l'indice de la matiere informatique(0 a %d): ", nombreMatieres - 1);scanf("%d", &indexinformatique);
    affircherMoyenneMaxInformatique(nombreEtudiants, nombreMatieres, notes, indexinformatique, tabnomsEtundiants);
    
    return 0;
}