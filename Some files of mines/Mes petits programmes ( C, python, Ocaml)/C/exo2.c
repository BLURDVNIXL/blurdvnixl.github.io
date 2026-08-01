#include <stdio.h>

void remplir(int *a, int *b, float *x){
    *a=0;
    *b=0;
    *x=0.0;

}
void divise( int *p, int *q){
    int tempo;
    tempo=*p;
    *p= *p / *q;
    *q= tempo % *q;
}
void echange(int * a, int * b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}




int main() {
    int a, b;float x;
    remplir(&a, &b, &x);
    printf("a=%d b=%d c=%f\n", a, b, x);
    printf("Entrer deux entiers : ");
    scanf("%d %d", &a, &b);
	printf("Avant echange: a=%d b=%d\n", a, b);
	printf("\t\t//////Echange/////\n");
	echange(&a, &b);
    printf("Apres echange: a=%d b=%d\n", a, b);

    return 0;
}