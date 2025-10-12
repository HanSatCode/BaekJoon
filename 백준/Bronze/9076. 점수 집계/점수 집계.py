import sys

N = int(sys.stdin.readline().strip())
for x in range(N):
    L = sorted(list(map(int, sys.stdin.readline().strip().split())))
    S = sum(L[1:4])
    if L[3] - L[1] >= 4:
        print("KIN")
    else:
        print(S)