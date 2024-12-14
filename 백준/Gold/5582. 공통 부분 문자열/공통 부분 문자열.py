#이전번째의 알파벳도 같으면 +1을 해준다는 점에 집중
#0이면 신규 문자열라서 상관없음
#메모리 초과..?
import sys

L1 = ' ' + sys.stdin.readline().rstrip()
L2 = ' ' + sys.stdin.readline().rstrip()

result = 0

dp = [ [ 0 for x in range(len(L2)) ] for y in range(len(L1)) ]
for x in range(1, len(L1)):
    for y in range(1, len(L2)):
        if L1[x] == L2[y]:
            dp[x][y] = dp[x-1][y-1] + 1
            result = max(result, dp[x][y])
#print(*dp, sep='\n')
print(result)