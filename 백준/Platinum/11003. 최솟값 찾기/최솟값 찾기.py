import sys
from collections import deque


N, L = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
D = deque()

for index in range(N):
    while D and D[-1][1] > A[index]: D.pop()
    D.append([index, A[index]])
    if D[0][0] <= index - L: D.popleft()
    print(D[0][1], end=' ')