import sys
from collections import deque

fix = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def BFS():
    global result
    while queue:
        #print(*graph, sep='\n')
        now = queue.popleft()
        for d in range(4):
            Fx = now[0] + fix[d][0]
            Fy = now[1] + fix[d][1]
            if (Fx >= 0 and Fx < M) and (Fy >= 0 and Fy < N) and graph[Fy][Fx] == 1:
                graph[Fy][Fx] = graph[now[1]][now[0]] + 1
                queue.append([Fx, Fy])

# N - 세로 / M - 가로
N, M = map(int, sys.stdin.readline().rstrip().split(' '))

graph = []
queue = deque()

for y in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
else:
    queue.append([0, 0])
    BFS()
    print(graph[-1][-1])