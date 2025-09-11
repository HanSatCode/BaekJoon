import sys

P = list(map(int, sys.stdin.readline().strip().split()))
A = list(map(int, sys.stdin.readline().strip().split()))
alive = True

for x in range(4):
    if P[x] in A:
        print(x + 1)
        alive = False
else:
    if alive:
        print(0)