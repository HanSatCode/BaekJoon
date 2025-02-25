import sys
from collections import deque
import time as t

def BFS() :
    while queue:
        #print(queue)
        # 시점, 카운트
        now, cnt = queue.popleft()
        if now == K:
            print(cnt)
            exit()
        for fix in [now - 1, now + 1, now * 2]:
            # 비교 변수로 fix 말고 now 적고 있었음..
            if (fix < 0) or (fix > 200000) or visited[fix]:
                continue
            queue.append([fix, cnt + 1])
            visited[fix] = True
            
N, K = map(int, sys.stdin.readline().rstrip().split(' '))
visited = [False for x in range(200001)]
queue = deque()
queue.append([N, 0])
BFS()