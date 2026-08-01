#include <stdio.h>

void main(){
    int tab[3][3]={2,20,14,3,50,6,5,2,7};
    int tabt[3][3];
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            tabt[i][j]=tab[j][i];
        }
    }
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            if(j==0){printf("|");}
            printf("\t%d",tabt[i][j]);
            if(j==2){printf("\t|");}
        }
        printf("\n");
    }
    int tr=0;
    for(int i=0;i<3;i++){
        tr+=tab[i][i];
    }
    printf("La trace de A est %d\t\t",tr);

}