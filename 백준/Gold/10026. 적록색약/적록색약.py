import sys
sys.setrecursionlimit(100000)

fix = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def DFS_RGB(x, y, color):
    visited[y][x] = True
    for d in range(4):
        Fx = x + fix[d][0]
        Fy = y + fix[d][1]
        if (Fx >= 0 and Fx < N) and (Fy >= 0 and Fy < N) and (not visited[Fy][Fx]):
            if graph[Fy][Fx] == color:
                DFS_RGB(Fx, Fy, color)

def DFS_RGB2(x, y, color):
    visited2[y][x] = True
    for d in range(4):
        Fx = x + fix[d][0]
        Fy = y + fix[d][1]
        if (Fx >= 0 and Fx < N) and (Fy >= 0 and Fy < N) and (not visited2[Fy][Fx]):
            if graph2[Fy][Fx] == color:
                DFS_RGB2(Fx, Fy, color)

N = int(sys.stdin.readline().rstrip())

graph = []
graph2 = []
visited = [ [False for x in range(N) ] for y in range(N) ]
visited2 = [ [False for x in range(N) ] for y in range(N) ]
result_RGB = { 'R' : 0, 'G' : 0, 'B' : 0 }
result_RGB2 = { 'R' : 0, 'G': 0, 'B' : 0 }

for _ in range(N):
    temp = sys.stdin.readline().rstrip()
    graph.append(list(temp))
    graph2.append(list(temp.replace('G', 'R')))
else:
    for color in ['R', 'G', 'B']:
        for y in range(N):
            for x in range(N):
                if (graph[y][x] == color) and (not visited[y][x]):
                    DFS_RGB(x, y, color)
                    result_RGB[color] += 1
                if (graph2[y][x] == color) and (not visited2[y][x]):
                    DFS_RGB2(x, y, color)
                    result_RGB2[color] += 1
                        
    print(sum(result_RGB.values()))
    print(sum(result_RGB2.values()))