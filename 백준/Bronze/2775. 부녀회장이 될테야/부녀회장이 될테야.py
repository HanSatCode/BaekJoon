import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    K = int(sys.stdin.readline().rstrip())
    N = int(sys.stdin.readline().rstrip())
    dp = [ [ x for x in range(N + 1) ] ] + [ [0, 1] + [0 for x in range(N - 1)] for y in range(K) ]

    for k in range(1, K + 1):
        for n in range(1, N + 1):
            dp[k][n] = dp[k - 1][n] + dp[k][n - 1]
    else:
        print(dp[K][N])