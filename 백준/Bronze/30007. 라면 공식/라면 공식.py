import sys
n = int(sys.stdin.readline().rstrip())
for x in range(n):
    A, B, X = map(int, sys.stdin.readline().rstrip().split(' '))
    print(A * (X - 1) + B)