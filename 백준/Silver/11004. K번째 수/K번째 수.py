import sys
N, K = map(int, sys.stdin.readline().strip('\n').split())
L = sorted(list(map(int, sys.stdin.readline().strip('\n').split())))
print(L[K-1])