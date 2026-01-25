import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

if N == 1 or M == 1: print(0)
else: print((N-1) * 2 * (M-1))