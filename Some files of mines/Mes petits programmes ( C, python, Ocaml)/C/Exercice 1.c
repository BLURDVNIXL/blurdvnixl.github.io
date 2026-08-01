/* Ce programme a pour but de demander à l'utilisateur d'entrer son prénoms et son âge,
puis affiche un message du type: Bonjour [prénom], tu as [âge] ans 
*/

#include <stdio.h>

void main(){
    char nom[100];
    int age;
    
    printf("Entrez votre prénom SVP ");
    scanf("%99s",nom);
    printf("Quel âge avez-vous ? ");
    scanf("%d", &age);
    printf("Bonjour %s, tu as %d ans",nom,age);
}       