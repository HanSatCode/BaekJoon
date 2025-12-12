#include <stdio.h>
#include <stdlib.h>
#define NO_EDGE 100000*100

//2차원 동적 배열 할당 함수
int** graph;

int main(void) {
	int n; scanf("%d", &n); // 노드 수
	int m; scanf("%d", &m); // 간선 수

	graph = (int**)malloc(n * sizeof(int*)); // 1차원 배열 할당
	for (int i = 0; i < n; i++) {
		graph[i] = (int*)malloc(n * sizeof(int)); // 2차원 배열 할당
		for (int j = 0; j < n; j++) {
			if (i == j) graph[i][j] = 0; // 자기 자신으로 가는 길은 0
			else graph[i][j] = NO_EDGE; // 일단 못가는 길
		}
	}

	int from, to, weight;
	for (int i = 0; i < m; i++) {
		scanf("%d %d %d", &from, &to, &weight);
		if (graph[from - 1][to - 1] > weight) { // 입력에 출발지 목적지지만 가중치가 다름...
			graph[from - 1][to - 1] = weight; // 방향 그래프
		}
	}

	for (int k = 0; k < n; k++) { // k를 경유하자!
		for (int i = 0; i < n; i++) { // 행 (출발지)
			for (int j = 0; j < n; j++) { // 열 (목적지)
				// 만약에, k를 경유하는 게 더 빠르면?
				if (graph[i][j] > graph[i][k] + graph[k][j]) {
					graph[i][j] = graph[i][k] + graph[k][j];
				}
			}
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			// 가중치 최대가 10만 아래인거지, 가중치 합은 그 이상일 수도 있음...
			if (graph[i][j] == NO_EDGE) printf("0 "); // 못 가는 길
			else printf("%d ", graph[i][j]); 
		}
		printf("\n");
	}
}