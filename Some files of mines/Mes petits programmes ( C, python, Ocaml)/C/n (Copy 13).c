#include <stdio.h>

int main() {
int x = 10;
int *p = &x;
printf("x = %d\n", x);
printf("Adresse de x = %p\n", &x);
printf("p = %p\n", p);
printf("*p = %d\n", *p);
return 0;
}