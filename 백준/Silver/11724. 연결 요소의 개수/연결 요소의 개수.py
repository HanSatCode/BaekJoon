import sys
sys.setrecursionlimit(100000)

def DFS(index):
    visited[index] = True
    for x in range(1, N + 1):
        if (not visited[x]) and graph[index][x]:
            DFS(x)

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

graph = [[False for x in range(N + 1)] for y in range(N + 1)]
visited = [False for x in range(N + 1)]

for x in range(M):
    X, Y = map(int, sys.stdin.readline().rstrip().split(' '))
    graph[X][Y] = True
    graph[Y][X] = True
else:
    cnt = 0
    for x in range(1, N + 1):
        if not visited[x]:
            DFS(x)
            cnt += 1
    else:
        print(cnt)