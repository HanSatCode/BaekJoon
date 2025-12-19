#include <stdio.h>
#include <stdlib.h>

typedef struct node {
	int data;
	struct node* lchild;
	struct node* rchild;
} Node;

typedef Node* NodePointer;

NodePointer tree;

int nodeCnt;
int postIndex;

int* inorder;
int* postorder;

int findIndex(int start, int end, int num) {
	for (int i = start; i <= end; i++) { // end도 포함해야함!!
		if (inorder[i] == num) return i;
	}
	return -1; // 반드시 리턴해서... 있으나마나.
}

NodePointer makeTree(int start, int end) {
	if (start > end) return NULL;
	
	int curData = postorder[postIndex--];
	NodePointer newNode = (NodePointer)malloc(sizeof(Node));
	newNode->data = curData; newNode->lchild = NULL; newNode->rchild = NULL;

	int index = findIndex(start, end, curData);

	newNode->rchild = makeTree(index + 1, end); // 오른쪽이 루트랑 더 가까워야함.. (LRV / LVR)
	newNode->lchild = makeTree(start, index - 1);
	
	return newNode;
}

void preorder(NodePointer ptr) {
	if (ptr) {
		printf("%d ", ptr->data);
		preorder(ptr->lchild);
		preorder(ptr->rchild);
	}
}

int main(void) {
	scanf("%d", &nodeCnt); postIndex = nodeCnt - 1;
	inorder = (int*)malloc(nodeCnt * sizeof(int));
	postorder = (int*)malloc(nodeCnt * sizeof(int));

	for (int temp, i = 0; i < nodeCnt; i++) {
		scanf("%d", &temp); inorder[i] = temp;
	}
	for (int temp, i = 0; i < nodeCnt; i++) {
		scanf("%d", &temp); postorder[i] = temp;
	}
	tree = makeTree(0, postIndex);

	preorder(tree);
}