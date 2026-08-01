#include <stdio.h>
#include <math.h>

void saisirNotes(float notes[], int taille) {
    for (int i = 0; i < taille; i++) {
        printf("Entrez la note %d: ", i + 1);
        scanf("%f", &notes[i]);
    }
}  
void afficher(float notes[], int taille) {
    printf("Les notes sont :\n");
    for (int i = 0; i < taille; i++) {
        printf("\t \t Note %d: %f\t", i + 1, notes[i]);
    }
    printf("\n");
}
float Moyenne(float notes[], int taille) {
    int somme = 0;
    for (int i = 0; i < taille; i++) {
        somme += notes[i];
    }
    return somme / taille;
}   
float EcartType(float notes[], int taille, float moyenne) {
    float sommeCarres = 0.0;
    for (int i = 0; i < taille; i++) {
        sommeCarres += (notes[i] - moyenne) * (notes[i] - moyenne);
    }
    return sqrt(sommeCarres / taille);
}   
float Max(float notes[], int taille) {
    int max = notes[0];
    for (int i = 1; i < taille; i++) {
        if (notes[i] > max) {
            max = notes[i];
        }
    }
    return max;}
float Min(float notes[], int taille) {
    int min = notes[0];
    for (int i = 1; i < taille; i++) {
        if (notes[i] < min) {
            min = notes[i];
        }
    }
    return min;
}
int positionMax(float notes[], int taille, float max) {

    int posMax = 0;
    for (int i = 0; i < taille; i++) {
        if (notes[i] == max) {
            posMax = i+1;break;
        }
    }
    return posMax;
}
char* supMoyenne(float notes[], int taille, float moyenne) {
    for (int i = 0; i < taille; i++) {
        if (notes[i] < moyenne) {
            return "NON";
        }
    }
    return "OUI";
}
int nombreAdmis(float notes[], int taille) {
    int cpt = 0;
    for (int i = 0; i < taille; i++) {
        if (notes[i] >= 10.0) {
            cpt++;
        }
    }
    return cpt;
}
float tabAdmis(float notes[], int taille, int nombreAdmis) {
    float admis[nombreAdmis];
    int j = 0;
    for (int i = 0; i < taille; i++) {
        if (notes[i] >= 10.0) {
            admis[j] = notes[i];
            j++;
        }
    }
    printf("Les notes des etudiants admis sont :\n");
    for (int i = 0; i < nombreAdmis; i++) {
        printf("\t \t Note %d: %f\t", i + 1, admis[i]);
    }
    printf("\n");
}
int n;

int main() {
    printf("Saisissez le nombre d'etudiants \n");scanf("%d", &n);float notes[n];
    saisirNotes(notes, n);afficher(notes, n);
    float moyenne = Moyenne(notes, n); float ecartType = EcartType(notes, n, moyenne); float max = Max(notes, n); float min = Min(notes, n);
    printf("[ Moyenne: %f\t |Ecart Type: %f\t |Note Max: %f\t |Note Min: %f ]\n", moyenne, ecartType, max, min);
    int posMax = positionMax(notes, n, max);
    printf("La position du premier etudiant ayant la note maximale est: %d\n", posMax);
    printf("\nNous allons verifier si toutes les notes sont superieures a la moyenne %f et repondre par oui si c'est le cas et non sinon.\n", moyenne);
    printf("Resultat : %s\n", supMoyenne(notes, n , moyenne));
    printf("\nLe nombre d'etudiants admis est: %d\n", nombreAdmis(notes, n));
    tabAdmis(notes, n, nombreAdmis(notes, n));
    return 0;
}