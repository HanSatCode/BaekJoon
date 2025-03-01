import sys
from collections import deque

def BFS() :
    while queue:
        now, cnt, path = queue.popleft()

        if now == K:
            print(cnt)
            print(*path)
            exit()

        move = [now * 2, now + 1, now - 1]
        for m in range(3):
            M = move[m]
            if (M >= 0 and M < 100001) and not visited[M]:
                queue.append([M, cnt + 1, path + [M]])
                visited[M] = True

N, K = map(int, sys.stdin.readline().rstrip().split(' '))
visited = [ False for x in range(100001) ]
queue = deque()

if N > K:
    print(N - K)
    for x in range(N, K-1, -1):
        print(x, end=' ')
else:
    queue.append([N, 0, [N]])
    BFS()