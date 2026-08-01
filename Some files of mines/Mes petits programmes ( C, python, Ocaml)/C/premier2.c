// Ce programme ramène la liste des nombres 1er compris entre 2 entiers
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

int premier(int b){
    int test;

    if(b==2){
        return 1;
    }
    else if(b==0 || b==1){
        return 0;
    }
    else { 
        for (int i=2;i<b ;i++){
            test=b % i;
            if(test==0){
                return 0;
                break;
            }
        }
    }
    return 1; 
    } 

void main(){
    int n,ch;

    printf("Entrer un entier SVP\n");
    scanf("%d",&n);
    printf("Un second\n");
    scanf("%d",&ch);
    printf("\n");
    
        for(int j=n;j<=ch;j++){
            if(premier(j)==1){
                printf("%d \n",j);
            }
        }
}
    
