#include <stdio.h>
#include <stdlib.h>

//2차원 동적 배열 할당 함수
int** array;

int main(void) {
	int N; scanf("%d", &N); // 노드 수
	array = (int**)malloc(N * sizeof(int*)); // 1차원 배열 할당
	for (int i = 0; i < N; i++) {
		array[i] = (int*)malloc(N * sizeof(int)); // 2차원 배열 할당
		for (int j = 0; j < N; j++) {
			scanf("%d", &array[i][j]);
		}
	}

	for (int k = 0; k < N; k++) { // k번째 노드를 경유하자!
		for (int i = 0; i < N; i++) { // 행
			for(int j = 0; j < N; j++) { // 열
				// 이미 가는 길이 있거나, i에서 k로 가는 길이 있고, k에서 j로 가는 길이 있으면
				if (array[i][j] || (array[i][k] && array[k][j])) {
					array[i][j] = 1;
				}
			}
		}
	}

	for (int y = 0; y < N; y++) {
		for (int x = 0; x < N; x++) {
			printf("%d ", array[y][x]);
		}
		printf("\n");
	}
}