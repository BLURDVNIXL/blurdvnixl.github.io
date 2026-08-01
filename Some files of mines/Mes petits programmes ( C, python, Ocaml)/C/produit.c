#include <stdio.h>

void main(){
    int A[3][3]={2,20,14,3,50,6,5,2,7};
    int B[3][3]={1,14,1,6,20,68,10,30,52};
    int C[3][3];

    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            C[i][j]=0;
            for(int k=0;k<3;k++){
            C[i][j]+=(A[i][k])*(B[k][j]);
            }
        }
    }
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            if(j==0){printf("|");}
            printf("\t%d",C[i][j]);
            if(j==2){printf("\t|");}
        }
        printf("\n");
    }

}