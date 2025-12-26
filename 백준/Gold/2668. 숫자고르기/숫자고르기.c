#include <stdio.h>
#include <stdlib.h>

int N;
int adj[101]; // 인접리스트
int visited[101]; // 방문 리스트
int checked[101]; // 체크 리스트
int result[101]; // 결과 리스트

int cnt = 0;

void dfs(int start, int cur) {
	visited[cur] = 1;
	checked[adj[cur]] = 1;
	if (!visited[adj[cur]]) { // 방문하지않았다면..
		dfs(start, adj[cur]);
	}
	else if (start == adj[cur]) return;
}

int main(void) {
	scanf("%d", &N);
	for (int i = 1; i <= N; i++) {
		scanf("%d", &adj[i]);
	}
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; visited[j] = 0, checked[j++] = 0);
		dfs(i, i); int isSame = 1;

		for (int j = 1; j <= N; j++) {
			if (visited[j] != checked[j]) {
				isSame = 0; break;
			}
		}

		if (isSame) {
			if (!result[i]) {
				result[i] = 1; cnt++;
			}
		}
	}

	printf("%d\n", cnt);
	for (int i = 1; i <= N; i++) {
		if (result[i]) printf("%d\n", i);
	}
}