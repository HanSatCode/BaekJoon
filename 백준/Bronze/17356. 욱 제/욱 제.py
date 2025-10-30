import sys
A, B = map(int, sys.stdin.readline().split())
M = (B - A) / 400
E_A = 1 / (1 + 10 ** M)
print(E_A)