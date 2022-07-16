#include <stdio.h>
int n, i, r;

int main() {
	scanf("%d", &n);
	for(i=1; i<=n; i++){
		r += i;
	}
	printf("%d", r);
}