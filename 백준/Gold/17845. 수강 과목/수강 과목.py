import sys 

#N 최대 공부시간, K 과목 수
N, K = map(int, sys.stdin.readline().rstrip().split(' '))
dp = [ [ 0 for x in range (N + 1) ] for y in range(K + 1) ]
S = [ [-1, -1] ]
for _ in range(K): #S[0] 중요도, S[1] 공부시간
    S.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

for x in range (1, K + 1):
    for y in range (1, N + 1):
        if y < S[x][1]:
            dp[x][y] = dp[x-1][y]
        else:
            dp[x][y] = max(dp[x-1][y], dp[x-1][y-S[x][1]] + S[x][0])

else:
    print(dp[K][N])