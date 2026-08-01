/* 
Ce programme calcule la moyenne de 3 réels saisi par L'utisateur 
*/
#include <stdio.h>


void main(){
    float a,b,c;
    printf("Veuillez saisir 3 réels nous vous donnerons la moyenne de ceux ci\n");
    scanf("%f %f %f",&a,&b,&c);
    printf("La moyenne de %f,%f et %f est %f",a,b,c,(a+b+c)/3);
}
