import sys
from collections import deque

fix = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def BFS() :
    while queue:
        now = queue.popleft() # x, y
        for x in range(4):
            Fx = now[0] + fix[x][0]
            Fy = now[1] + fix[x][1]
            if (Fx >= 0 and Fx < M) and (Fy >= 0 and Fy < N) and visited[Fy][Fx] == -1:
                if graph[Fy][Fx] == 0:
                    visited[Fy][Fx] = 0
                elif graph[Fy][Fx] == 1:
                    queue.append([Fx, Fy])
                    visited[Fy][Fx] = visited[now[1]][now[0]] + 1


# N - 세로 / M - 가로
N, M = map(int, sys.stdin.readline().rstrip().split(' '))

graph = []
queue = deque()

for line in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    graph.append(temp)
    for index in range(M):
        if temp[index] == 2:
            queue.append([index, line])
else:
    visited = [ [-1 for x in range(M)] for y in range(N)]
    BFS()
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 0 or graph[y][x] == 2:
                print(0, end = ' ')
            elif visited[y][x] == -1:
                print(-1, end = ' ')
            else:
                print(visited[y][x] + 1, end = ' ')
        print()