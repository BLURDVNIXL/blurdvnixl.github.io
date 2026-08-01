#include <string.h>
#include <stdio.h>


int repetition(char chaine[][50]){
    char cptstr;int cpt;
  cpt=0;
        for (int j = 0; j < strlen(chaine); j++)
        {
            cptstr = chaine[j];
            if (strcmp(chaine[j], cptstr) == 0) {//strcmp compare deux chaînes de caractères et retourne 0 si elles sont égales
            cpt++;
        }
        }    
return cpt;
    
}

void conway(int n){
    //char 

} 

char nombre[50];

int main() {
    printf("NOMBRE:\n");scanf("%s",nombre);
    


    return 0;
}