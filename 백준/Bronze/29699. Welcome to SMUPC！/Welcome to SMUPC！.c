#include <stdio.h>

int main(void) {
	char str[] = "WelcomeToSMUPC";
	int n; scanf("%d", &n);
	printf("%c", str[--n % 14]);
}