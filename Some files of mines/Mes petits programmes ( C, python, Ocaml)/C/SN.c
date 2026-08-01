#include <stdio.h>

void main(){
    int n,sn,sn1;
    printf("n = ");
    scanf("%d",&n);
    sn=n;
    if(sn%2==0){
            sn1=sn/2;
        }
    else{
        sn1=3*sn1+3;
    }

    for(int i=1;i<=n;i++){
        if(sn%2==0){
            sn1=sn/2;
        }
        else if(sn%2==1){
            sn1=3*sn+1;
        }
        sn=sn1;
    }
    printf("%d",sn1);
}