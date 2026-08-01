/*ce programme permet de résoudre une équation du second dégré dans résoudre
*/
#include <stdio.h>
#include <math.h>

void main(){
    float a,b,c;
    printf("veuillez entrez les nombres a,b et c de votre équation ax²+bx+c=0\n\t");
    scanf("%f %f %f",&a,&b,&c);
    if(a==0){
        printf("la solution est x= %f",-c/b);
    }
    else{
        if(b*b-4*a*c==0){
            printf("l'équation admet une racine double x=%f",-(b/(2*a)));
        }
        if(b*b-4*a*c<0){
            printf("Votre équation n'a pas de solution réel");
        }
        else{
            printf("les 2 solutions sont:\n x1= %f \n x2= %f",(-b-sqrt(b*b-4*a*c))/(2*a),(-b+sqrt(b*b-4*a*c))/(2*a));
        }
    }

}
