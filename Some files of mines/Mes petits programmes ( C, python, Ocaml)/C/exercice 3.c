#include <stdio.h>
#include <stdbool.h>


bool stochastique(int n,int P[n][n]){
    int x; 
    for(int i=0 ; i<n; i++){
        for (int j = 0; j < n; j++)
        {
            if (P[i][j]<0)
            {
                return false;
            }
            
        }
        
    }
    for (int i = 0; i < n; i++)
    {
        int s=0;
        for(int j=0; j<n ; j++){
            s+=P[i][j];
        }
        if (s!=1) return false;
        else x++;
        }
        if (x==n) return true;
    
}

int main() {
    int n;
    printf("Entrez la taille de la matrice : ");
    scanf("%d", &n);
    int P[n][n];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("Remplissez la matrice");
            printf("\n P[%d][%d] = ", i, j);
            scanf("%d", &P[i][j]);
        }
        
    }
    if (stochastique(n,P[n][n])==true) printf("Votre matrice est stochastique ");
    else printf("Votre matrice n'est pas stochastique ");
    return 0;
}