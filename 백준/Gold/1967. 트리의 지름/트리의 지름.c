#include <stdio.h>
#include <stdlib.h>

typedef struct node {
	int nodeNo;
	int weight;
	struct node* nextNode;
}Node;

typedef Node* NodePointer;

typedef struct graph {
	NodePointer* adjList; // 인접 리스트
} Graph;

int* visited; Graph* graph; int maxNode = -1; int max = -1;

void DFS(int start, int sum) {
	if (sum > max) {
		max = sum;
		maxNode = start;
	}

	visited[start] = 1; // 방문 처리
	NodePointer temp = graph->adjList[start];
	while (temp != NULL) {
		if (!visited[temp->nodeNo]) { // 방문하지 않은 길
			DFS(temp->nodeNo, sum + temp->weight);
			visited[temp->nodeNo] = 0;
		}
		temp = temp->nextNode;
	}
}

int main(void) {
	int N; scanf("%d", &N); // 노드 수
	int start, end, weight; // 간선 정보
	visited = (int*)malloc(sizeof(int) * (N + 1));
	graph = (Graph*)malloc(sizeof(Graph));

	graph->adjList = (NodePointer*)malloc(sizeof(NodePointer) * (N + 1));
	for (int i = 0; i <= N; i++) graph->adjList[i] = NULL; // 인접 리스트 초기화

	for (int i = 0; i < N-1; i++) {
		scanf("%d %d %d", &start, &end, &weight);
		NodePointer temp = (NodePointer) malloc (sizeof(Node));
		temp->nodeNo = end; temp->weight = weight; temp->nextNode = graph->adjList[start];
		graph->adjList[start] = temp;
		temp = (NodePointer)malloc(sizeof(Node));
		temp->nodeNo = start; temp->weight = weight; temp->nextNode = graph->adjList[end];
		graph->adjList[end] = temp;
	}

	for (int j = 0; j <= N; visited[j++] = 0); // visited 초기화.
	DFS(1, 0); max = 0; // 1번 노드에서 시작
	for (int j = 0; j <= N; visited[j++] = 0); // visited 초기화.
	DFS(maxNode, 0); // maxNode에서 시작
	printf("%d\n", max);
}