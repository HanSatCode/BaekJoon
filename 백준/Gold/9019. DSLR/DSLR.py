import sys
from collections import deque

# 추가1 1 -> 0001로 생각해야한다..

def BFS():
    while queue:
        now = queue.popleft()
        if now == B:
            print(graph[now])
            break
        else:
            Fn = (now * 2) % 10000
            if not visited[Fn]:
                visited[Fn] = True
                graph[Fn] += graph[now] + 'D'
                queue.append(Fn)

            Fn = 9999 if now == 0 else now - 1
            if not visited[Fn]:
                visited[Fn] = True
                graph[Fn] += graph[now] + 'S'
                queue.append(Fn)
            
            Fn = (now // 1000) + ((now % 1000) * 10)
            if not visited[Fn]:
                visited[Fn] = True
                graph[Fn] += graph[now] + 'L'
                queue.append(Fn)

            Fn = (now % 10) * 1000 + (now // 10)
            if not visited[Fn]:
                visited[Fn] = True
                graph[Fn] += graph[now] + 'R'
                queue.append(Fn)

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split(' '))
    graph = [ '' for x in range(10000) ]
    visited = [ False for x in range(10000) ]
    queue = deque()

    visited[A] = True
    queue.append(A)
    BFS()