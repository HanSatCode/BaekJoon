import sys

N, T = map(int, sys.stdin.readline().rstrip().split(' '))
L = [] #L[x][0] 시간 / L[x][1] 배점
for _ in range(N):
    L.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
else:
    L = [0] + L
dp = [ [ 0 for x in range(T + 1) ] for y in range(N + 1) ]

for x in range(1, N + 1):
    for y in range(1, T + 1):
        if y < L[x][0]:
            dp[x][y] = dp[x-1][y]
        else:
            dp[x][y] = max(dp[x-1][y-L[x][0]] + L[x][1], dp[x-1][y])

print(dp[x][y])