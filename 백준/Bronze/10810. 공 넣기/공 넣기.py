import sys

D = {}
N, M = map(int, sys.stdin.readline().split())
for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for x in range(i, j + 1):
        D[x] = k
for x in range(N):
    print(D[x+1] if D.get(x+1) is not None else 0, end = ' ')