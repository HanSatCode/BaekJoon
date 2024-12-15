#메모리초과

import sys 

N = int(sys.stdin.readline().rstrip())
M = 0
C = []

while N >= 2 ** M:
    C.append(2 ** M)
    M += 1

#dp = [ [1] + [ 0 for x in range(N) ] for y in range(M + 1) ]
dp1 = [ 1 for x in range(N + 1) ]
dp2 = [1] + [0 for x in range(N)]

for x in range(1, M):
    for y in range(1, N + 1):
        #dp[x][y] = (dp[x-1][y] + dp[x][y-C[x-1]]) % 1000000000
        dp2[y] = (dp1[y] + dp2[y - C[x]]) % 1000000000
    else:
     #print(dp1, dp2, sep='\n')
     dp1 = dp2[:]
     dp2 = [1] + [0 for x in range(N)]


else:
    print(dp1[N])