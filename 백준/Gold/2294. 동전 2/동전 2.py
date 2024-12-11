import sys

N, K = map(int, sys.stdin.readline().rstrip().split(" "))
C = []
for _ in range(N):
    C.append(int(sys.stdin.readline().rstrip()))
else:
    C = sorted(C)

dp = [0] + [10001 for x in range(K)]

for x in range(N):
    if C[x] > K: #IndexError 보완. 정렬했으니까 금액보다 크면 그 이후는 계산할 필요가 없음
        break
    for y in range(C[x], K+1):
        dp[y] = min(dp[y], dp[y-C[x]] + 1)
    
#print(dp)
if dp[K] == 10001: #"불가능할경우에는 -1을 출력한다"를 안읽음..
    print(-1)
else:
    print(dp[K])