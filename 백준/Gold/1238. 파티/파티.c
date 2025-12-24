#include <stdio.h>
#include <stdlib.h>
#define NONEDGE 1000000

int** graph; // 인접 행렬
int* visited;
int N, M, X; // 학생 수, 도로수, 목적지
int* shortestPath; // 최단 경로 저장 배열
int* revShortestPath; // 역방향 최단 경로 저장 배열

int selectMinimum() {
	int min = NONEDGE; int minIndex = -1;
	for (int i = 1; i <= N; i++) {
		if (visited[i] == 0 && shortestPath[i] < min) {
			min = shortestPath[i]; minIndex = i;
		}
	}
	return minIndex;
}

int revSelectMinimum() {
	int min = NONEDGE; int minIndex = -1;
	for (int i = 1; i <= N; i++) {
		if (visited[i] == 0 && revShortestPath[i] < min) {
			min = revShortestPath[i]; minIndex = i;
		}
	}
	return minIndex;
}

int main(void) {
	scanf("%d %d %d", &N, &M, &X);
	graph = (int**)malloc((N + 1) * sizeof(int*));
	visited = (int*)malloc((N + 1) * sizeof(int));
	shortestPath = (int*)malloc((N + 1) * sizeof(int));
	revShortestPath = (int*)malloc((N + 1) * sizeof(int));

	for (int i = 1; i <= N; i++) {
		graph[i] = (int*)malloc((N + 1) * sizeof(int));
		for (int j = 1; j <= N; j++) {
			if (i == j) graph[i][j] = 0;
			else graph[i][j] = NONEDGE;
		}
	}

	for (int i = 0; i < M; i++) {
		int a, b, t;
		scanf("%d %d %d", &a, &b, &t);
		graph[a][b] = t;
	}

	for (int x = 1; x <= N; visited[x++] = 0); visited[X] = 1;
	for (int x = 1; x <= N; shortestPath[x++] = graph[X][x]);
	for (int i = 1; i <= N; i++) {
		int via = selectMinimum(); 
		if (via == -1) break; visited[via] = 1;
		for (int j = 1; j <= N; j++) {
			if (!visited[j] && graph[via][j] != NONEDGE) {
				if (shortestPath[j] > shortestPath[via] + graph[via][j]) {
					shortestPath[j] = shortestPath[via] + graph[via][j];
				}
			}
		}
	}

	for (int x = 1; x <= N; visited[x++] = 0); visited[X] = 1;
	for (int x = 1; x <= N; revShortestPath[x++] = graph[x][X]);
	for (int i = 1; i <= N; i++) {
		int via = revSelectMinimum(); 
		if (via == -1) break; visited[via] = 1;
		for (int j = 1; j <= N; j++) {
			if (!visited[j] && graph[j][via] != NONEDGE) {
				if (revShortestPath[j] > revShortestPath[via] + graph[j][via]) {
					revShortestPath[j] = revShortestPath[via] + graph[j][via];
				}
			}
		}
	}

	int M = -1;
	for (int i = 1; i <= N; i++) {
		if (M < revShortestPath[i] + shortestPath[i])
			M = revShortestPath[i] + shortestPath[i];
	}
	printf("%d", M);
}