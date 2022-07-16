#include <stdio.h>
int main(){
    int H, M;
    scanf("%d %d", &H, &M);

    if(M-45<0) {
        if(H==0) {
            printf("%d %d", 23, 60+(M-45));
        }
        else {
            printf("%d %d", H-1, 60+(M-45));
        }
    }
    else {
        printf("%d %d", H, M-45);
    }
}