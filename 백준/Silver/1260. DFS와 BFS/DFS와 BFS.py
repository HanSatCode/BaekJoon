import sys

def DFS(index):
    visited[index] = True
    result_DFS.append(index)
    for x in range(N + 1):
        # 방문하지 않았고, 해당 지점의 값이 True일 경우
        if (not visited[x]) and (graph[index][x]):
            DFS(x)

def BFS(index):
    queue = [index]
    visited[index] = True
    while queue:
        index = queue.pop(0)
        result_BFS.append(index)
        for x in range(N + 1):
            if (not visited[x]) and (graph[index][x]):
                queue.append(x)
                visited[x] = True

N, M, V = map(int, sys.stdin.readline().rstrip().split(' '))

graph = [ [False for x in range(N + 1)] for y in range(N + 1)]



for x in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split(' '))
    graph[A][B] = True
    graph[B][A] = True
else:
    result_DFS = []
    visited = [False for x in range(N + 1)]
    DFS(V)
    print(*result_DFS, sep=' ')

    result_BFS = []
    visited = [False for x in range(N + 1)]
    BFS(V)
    print(*result_BFS, sep=' ')