import sys

N, K = map(int, sys.stdin.readline().rstrip().split(" "))
C = []
for _ in range(N):
    C.append(int(sys.stdin.readline().rstrip()))
else:
    C = [0] + C

''' # 메모리 초과 + deepcopy 사용으로 시간초과
dp = [ [1] + [ 0 for x in range(K) ] for y in range(N + 1)]

for x in range(1, N + 1):  # 누적 코인 고른 갯수
    for y in range(1, K + 1): # 1 ~ K까지의 경우의 수
        dp[x][y] = dp[x][y - C[x]] + dp[x - 1][y]
    print(dp[x])
else:
    print(dp[N][K])
'''

dp1 = [1] + [ 0 for x in range(K)]

for x in range(1, N + 1):
    dp2 = [1] + [ 0 for x in range(K)]
    if C[x] <= K: # 금액보다 코인의 가치가 더 클 수도 있다는 것을 고려해야 함
        for y in range(1, K + 1):
            dp2[y] = dp2[y - C[x]] + dp1[y]
    dp1 = dp2[:]
else:
    print(dp2[K])