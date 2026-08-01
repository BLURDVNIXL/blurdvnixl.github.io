#include <stdio.h>
#include <ctype.h>




/* ===== QUESTION 1 ===== */
typedef struct {
    char nom[50];
    int age;
    int matricule;
    float notes[3];
    int nombrenote;
    float moyenne;
} Etudiant;

/* ===== Mise en majuscules ===== */
void to_upper(char *s)
{
    for (int i = 0; s[i]; i++)
        s[i] = (char) toupper((unsigned char)s[i]);
}




/* ===== Moyenne étudiant ===== */
float moyenneEtudiant(Etudiant e)
{;
    float somme = 0.0f;
    for (int i = 0; i < e.nombrenote; i++)
       somme += e.notes[i];
    return somme / e.nombrenote;
}


void afficherinfo(Etudiant e){
    printf("\t INFORMATION SUR L'ETUDIANT : \n -NOM: %s \n -AGE: %d \n -MATRICULE: %d ",e.nom,e.age,e.matricule);
    
    for (int i = 0; i < e.nombrenote; i++) {
        printf("\n \t Note %d : %.2f\n", i + 1,e.notes[i]);
    }
    printf("LA MOYENNE DE L'ETUDIANT %s EST : %.2f", e.nom, moyenneEtudiant(e));
    
}





/* ===== MAIN ===== */
int main(void)
{
    
    Etudiant e;

    printf(" \t ===== SUPPOSONS QUE L'ETUDIANT A 3 NOTES ===== \n");e.nombrenote=3;
    


    printf("NOM : ");
    scanf("%49s", e.nom);
    to_upper(e.nom);

    printf("AGE : ");
    scanf("%d", &e.age);

    printf("MATRICULE : ");
    scanf(" %d", &e.matricule);
   
    
    for (int i = 0; i < e.nombrenote; i++) {
        printf("Note %d : ", i + 1);
        scanf("%f", &e.notes[i]);
    }

    printf("\t INFORMATION SUR L'ETUDIANT : \n -NOM: %s \n -AGE: %d \n -MATRICULE: %d ",e.nom,e.age,e.matricule);
    
    for (int i = 0; i < e.nombrenote; i++) {
        printf("\n \t Note %d : %.2f\n", i + 1,e.notes[i]);
    }

 
    printf(" \t ===== QUEL EST LE REEL NOMBRE DE NOTE DE L'ETUDIANT ?===== \n");scanf("%d",&e.nombrenote);

/*
    printf("NOM : ");
    scanf("%49s", e.nom);
    to_upper(e.nom);

    printf("AGE : ");
    scanf("%d", &e.age);

    printf("MATRICULE : ");
    scanf(" %d", &e.matricule);*/
   
    
    for (int i = 0; i < e.nombrenote; i++) {
        printf("Note %d : ", i + 1);
        scanf("%f", &e.notes[i]);
    }

   /* printf("\t INFORMATION SUR L'ETUDIANT : \n -NOM: %s \n -AGE: %d \n -MATRICULE: %d ",e.nom,e.age,e.matricule);
    
    for (int i = 0; i < e.nombrenote; i++) {
        printf("\n \t Note %d : %.2f\n", i + 1,e.notes[i]);
    }*/
    afficherinfo(e);

    

   

    
    return 0;
}
