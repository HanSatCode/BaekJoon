import sys

S = [ 25, 10, 5, 1 ]

T = int(sys.stdin.readline().strip())
for _ in range(T):
    C = int(sys.stdin.readline().strip())
    for x in S:
        print(C // x, end=' ')
        C -= (C // x) * x
    print()