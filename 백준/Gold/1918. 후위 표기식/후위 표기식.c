#include <stdio.h>
#define MAX_STACK_SIZE 100
#define MAX_EXPR_SIZE 100

typedef enum {
	lparen, rparen, plus, minus, times,
	divide, eos, operand
} precedence;

int icp[] = { 20, 19, 12, 12, 13, 13, 0 }; // 들어갈 때의 우선순위
int isp[] = { 0, 19, 12, 12, 13, 13, 0 }; // 안에 있을 때의 우선순위

char stack[MAX_STACK_SIZE];
char expr[MAX_EXPR_SIZE];
int top = -1;

void push(char c) {
	stack[++top] = c;
}

char pop() {
	return stack[top--];
}

precedence getToken(char* symbol, int* n) {
	*symbol = expr[(*n)++];
	switch (*symbol) {
	case '(': return lparen;
	case ')': return rparen;
	case '+': return plus;
	case '-': return minus;
	case '*': return times;
	case '/': return divide;
	case '\0': return eos;
	default: return operand;
	}
}

void print_token(precedence token) {
	switch (token) {
		case plus: printf("+"); break;
		case minus: printf("-"); break;
		case divide: printf("/"); break; 
		case times: printf("*"); break;
	}
}

void postfix(void) {
	char symbol;
	precedence token;
	int n = 0; // 인덱스
	top = 0; // 스택의 최상단 인덱스
	stack[0] = eos; // 가장 낮은 우선순위를 넣어서 위로 쌓을 수 있게끔 만듦

	for (token = getToken(&symbol, &n); token != eos; token = getToken(&symbol, &n)) {
		if (token == operand) { // 피연산자 (숫자일경우)
			printf("%c", symbol); // 그대로 출력
		}
		else if (token == rparen) { // 오른쪽 괄호일경우
			while (stack[top] != lparen) { // 왼쪽 괄호가 나올때까지 쌓은 것들을 제거함
				print_token(pop());
			}
			pop(); // 왼쪽 괄호를 제거함
		}
		else {
			while (isp[stack[top]] >= icp[token]) { // 스택 내 우선순위가 높거나 같은 것들을 제거함
				print_token(pop());
			}
			push(token); // 다 꺼냈으면 넣기
		}
	}
	while ((token = pop()) != eos) { // 수식의 끝을 만날경우, 모두 제거하여 모두 출력
		print_token(token);
	}
}

int main() {
	scanf("%s", expr);
	postfix();
}