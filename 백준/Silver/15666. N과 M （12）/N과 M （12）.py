#sorted 사용해서 시간초과 -> 오름차순이 되어야 하니까 이전 원소보다 작으면 OUT

import sys

def backTracking(list):
    if len(list) == M:
        print(' '.join(map(str, list)))
    else:
        lastElement = -1
        length = len(list)
        for x in range(N):
            if lastElement == L[x]:
                continue
            elif length > 0:
                if list[-1] > L[x]:
                    continue
            list.append(L[x])
            lastElement = L[x]
            backTracking(list)
            list.pop()

N, M = map(int, sys.stdin.readline().rstrip().split(" "))
L = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))
result = []

backTracking([])