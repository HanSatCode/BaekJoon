import sys

N = int(sys.stdin.readline().rstrip())
R = list(map(int, sys.stdin.readline().rstrip().split(" ")))

# 0: 매 회차 당 단죄하지 않았지만 조건 만족
# 1: 바로 이전과 동시에, 이전 표적 버리고 단독으로 단죄할 때 중 작은 것

dp = [ [0, R[0]] ] +[ [0, 0] for x in range(N - 1)]

if N != 1:
    for x in range(N):
        dp[x][0] = dp[x - 1][1]
        dp[x][1] = min(dp[x - 1][0], dp[x - 1][1]) + R[x]
    else :
        print(min(dp[N - 1][0], dp[N - 1][1]))
else :
    print(0)