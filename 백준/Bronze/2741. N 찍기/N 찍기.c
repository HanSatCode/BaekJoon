#include <stdio.h>
int a, i;
int main(){
	scanf("%d", &a);
	for(i=1; a>=i; i++){
		printf("%d\n", i);
	}
}