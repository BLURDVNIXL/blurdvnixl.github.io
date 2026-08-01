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


int main() {
    int a, b;float x;int p,q;
    remplir(&a, &b, &x);
    printf("a=%d b=%d c=%f\n", a, b, x);
    
    printf("Entrer deux entiers : ");
    scanf("%d %d", &p, &q);
    divise(&p, &q);
    printf("quotient=%d reste=%d\n", p, q);

    return 0;
}