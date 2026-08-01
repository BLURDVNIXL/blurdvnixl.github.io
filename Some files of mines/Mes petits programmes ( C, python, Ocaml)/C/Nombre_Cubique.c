//nombre cubique
#include <stdio.h>


void main(){
    int n,j,a;
    printf("n = ");
    scanf("%d",&n);
    a=n;
    int b=n;
    while(n!=0){
        a+=(n%10)*(n%10)*(n%10);
        n=n/10;
    }
    if(b==a/2){
        printf("%d est cubique",b);
    }
    else{
        printf("%d n'est pas cubique",b);
    }

}
