#include <stdio.h>

int main() {
	int N;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		for(int space = i; space < N - 1; space++) {
			printf(" ");
		}
		for(int star = 0; star < (2 * i + 1); star++) {
			if (star % 2 == 0) {
				printf("*");
			} else {
				printf(" ");
			}
		}
		printf("\n");
	}
}