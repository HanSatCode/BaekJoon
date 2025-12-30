#include <stdio.h>
#include <stdlib.h>

typedef struct node {
	int position;
	int time;
	struct node* next;
} Node;
typedef Node* NodePointer;

NodePointer front = NULL;
NodePointer rear = NULL;

int* line; int N, K; // 길, 시작점, 도착점

// 수빈 < 동생의 위치라는 보장이 없음.. 거꾸로도 생각해볼것

int main() {
	scanf("%d %d", &N, &K);

	if (N >= K) { printf("%d\n", N - K); return 0; }

	line = (int*) malloc (100001 * sizeof(int));
	for (int i = 0; i < 100001; i++) line[i] = 100000;

	front = (NodePointer)malloc(sizeof(Node));
	front->position = N; front->time = 0; front->next = NULL;
	rear = front;

	while (front != NULL) {
		int curPossition = front->position; int curTime = front->time;
		
		// 1. 1초후에 뒤로 한 칸 이동 + 범위 내에서 더 빨리 도달할 수 있을 때. (다익스트라)
		NodePointer temp = (NodePointer)malloc(sizeof(Node));
		if (curPossition - 1 >= 0 && line[curPossition - 1] > curTime + 1) { 
			line[curPossition - 1] = curTime + 1;
			temp->position = curPossition - 1; temp->time = curTime + 1; temp->next = NULL;
			rear->next = temp; rear = temp;
		}

		// 2. 1초후에 앞으로 한 칸 이동
		temp = (NodePointer) malloc (sizeof(Node));
		if (curPossition + 1 <= 100000 && line[curPossition + 1] > curTime + 1) {
			line[curPossition + 1] = curTime + 1;
			temp->position = curPossition + 1; temp->time = curTime + 1; temp->next = NULL;
			rear->next = temp; rear = temp;
		}

		// 3. 0초후에 2배 위치로 이동
		temp = (NodePointer) malloc (sizeof(Node));
		if (curPossition * 2 <= 100000 && line[curPossition * 2] > curTime) { 
			line[curPossition * 2] = curTime;
			temp->position = curPossition * 2; temp->time = curTime; temp->next = NULL;
			rear->next = temp; rear = temp;
		}
		front = front->next;
	}
	printf("%d\n", line[K]);
}