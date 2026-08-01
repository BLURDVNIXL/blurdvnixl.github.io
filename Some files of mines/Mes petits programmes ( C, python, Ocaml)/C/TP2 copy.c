#include <stdio.h>
#include <string.h>
#include <ctype.h>

int nombreMatieres, nombreEtudiants, indexinformatique;


void to_upper(char *s)
{
    for (int i = 0; i < strlen(s); i++)
    s[i] = (char) toupper((unsigned char) s[i]);//unsigned char pour éviter des comportements indéfinis avec des caractères négatifs 
}


void correspondancenomEtudiantNUmero(int nombreEtudiants,char tabnomsEtundiants[][50]) { 
    for (int i = 0; i < nombreEtudiants; i++) {
        printf("ENTREZ LE NOM DE L'ETUDIANT %d: \t", i + 1);
        scanf("%s", tabnomsEtundiants[i]);to_upper(tabnomsEtundiants[i]);
    }
}

void correspondancenomMatiereNUmero(int nombreMatiere,char tabnomsMatiere[][50],int indexinformatique) { 
    for (int i = 0; i < nombreMatiere; i++) {
        printf("ENTREZ LE NOM DE LA MATIERE %d: \t", i + 1);
        scanf("%s", tabnomsMatiere[i]);to_upper(tabnomsMatiere[i]);
        if ((strcmp(tabnomsMatiere[i], "INFORMATIQUE") == 0) || (strcmp(tabnomsMatiere[i], "INFO") == 0)) {//strcmp compare deux chaînes de caractères et retourne 0 si elles sont égales
            indexinformatique = i;
        }   
    }
}

void saisirNotes( int nombreEtudiants, int nombreMatieres ,int notes[nombreEtudiants][nombreMatieres], char tabnomsEtundiants[][50], char tabnomsMatiere[][50]) {
    for (int i = 0; i < nombreEtudiants; i++) {
        printf("ENTREZ LES NOTES DE L'ETUDIANT %s:\n", tabnomsEtundiants[i]);
        for (int j = 0; j < nombreMatieres; j++) {
            printf("\t NOTE POUR LA MATIERE %s: \t", tabnomsMatiere[j]);
            scanf("%d", &notes[i][j]);
        }
        printf("\n");
    }
}

void affichermoyenneparmatiere(int nombreEtudiants, int nombreMatieres, int notes[nombreEtudiants][nombreMatieres], char tabnomsEtudiants[][50], char tabnomsMatiere[][50]) {
    
        for (int j = 0; j < nombreMatieres; j++) 
        {
        int somme = 0;
        for (int i = 0; i < nombreEtudiants; i++) {
            somme += notes[i][j];
        }
        float moyenne = (float)somme / nombreEtudiants;
        printf("\t -LA MOYENNE DE LA MATIERE %s EST: %.2f\n", tabnomsMatiere[j], moyenne);
        }
    
    
    
    

}

void afficherMoyennesgenerale( int nombreEtudiants, int nombreMatieres, int notes[nombreEtudiants][nombreMatieres], char tabnomsEtundiants[][50]) {
    for (int i = 0; i < nombreEtudiants; i++) {
        int somme = 0;
        for (int j = 0; j < nombreMatieres; j++) {
            somme += notes[i][j];
        }
        float moyenne = (float)somme / nombreMatieres;
        printf(" -LA MOYENNE GENERALE DE L'ETUDIANT %s EST: %.2f\n", tabnomsEtundiants[i] , moyenne);
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
    printf("L'ETUDIANT AVEC LA PLUS FORTE NOTE EN INFORMATIQUE EST %s AVEC UNE NOTE DE %d\n \n", nomEtudiantMax, maxNote);
}

void admispourcentage( int nombreEtudiants, int nombreMatieres, int notes[nombreEtudiants][nombreMatieres], char tabnomsEtundiants[][50]) {
    int cptAdmis = 0;
    for (int i = 0; i < nombreEtudiants; i++) {
        int somme = 0;
        for (int j = 0; j < nombreMatieres; j++) {
            somme += notes[i][j];
        }
        float moyenne = (float)somme / nombreMatieres;
        if (moyenne >= 10.0) {
            cptAdmis++;
        }
    }
    float pourcentageAdmis = ((float)cptAdmis / nombreEtudiants) * 100;
    printf("LE POURCENTAGE D'ETUDIANT ADMIS EST: %.2f%%\n \n", pourcentageAdmis);
}

void matiereoulesetudiantscartonnent(int nombreEtudiants, int nombreMatieres, int notes[nombreEtudiants][nombreMatieres], char tabnomsMatiere[][50]) {
    for (int j = 0; j < nombreMatieres; j++) {
        int cptAdmisMatiere = 0;
        for (int i = 0; i < nombreEtudiants; i++) {
            if (notes[i][j] >= 10) {
                cptAdmisMatiere++;
            }
        }
        float pourcentageAdmisMatiere = ((float)cptAdmisMatiere / nombreEtudiants) * 100;
        if (pourcentageAdmisMatiere >= 80.0) {
            printf("LA MATIERE %s a un pourcentage d'admis de %.2f%%\n", tabnomsMatiere[j], pourcentageAdmisMatiere);
        }
    }
}


int main() 
{
    printf("ENTREZ LE NOMBRE D'ETUDIANTS:\t");scanf("%d", &nombreEtudiants);printf("ENTREZ LE NOMBRE DE MATIERE:\t");scanf("%d", &nombreMatieres);printf("\n");
    int notes[nombreEtudiants][nombreMatieres];indexinformatique = 0;
    char tabnomsEtundiants[nombreEtudiants][50]; char tabnomsMatiere[nombreMatieres][50];
    correspondancenomEtudiantNUmero(nombreEtudiants, tabnomsEtundiants);printf("\n");correspondancenomMatiereNUmero(nombreMatieres, tabnomsMatiere, indexinformatique);printf("\n");
    saisirNotes(nombreEtudiants, nombreMatieres, notes, tabnomsEtundiants, tabnomsMatiere);
    affichermoyenneparmatiere(nombreEtudiants, nombreMatieres, notes, tabnomsEtundiants, tabnomsMatiere);printf("\n");
    afficherMoyennesgenerale(nombreEtudiants, nombreMatieres, notes, tabnomsEtundiants);printf("\n");
    affircherMoyenneMaxInformatique(nombreEtudiants, nombreMatieres, notes, indexinformatique, tabnomsEtundiants);printf("\n");
    admispourcentage(nombreEtudiants, nombreMatieres, notes, tabnomsEtundiants);printf("\n");
    matiereoulesetudiantscartonnent(nombreEtudiants, nombreMatieres, notes, tabnomsMatiere);
    
    return 0;
}