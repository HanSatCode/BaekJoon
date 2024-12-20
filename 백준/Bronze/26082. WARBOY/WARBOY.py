import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split(' '))
print(B//A*C*3)