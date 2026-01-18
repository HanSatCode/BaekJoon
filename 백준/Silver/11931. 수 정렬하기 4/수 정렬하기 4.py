import sys

N = int(sys.stdin.readline().strip())
L = []
for _ in range(N):
    L.append(int(sys.stdin.readline().strip()))
print('\n'.join(map(str, sorted(L, reverse=True))))