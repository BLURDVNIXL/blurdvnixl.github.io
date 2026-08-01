#include <stdio.h>

// Fonction addition (issue de l'image 30c962.png, mais corrigée selon ma réponse précédente si l'intention est l'addition)
// Note: Le code dans l'image 30c962.png utilise l'opérateur de multiplication (*), ici corrigé en addition (+)
int addition(int * x, int * y) {
    return *x + *y; 
}

void swap(int * x, int * y) {
    int tmp = *x;
    *x = *y;
    *y = tmp;
}

int main() {
    int a = 3;
    int b = 2;

    // Affichage initial (issu de l'image 30638a.png)
    printf("a = %d | b = %d\n", a, b);

    // Appel de la fonction swap (issu de l'image 30638a.png)
    swap(&a, &b);

    // Affichage après swap (issu de l'image 30638a.png)
    printf("Swap...\n");
    printf("a = %d | b = %d\n", a, b);
    
    /* // Bloc commenté pour l'addition (issu de l'image 30638a.png)
    int resultat = addition(&a, &b);
    
    // Affichage du résultat de l'addition (issu de l'image 30c962.png)
    printf("a + b = %d\n", resultat);
    */

    return 0;
}