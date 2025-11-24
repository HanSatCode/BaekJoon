#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>


typedef struct node{
	char data;
	struct node* left;
	struct node* right;
} Node;

typedef Node* NodePointer;

void preorder(NodePointer ptr) {
	if (ptr != NULL) {
		printf("%c", ptr->data);
		preorder(ptr->left);
		preorder(ptr->right);
	}
}

void inorder(NodePointer ptr) {
	if (ptr != NULL) {
		inorder(ptr->left);
		printf("%c", ptr->data);
		inorder(ptr->right);
	}
}

void postorder(NodePointer ptr) {
	if (ptr != NULL) {
		postorder(ptr->left);
		postorder(ptr->right);
		printf("%c", ptr->data);
	}
}

NodePointer findNode(NodePointer ptr, char key) {
	if (ptr == NULL) return NULL;
	if (ptr->data == key) return ptr;
	NodePointer found = findNode(ptr->left, key);
	if (found != NULL) return found;
	return findNode(ptr->right, key);
}


int main(void) {
	char a, b, c;
	NodePointer left, right;
	NodePointer tree = (Node*) malloc(sizeof(Node));
	tree->data = 'A'; tree->left = NULL; tree->right = NULL;

	int N; scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf(" %c %c %c", &a, &b, &c);
		NodePointer target = findNode(tree, a);
		
		if (b != '.') {
			left = (Node*)malloc(sizeof(Node));
			left->data = b; left->left = NULL; left->right = NULL;
			target->left = left;
		}
		else target->left = NULL;

		if (c != '.') {
			right = (Node*)malloc(sizeof(Node));
			right->data = c; right->left = NULL; right->right = NULL;
			target->right = right;
		}
		else target->right = NULL;
	}
	preorder(tree); printf("\n");
	inorder(tree); printf("\n");
	postorder(tree); printf("\n");
}