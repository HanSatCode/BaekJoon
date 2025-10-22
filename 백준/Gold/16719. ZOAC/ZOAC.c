#include <stdio.h>
#include <string.h>

void solve(char* str, int n) {
	if (n == 1) {
		printf("%s\n", str);
		return;
	}
	else {
		char t[100] = ""; strcpy(t, str);
		for (int i = 0; i < n - 1; i++) {
			if (str[i] > str[i + 1]) { // 앞이 더 클 때
				char temp[100]; strcpy(temp, str + i + 1);
				strcpy(str + i, temp); // str = str[:i] + str[i+1:]
				solve(str, n - 1);
				break;
			}
			else if (i == n - 2) { // 끝까지 왔을 때
				str[n - 1] = '\0'; // str = str[:n-1]
				solve(str, n - 1);
			}
		}
		printf("%s\n", t);
	}
}

int main(void) {
	char str[101];
	scanf("%s", str);
	solve(str, strlen(str));
}