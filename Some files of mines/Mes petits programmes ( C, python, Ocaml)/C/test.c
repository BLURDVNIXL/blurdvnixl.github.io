#include <stdio.h>
int main(void) {
int a = 0x63;
int b = 0x2A;
printf("%X\n", a & b);
printf("%X\n", a | b);
printf("%X\n", a ^ b);
return 0;
}