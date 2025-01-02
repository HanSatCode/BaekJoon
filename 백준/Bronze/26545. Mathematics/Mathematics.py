import sys

A = int(sys.stdin.readline().rstrip())
B = []
for x in range(A):
    B.append(int(sys.stdin.readline().rstrip()))
else:
    print(sum(B))