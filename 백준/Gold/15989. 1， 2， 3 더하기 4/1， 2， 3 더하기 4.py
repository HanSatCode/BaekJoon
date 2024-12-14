import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    if N == 1:
        print(1)
    else:
        dp = [[1] * (N+1)] + [ [1] + ([0] * (N))  for x in range(2) ]
        
        for x in range(1, 3): #2, 3
            for y in range(1, N + 1): #1 ~ N
                dp[x][y] = dp[x][y-(x+1)] + dp[x-1][y] 
        #print(*dp, sep='\n')
        print(dp[x][y])