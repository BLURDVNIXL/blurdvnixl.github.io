#include <stdio.h>

void main(){

    float moy,a;
    int i=1;

    while(1){
        printf("Note %d : ",i);
        scanf("%f",&a);
        
        if(a>=0){
            moy+=a;
            i+=1;
        }
        else{
            break;
        }
        
    }
    printf("Moyenne de ces %d notes : %.2f",i-1,moy/(i-1));
}