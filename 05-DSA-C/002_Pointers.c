#include <stdio.h>
int main() {
int x = 10;
int *p;
p = &x;
printf("%d", *p); //Output:10
printf("\n%d",x); //Output:10

return 0;
}


