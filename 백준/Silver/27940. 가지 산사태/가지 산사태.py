# 사실상 첫 번째만 넘치는지 확인하면 되는거 아닌가..?

import sys

N, M, K = map(int, sys.stdin.readline().rstrip().split(' '))

ground = 0
cnt = 0

for x in range(M):
    T, R = map(int, sys.stdin.readline().rstrip().split(' '))
    ground += R
    if ground > K and (not cnt):
        cnt = x + 1
else:
    if ground > K:
        print(cnt, 1)
    else:
        print(-1)