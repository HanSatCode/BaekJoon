import sys

N = int(sys.stdin.readline().strip())
L = list(map(int, sys.stdin.readline().strip().split(' ')))
visited = [ 0 for x in range(N + 1) ] # 1-based
M = 0
R = 0
for x in L:
    if not visited[x]:
        visited[x] = 1
        M += 1
        if R < M: R = M
    else:
        visited[x] = 0
        M -= 1
print(R)