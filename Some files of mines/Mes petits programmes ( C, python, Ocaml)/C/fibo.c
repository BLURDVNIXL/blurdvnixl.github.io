
void main(){

    int n,fn;
    
    while(1){
        int a,b,n;
        a=0;
        a=1;
        printf("\nQuel terme voulez-vous? : ");
        scanf("%d",&n);
        int tab[n];
        tab[0]=0;
        tab[1]=1;
        printf("F%d = ",n);
        
        if(n>1){
            for(int i=2;i<=n;i++){
                tab[i]=tab[i-2]+tab[i-1];
            }
        }
        printf("%d",tab[n]);
    }

}