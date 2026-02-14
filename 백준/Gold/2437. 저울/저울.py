import sys

N = int(sys.stdin.readline().strip())
L = sorted(list(map(int, sys.stdin.readline().strip().split())))
S = L[0]
for i in range(1, N):
    if S + 1 < L[i]: break
    S += L[i]
print(S + 1 if L[0] == 1 else 1)