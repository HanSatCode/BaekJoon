import sys
sys.setrecursionlimit(10000)

# 0 없음 / 1 있음(방문안함) / -1 방문함

Fx = [-1, 1, 0, 0]
Fy = [0, 0, -1, 1]

def solve(x, y):
    if x >= 0 and x < M and y >= 0 and y < N:
        if graph[y][x] == 1:
            graph[y][x] = -1
            for a in range(4):
                solve(x + Fx[a], y + Fy[a])

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split(' '))
    
    graph = [[0 for x in range(M)] for y in range(N)]
    result = 0
    
    for b in range(K):
        x, y = map(int, sys.stdin.readline().rstrip().split(' '))
        graph[y][x] = 1

    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                solve(x, y)
                result += 1
    else:
        #print(*graph, sep="\n")
        print(result)