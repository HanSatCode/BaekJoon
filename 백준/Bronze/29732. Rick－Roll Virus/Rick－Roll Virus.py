import sys
import copy

N, M, K = map(int, sys.stdin.readline().rstrip().split(' '))
S = [' '] + list(sys.stdin.readline().rstrip())
SC = copy.deepcopy(S)

for x in range(1, N + 1):
    if S[x] == 'R':
        m, n = max(1, x - K), min(N, x + K)
        for y in range(m, n+1):
            #print(SC)
            SC[y] = 'R'
else:
    print("Yes" if SC.count('R') <= M else "No")