import sys

def backTracking(list):
    if len(list) == M:
        print(' '.join(map(str, list)))
    else:
        lastElement = -1
        for x in range(N):
            if L_used[x] or lastElement == L[x]:
                continue
            lastElement = L[x]
            L_used[x] = True
            list.append(L[x])
            backTracking(list)
            list.pop()
            L_used[x] = False

N, M = map(int, sys.stdin.readline().rstrip().split(" "))
L = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))
L_used = [ False for x in range(N) ]

backTracking([])