//racine carrée
#include <stdio.h>
#include <math.h>

void main(){

    float A,Xn,Xn1;
    printf("entrez A ");
    scanf("%f",&A);
    Xn=A;
    Xn1=(Xn+(A/Xn))/2;
    do{
        Xn=Xn1;
        Xn1=(Xn+(A/Xn))/2;
        
    }
    while(fabs(Xn-Xn1)>=0.0000000000000000000000000000000000000001);
    printf("%f",Xn1);
    printf("%f",sqrtf(Xn1));
}
