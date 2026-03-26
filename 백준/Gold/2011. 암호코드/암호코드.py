import sys

N = sys.stdin.readline().strip()
dp = [ 0 for x in range(len(N) + 1) ]
dp[0] = 1; dp[1] = 1 # 공백 / 1번째자리의 경우의수

if N[0] == "0":
    print(0)
else:
    for x in range(2, len(N) + 1): # 2번째자리부터 탐색
        if int(N[x - 1]) > 0: dp[x] = dp[x] + dp[x - 1]
        if 10 <= int(N[x - 2 : x]) <= 26: dp[x] = dp[x] + dp[x - 2]

    print(dp[-1] % 1000000)