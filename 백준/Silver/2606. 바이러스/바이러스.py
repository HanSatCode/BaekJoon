import sys

def dfs(index) :
    visited[index] = 1
    for x in range(1, N+1):
        if graph[index][x] == 1 and visited[x] != 1:
            dfs(x)

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

graph = [ [ 0 for x in range(N + 1) ] for _ in range(N + 1) ]

visited = [ 0 for x in range (N + 1) ]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split(' '))
    graph[A][B] = 1
    graph[B][A] = 1
else:
    dfs(1)
    print(visited.count(1) - 1)