import sys
from collections import deque

fix = [ [1, 0], [-1, 0], [0, 1], [0, -1] ]

def DFS():
    while queue:
        #pop -> 시간 초과 (시간복잡도 O(N) 이라서 그런듯)
        #current = queue.pop(0) # current[0] -> y / current[1] -> x
        current = queue.popleft()
        for d in range(4):
            Fx = current[1] + fix[d][0]
            Fy = current[0] + fix[d][1]
            if (Fx >= 0 and Fx < M) and (Fy >= 0 and Fy < N) and (graph[Fy][Fx] == 0):
                graph[Fy][Fx] = graph[current[0]][current[1]] + 1
                queue.append([Fy, Fx])


# M - 가로 / N - 세로
M, N = map(int, sys.stdin.readline().rstrip().split(' '))

graph = []
queue = deque()
result = 0

for x in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    graph.append(temp)
    for index in range(M):
        if temp[index] == 1: #y, x임
            queue.append([x, index])
else:
    DFS()
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 0:
                print(-1)
                exit()
        else:
            result = max(result, max(graph[y]))
    else:
        print(result - 1)