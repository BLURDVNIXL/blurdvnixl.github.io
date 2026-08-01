#include <stdio.h>
#include <math.h>

void main(){
    int n;
    long e,x,facto=1;

    printf("Entrez x et n: ");
    scanf("%ld %d",&x,&n);

    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
        facto=facto*j;
    }
        e+=(pow(x,i))/facto;

    }
}
