import sys
N, M = map(int, sys.stdin.readline().strip().split(' '))
for _ in range(N):
    temp = sys.stdin.readline().strip()
    print(temp[::-1], end="")
    print()