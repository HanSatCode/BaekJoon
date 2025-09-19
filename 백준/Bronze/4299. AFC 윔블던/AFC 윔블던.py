import sys

P, M = map(int, sys.stdin.readline().split(' '))
L = [(P + M) // 2, (P - M) // 2]
if L[0] + L[1] != P or L[0] - L[1] != M or P < M:
    print(-1)
else:
    print(max(L), min(L))