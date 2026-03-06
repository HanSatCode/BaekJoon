import sys

N = int(sys.stdin.readline().strip())
L = []

for _ in range(N):
    L.append(list(map(int, sys.stdin.readline().strip().split(' '))))
L = sorted(L, key = lambda x: x[0])

DP = [1] * N
for x in range(1, N):
    for y in range(x):
        if L[y][1] < L[x][1]: DP[x] = max(DP[x], DP[y] + 1)
print(N - max(DP))