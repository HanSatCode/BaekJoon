import sys

L1 = sys.stdin.readline().rstrip()
L2 = sys.stdin.readline().rstrip()

dp = [ [ 0 for x in range(len(L1) + 1) ] for y in range(len(L2) + 1) ]



for x in range(1, len(L1) + 1):
    for y in range(1, len(L2) + 1):
        if L1[x - 1] == L2[y - 1]:
            dp[y][x] = dp[y - 1][x - 1] + 1
        else:
            dp[y][x] = max(dp[y - 1][x], dp[y][x - 1])
else:
    #print(*dp, sep="\n")
    print(dp[len(L2)][len(L1)])