import sys

N, K = map(int, sys.stdin.readline().strip().split(" "))
L = list(map(int, sys.stdin.readline().strip().split(" ")))

gL = sorted([ L[x + 1] - L[x] for x in range(N - 1) ])
print(sum(gL[:N - K]))