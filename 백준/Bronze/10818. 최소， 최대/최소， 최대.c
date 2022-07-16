#include <stdio.h>
int main(){
    int x, count, list;
    int max = -1000000;
    int min = 1000000;

    scanf("%d", &x);

    for (count=1; count<=x; count++){
        scanf("%d", &list);
        if (max <= list) {
            max = list;
        }
        if (min >= list) {
            min = list;
        }
    }
    printf("%d %d", min, max);
}