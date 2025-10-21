#include <stdio.h>

void hanoi(int N, int start, int end, int via) {
    if (N == 1) {
        printf("%d %d\n", start, end);
        return;
    }
    else {
        hanoi(N - 1, start, via, end);
        printf("%d %d\n", start, end);
        hanoi(N - 1, via, end, start);
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
	printf("%d\n", (1 << n) - 1);
    hanoi(n, 1, 3, 2);
}