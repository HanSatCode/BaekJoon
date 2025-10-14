#include <stdio.h>
#include <string.h>

int main(void) {
    char s[11]; scanf("%s", &s);
    long long result = 0;

    for(int i = 0; i < strlen(s); i++) {
        result *= 26;
        result += s[i] - 64;
    }
    printf("%lld\n", result); // 오버플로 조심
}