#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
	int nodeNo; // 노드 번호
	int weight;	// 간선 가중치(길이)
	struct Node* next; // 다음 노드 포인터
} Node;

typedef Node* NodePointer;

typedef struct Graph {
	NodePointer* adjList; // 인접 리스트
} Graph;

Graph* createGraph(int num) { // 1베이스
	Graph* graph = (Graph*) malloc (sizeof(Graph));
	graph->adjList = (NodePointer*)malloc((num + 1) * sizeof(NodePointer));
	for (int i = 0; i <= num; i++) {
		graph->adjList[i] = NULL;
	}
	return graph;
}

int max = 0; int maxNode = -1; Graph* graph; int* visited;

void getMaxWeight(int nodeNo, int sum) {
	visited[nodeNo] = 1; // 방문 처리
	if (sum > max) {
		max = sum;
		maxNode = nodeNo;
	}
	NodePointer temp = graph->adjList[nodeNo];
	while (temp != NULL) {
		if (!visited[temp->nodeNo]) {
			getMaxWeight(temp->nodeNo, sum + temp->weight);
			visited[temp->nodeNo] = 0; // 갈래길에서 다른 쪽으로 가려면 복원해줘야 함
		}
		temp = temp->next;
	}
}

int main(void) {
	int nodeNo, weight, nextNodeNo;
	int N; scanf("%d", &N);
	graph = createGraph(N);
	visited = (int*) malloc ((N + 1) * sizeof(int));

	for (int i = 0; i <= N; visited[i++] = 0); // visited 초기화

	for (int i = 0; i < N; i++) {
		scanf("%d", &nodeNo);
		while (1) { // -1이 나올 때까지 입력하기
			scanf("%d", &nextNodeNo);
			if (nextNodeNo == -1) break;
			scanf("%d", &weight);

			Node* temp = (Node*)malloc(sizeof(Node));
			temp->nodeNo = nextNodeNo; temp->weight = weight;
			temp->next = graph->adjList[nodeNo]; // 스택처럼 넣기
			graph->adjList[nodeNo] = temp;
		}
	}
	getMaxWeight(1, 0); // 임의의 노드
	for (int i = 0; i <= N; visited[i++] = 0); // visited 초기화를 안함...
	getMaxWeight(maxNode, 0); // 가장 먼 노드에서 가장 먼 노드 = 지름
	printf("%d\n", max);
}