import sys
from collections import deque

# 상위 / 하위 / 우 / 좌 / 하 / 상 
move = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]

def BFS():
    while queue:
        #print(*graph, sep='\n')
        now = queue.popleft()
        for d in range(6):
            Fh = now[0] + move[d][0]
            Fx = now[1] + move[d][1]
            Fy = now[2] + move[d][2]
            if (Fh >= 0 and Fh < H) and (Fx >= 0 and Fx < M) and (Fy >= 0 and Fy < N) and (graph[Fh][Fy][Fx] == 0):
                queue.append([Fh, Fx, Fy])
                graph[Fh][Fy][Fx] = graph[now[0]][now[2]][now[1]] + 1



M, N, H = map(int, sys.stdin.readline().rstrip().split(' '))

graph = [[[0 for x in range(M)] for y in range(N)]for z in range(H)]
queue = deque()
result = 0

for height in range(H):
    for y in range(N):
        temp = list(map(int, sys.stdin.readline().rstrip().split(' ')))
        graph[height][y] = temp
        for x in range(M):
            if temp[x] == 1:
                queue.append([height, x, y])
else:
    BFS()
    for h in range(H):
        for y in range(N):
            for x in range(M):
                if graph[h][y][x] == 0:
                    print(-1)
                    exit()
            else:
                result = max(result, max(graph[h][y]))
    print(result - 1)