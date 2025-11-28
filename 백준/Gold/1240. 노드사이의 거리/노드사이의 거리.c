#include <stdio.h>
#include <stdlib.h>

typedef struct node {
	int nodeNo;	// 노드의 데이터 필드
	int length; // 간선의 가중치
	struct node* next;	// 왼쪽 자식 노드 포인터
} Node;
typedef Node* NodePointer;	// 노드 포인터

typedef struct graph {
	NodePointer* adjList;	// 인접 리스트
} Graph;

Graph myGraph; int* visited;

void solve(int cur, int end, int length) {
	visited[cur] = 1;	// 현재 노드를 방문 처리
	if (cur == end) {	// 도착 노드에 도달한 경우
		printf("%d\n", length);	// 길이 출력하고 끝.
		return;
	}
	NodePointer temp = myGraph.adjList[cur]; // 인접 리스트를 가져옴
	while (temp != NULL) {
		if (!visited[temp->nodeNo]) {
			solve(temp->nodeNo, end, length + temp->length);
			visited[temp->nodeNo] = 0; // 백트래킹 위해 방문 해제
		}
		temp = temp->next;
	}
}


int main(void) {
	int N, M; scanf("%d %d", &N, &M);
	visited = (int*)malloc((N + 1) * sizeof(int));	// 방문 배열 동적 할당
	for (int i = 0; i <= N; i++) visited[i] = 0;	// 방문 배열 초기화
	myGraph.adjList = (NodePointer*)malloc((N + 1) * sizeof(NodePointer));	// 노드 번호는 1부터 시작
	for (int i = 1; i <= N; i++) {
		myGraph.adjList[i] = NULL;	// 인접 리스트 초기화
	}
	for (int i = 0; i < N-1; i++) {
		int nodeA, nodeB, weight; scanf("%d %d %d", &nodeA, &nodeB, &weight);
		NodePointer tempA = (NodePointer)malloc(sizeof(Node)); tempA->nodeNo = nodeB; tempA->length = weight;
		tempA->next = myGraph.adjList[nodeA]; myGraph.adjList[nodeA] = tempA;

		NodePointer tempB = (NodePointer)malloc(sizeof(Node)); tempB->nodeNo = nodeA; tempB->length = weight;
		tempB->next = myGraph.adjList[nodeB]; myGraph.adjList[nodeB] = tempB;
	}

	for (int i = 0; i < M; i++) {
		int start, end; scanf("%d %d", &start, &end);
		solve(start, end, 0);
		for (int i = 0; i <= N; i++) visited[i] = 0; // 꼭!!! 다음 문제를 위해 방문 배열 초기화
	}
}