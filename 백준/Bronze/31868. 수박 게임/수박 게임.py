import sys

N, K = map(int, sys.stdin.readline().rstrip().split(' '))

print(K // (2 ** (N-1)))