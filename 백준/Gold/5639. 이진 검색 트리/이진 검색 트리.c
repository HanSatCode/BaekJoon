#include <stdio.h>
#include <stdlib.h>

typedef struct node {
	int data;
	struct node* left;
	struct node* right;
} Node;

typedef Node* NodePointer;

void attach(NodePointer cur, int n) {
	if (n < cur->data) { // 왼쪽
		if (cur->left == NULL) { // 왼쪽 노드가 비어있는 경우...
			NodePointer temp = (NodePointer)malloc(sizeof(Node));
			temp->data = n; temp->left = NULL; temp->right = NULL;
			cur->left = temp;
			return;
		}
		return attach(cur->left, n);  // 있으면 그냥 방문
	}
	else {
		if (cur->right == NULL) { // 오른쪽 노드가 비어있는 경우...
			NodePointer temp = (NodePointer)malloc(sizeof(Node));
			temp->data = n; temp->left = NULL; temp->right = NULL;
			cur->right = temp;
			return;
		}
		return attach(cur->right, n); // 있으면 그냥 방문
	}
}

void postorder(NodePointer ptr) {
	if (ptr != NULL) {
		postorder(ptr->left);
		postorder(ptr->right);
		printf("%d\n", ptr->data);
	}
}

int main(void) {
	NodePointer root = (NodePointer) malloc (sizeof(Node));
	int n; scanf("%d", &n); root->data = n; root->left = NULL; root->right = NULL;
	
	while (scanf("%d", &n) != EOF) {
		attach(root, n);
	}
	postorder(root);
}