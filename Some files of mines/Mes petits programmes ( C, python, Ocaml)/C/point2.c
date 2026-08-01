#include <stdio.h>

int main() {
    // Déclaration d'une variable
    int x = 10;
    
    // Déclaration d'un pointeur et initialisation avec l'adresse de x
    int *ptr = &x;
    
    // Afficher la valeur de x
    printf("Valeur de x: %d\n", x);
    
    // Afficher l'adresse de x
    printf("Adresse de x: %p\n", &x);
    
    // Afficher la valeur pointée par ptr (déréférencement)
    printf("Valeur pointée par ptr: %d\n", *ptr);
    
    // Afficher l'adresse stockée dans ptr
    printf("Adresse stockée dans ptr: %p\n", ptr);
    
    // Modifier x via le pointeur
    *ptr = 20;
    printf("Nouvelle valeur de x: %d\n", x);
    
    return 0;
}