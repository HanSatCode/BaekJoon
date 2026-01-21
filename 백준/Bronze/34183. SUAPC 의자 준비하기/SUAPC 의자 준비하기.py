import sys

N, M, A, B = map(int, sys.stdin.readline().strip().split(' '))
if N * 3 <= M: print(0)
else:
    print((N * 3 - M) * A + B)