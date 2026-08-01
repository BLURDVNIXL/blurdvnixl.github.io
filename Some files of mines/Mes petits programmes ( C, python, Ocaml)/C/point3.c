#include <stdio.h>
#include <stdlib.h>

int main() {
    // Exemple 1 : Pointeur simple
    int x = 10;
    int* ptr = &x;  // ptr pointe vers x
    
    printf("Valeur de x : %d\n", x);
    printf("Adresse de x : %p\n", &x);
    printf("Valeur pointée par ptr : %d\n", *ptr);
    
    // Exemple 2 : Modifier une variable via un pointeur
    *ptr = 20;  // Change la valeur de x
    printf("x après modification : %d\n", x);
    
    // Exemple 3 : Allocation dynamique
    int* arr = malloc(3 * sizeof(int));
    arr[0] = 100;
    arr[1] = 200;
    arr[2] = 300;
    
    printf("arr[0] = %d\n", arr[0]);
    for(int i = 0; i < 3; i++) {
        printf("arr[%d] = %d\n", i, arr[i]);
    }
    
    free(arr);
    return 0;
}
