#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int location; // 현재 위치
    int count; // 이동 횟수
    struct node* next; // 다음 노드 포인터
} Node;
typedef Node* NodePointer;

NodePointer front = NULL; 
NodePointer rear = NULL;

int moveTable[101]; // 1~100 (뱀과 사다리 위치 저장)
int visited[101]; // 방문 배열

void addQueue(int location, int count) {
    NodePointer newNode = (NodePointer)malloc(sizeof(Node));
    newNode->location = location; newNode->count = count; newNode->next = NULL;
	if (front == NULL) { // 큐가 비어있을 때
        front = rear = newNode;
    }
    else {
        rear->next = newNode;
        rear = newNode;
    }
}

NodePointer deleteQueue() {
    if (front == NULL) return NULL;
    NodePointer temp = front;
    front = temp->next;
    if (front == NULL) rear = NULL;
    return temp;
}


int main(void) {
    for (int i = 0; i <= 100; moveTable[i] = -1, visited[i++] = 100);
    int ladder, sneke; scanf("%d %d", &ladder, &sneke);
    for (int i = 0; i < ladder + sneke; i++) {
        int start, end; scanf("%d %d", &start, &end);
        moveTable[start] = end; // 사다리 또는 뱀의 시작 위치에 도착 위치 저장
    }

	addQueue(1, 0); // 시작 위치와 이동 횟수 0으로 큐에 추가
    NodePointer next = deleteQueue(); // BFS를 위한 큐 초기화
    int minCount = -1; // 최소 이동 횟수
    

    while (next != NULL) {
        if (next->location == 100) { // 100에 도착했을 때
            printf("%d", next->count);
            break;
        }
        // 사다리와 뱀은 반드시 이동해야함!!!
        for (int i = 1; i <= 6; i++) { // 주사위 굴리기
            if (next->location + i > 100) continue; // 100을 초과하면 무시

            if (moveTable[next->location + i] != -1) { // 주사위 던지고 난 후, 위치에 뱀이나 사다리가 있는경우?
                visited[moveTable[next->location + i]] = next->count + 1;
                addQueue(moveTable[next->location + i], next->count + 1);
                continue;
            }

            if (next->count + 1 < visited[next->location + i]) { // 최소기록 인경우
                visited[next->location + i] = next->count + 1;
                addQueue(next->location + i, next->count + 1); // 주사위 눈만큼 이동
            }
        }
        next = deleteQueue();
        //printf("위치 : %d / 카운트 : %d\n", next->location, next->count);
        
    }
}