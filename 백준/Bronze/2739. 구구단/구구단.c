#include <stdio.h>
int main(){
    int a, b;
    scanf("%d", &a);
    for(b=1; b<=9; b++)
    {
        printf("%d * %d = %d\n", a, b, a*b);
    }
}