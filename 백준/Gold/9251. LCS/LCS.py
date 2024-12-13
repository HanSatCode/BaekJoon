import sys

L1 = ' ' + sys.stdin.readline().rstrip()
L2 = ' ' + sys.stdin.readline().rstrip()

L1_length = len(L1)
L2_length = len(L2)

dp = [ [ 0 for x in range(L2_length)] for y in range(L1_length) ]

for x in range(1, L1_length):
    for y in range(1, L2_length):
        if L1[x] == L2[y]: #맞으면
                dp[x][y] = dp[x-1][y-1] + 1
        else: #아니면
            dp[x][y] = max(dp[x][y-1], dp[x-1][y])
else:
    #print(*dp, sep="\n")
    print(dp[L1_length - 1][L2_length - 1])