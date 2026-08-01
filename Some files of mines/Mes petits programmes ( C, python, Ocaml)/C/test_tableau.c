#include <stdio.h>

void main(){
    int i,j,max,min;
    printf("combien de ligne et de colonne compte votre tableau ?\t");
    scanf("%d %d",&i,&j);
    int tab[i][j];
    j=i*j;
    printf("on va procéder à présent au remplissage du tableau.\n");
    max=tab[0][0];

    for(i=0;i<j;i++){
        scanf("%d",&tab[0][i]);
        
    }

    max,min=tab[0][0],tab[0][0];

    for(i=1;i<j;i++){
        max= (max<tab[0][i]) ? tab[0][i]:max;
        min= (min>tab[0][i]) ? tab[0][i]:min;
    }

    printf("max =%d\nmin = %d",max,min);
    }