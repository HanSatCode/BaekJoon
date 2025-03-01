import sys
from collections import deque


def BFS():
    while queue:
        #print(graph)
        now = queue.popleft()

        move = [2 * now, now + 1, now - 1]
        for d in range(3):
            if (move[d] >= 0 and move[d] < 100001) and (not visited[move[d]]):
                graph[move[d]][0] = graph[now][0] + 1
                graph[move[d]][1] += 1
                queue.append(move[d])
                visited[move[d]] = True
            #방문은 했지만 방문한 시점의 값과 같을때?
            elif (move[d] >= 0 and move[d] < 100001) and (visited[move[d]]) and (graph[move[d]][0] == graph[now][0] + 1):
                graph[move[d]][1] += 1
                queue.append(move[d])


#나 / 동생
N, K = map(int, sys.stdin.readline().rstrip().split(' '))
graph = [[0, 0] for x in range(100001)] # 최소시간 / 횟수
visited = [False for x in range(100001)]
queue = deque()
queue.append(N)
visited[N] = True
if N == K:
    print(*[0, 1], sep = '\n')
else:
    BFS()
    print(*graph[K], sep="\n")