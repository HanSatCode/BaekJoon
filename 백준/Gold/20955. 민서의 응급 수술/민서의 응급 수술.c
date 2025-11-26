#include <stdio.h>
#include <stdlib.h>

int* parent; // 부모 테이블
int result = 0; // 결과 변수

int Find(int target) {
	for (; parent[target] >= 0; target = parent[target]);
	return target;
}

void Union(int a, int b) {
	int rootA = Find(a); int rootB = Find(b); // 각 원소의 루트 노드

	int hap = parent[rootA] + parent[rootB]; // 두 집합의 크기 합
	if (rootA != rootB) {
		// 작은 쪽이 큰 쪽에 붙도록
		if (rootA < rootB) {	// rootA가 더 큰 집합 (더 작은 음수)
			parent[rootA] = hap;
			parent[rootB] = rootA;
		}
		else {	// rootB가 더 큰 집합
			parent[rootB] = hap;
			parent[rootA] = rootB;
		}
	}
	else result++; // 대표가 같은 경우, 사이클을 끊어내야함 (그냥 안넣는게 아니라)
}


int main(void) {
	int N, M; scanf("%d %d", &N, &M); // 노드 수, 사전정의된 집합 수
	parent = (int*) malloc ((N + 1) * sizeof(int)); // 부모 테이블
	for (int i = 0; i <= N; parent[i++] = -1); // 초기화
	

	for (int i = 0; i < M; i++) {
		int a, b; scanf("%d %d", &a, &b);
		Union(a, b);
	}

	for (int i = 1; i <= N; i++) {
		if (parent[i] < 0) result++;
	}
	printf("%d\n", result - 1); // 동치 클래스 - 1
}