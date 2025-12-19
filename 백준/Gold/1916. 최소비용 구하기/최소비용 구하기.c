#include <stdio.h>
#include <stdlib.h>
#define MAXWEIGHT 100000000

typedef struct node {
	int node;
	int weight;
	struct node* next;
} Node;

typedef Node* NodePointer;

NodePointer* myGraph;
int numNodes; int numEdges;
int v; int w;
int* visited;
int* shortestPath;

int minimum() {
	int min = MAXWEIGHT; int minIndex = -1;
	for (int i = 1; i <= numNodes; i++) {
		if (!visited[i] && shortestPath[i] < min) {
			min = shortestPath[i];
			minIndex = i;
		}
	}
	return minIndex;
}

void findShortestPath(int v) {
	shortestPath[v] = 0;
	for (int i = 0; i < numNodes; i++) {
		int minIndex = minimum();
		if (minIndex == -1) break;
		visited[minIndex] = 1;
		for (NodePointer cur = myGraph[minIndex]; cur != NULL; cur = cur->next) {
			if (!visited[cur->node]) {
				if (shortestPath[minIndex] + cur->weight < shortestPath[cur->node]) {
					shortestPath[cur->node] = shortestPath[minIndex] + cur->weight;
				}
			}
		}
	}
}

int main(void) {
	scanf("%d", &numNodes); scanf("%d", &numEdges);

	visited = (int*)malloc((numNodes + 1) * sizeof(int));
	myGraph = (NodePointer*)malloc((numNodes + 1) * sizeof(NodePointer));
	shortestPath = (int*)malloc((numNodes + 1) * sizeof(int));
	
	for (int i = 1; i <= numNodes; i++) {
		myGraph[i] = NULL; visited[i] = 0; shortestPath[i] = MAXWEIGHT;
	}

	for (int i = 0; i < numEdges; i++) {
		int from, to, weight;
		scanf("%d %d %d", &from, &to, &weight);
		NodePointer newNode = (NodePointer)malloc(sizeof(Node));
		newNode->node = to; newNode->weight = weight; newNode->next = myGraph[from];
		myGraph[from] = newNode;
	}

	scanf("%d %d", &v, &w);

	findShortestPath(v);
	
	printf("%d", shortestPath[w]);
}