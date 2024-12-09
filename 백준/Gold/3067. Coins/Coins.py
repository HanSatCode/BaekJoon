import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    C = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    M = int(sys.stdin.readline().rstrip())
    dp = [0 for x in range(M + 1)]
    dp[0] = 1
    for coin in C:
        for x in range(coin, M + 1):
            dp[x] = dp[x] + dp[x-coin]
    else:
        print(dp[-1])