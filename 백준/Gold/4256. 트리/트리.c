#include <stdio.h>
#include <stdlib.h>

int* preo; int* ino;


int findNodeIndex(int start, int end, int nodeData) {
	for (int i = start; i <= end; i++) {
		if (ino[i] == nodeData) return i;
	}
}

void solve(int preoStart, int inoStart, int inoEnd) {
	if (inoStart > inoEnd) return;
	int curNode = preo[preoStart];
	int nodeIndex = findNodeIndex(inoStart, inoEnd, curNode); // 좌/우 나누기 준비
	int lSize = nodeIndex - inoStart;
	solve(preoStart + 1, inoStart, nodeIndex - 1); // 좌측 : 탐색 시작, 왼쪽 부분
	solve(preoStart + 1 + lSize, nodeIndex + 1, inoEnd); // 우측 : 탐색 시작, 오른쪽 부분
	printf("%d ", curNode); // 후위 순회 출력
}

int main(void) {
	int T; scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		int n; scanf("%d", &n);
		preo = (int*) malloc (n * sizeof(int)); ino = (int*) malloc (n * sizeof(int));
		for (int j = 0; j < n; j++) {
			scanf("%d", &preo[j]);
		}
		for (int j = 0; j < n; j++) {
			scanf("%d", &ino[j]);
		}
		solve(0, 0, n-1);
		if (i != T - 1) printf("\n");
	}
}