// Dans ce code, il sagit de calculer la factorielle d'un entier n saisit par l'utilisateur
#include <stdio.h>

int a,n;
void main(){
    printf("Veuillez saisir un entier n SVP ");
    scanf("%d",&n);
    a=1;
    for(int i=2;i<=n;i++){
        a=a*i;
    }
    printf("%d! = %d\n\n",n,a);
}
