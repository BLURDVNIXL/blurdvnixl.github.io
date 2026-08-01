#include <stdio.h>

void remplirTableau(int * tab, int size)
{
    int i;
    for (i = 0; i < size; i++)
    {
        *(tab + i) = 100 * i; // <=> tab[i] = 100 * i
    }
}

int main()
{
    int tabEntier[5];
    int taille = 5;
    int i;

    // tabEntier <=> &tabEntier[0]
    // tab[i] <=> *(tab + i)

    for (i = 0; i < taille; i++)
    {
        printf("tabEntier[%d] = %d\n", i, tabEntier[i]);
    }

    remplirTableau(tabEntier, taille);
    printf("\n========\n");

    for (i = 0; i < taille; i++)
    {
        printf("tabEntier[%d] = %d\n", i, tabEntier[i]);
    }
    
    return 0; // Added return statement for completeness in main
}