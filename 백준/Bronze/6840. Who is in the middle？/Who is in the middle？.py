import sys

L = []
for _ in range(3):
    L.append(int(sys.stdin.readline().rstrip()))
else:
    print(sorted(L)[1])
