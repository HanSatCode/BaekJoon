import sys

L = []

N, K = map(int, sys.stdin.readline().strip('\n').split())
for x in range(N) :
    L.append(list(map(int, sys.stdin.readline().strip('\n').split())))
    if L[x][0] == K :
        target = [ L[x][y] for y in range(1, 4) ]
L = sorted(L, key=lambda x : (-x[1], -x[2], -x[3]))

R = 1
C = 0

for x in L :
    if target == [ x[y] for y in range(1, 4) ] :
        print(R)
        break
    else :
        R += 1