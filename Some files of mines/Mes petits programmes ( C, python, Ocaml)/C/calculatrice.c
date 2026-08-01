#include <stdio.h>

void main(){
    float a,b;
    int i;
    while(1==1){
        printf("\n \t \t \t \t \t \t Quels sont vos nombres et quel opération souhaitez vous effectuer?\n\t+ (1)\n\t- (2)\n\tx (3)\n\t/ (4)\n");
        scanf("%f %f %d",&a,&b,&i);
        switch(i){
            case 1: printf("%f + %f = %f",a,b,a+b);break;
            case 2: printf("%f - %f = %f",a,b,a-b);break;
            case 3: printf("%f x %f = %f",a,b,a*b);break;
            case 4: if(b!=0){printf("%f / %f = %f",a,b,a/b);}
                    else{printf("Erreur ! Division par 0");}
                    break;
            default: printf("option non repertorié");
        }
    }
}