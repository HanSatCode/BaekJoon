import sys

n = list(map(int, sys.stdin.readline().rstrip().split(' ')))

n1 = n[0] * n[1] / n[2]
n2 = n[0] / n[1] * n[2]

print(int(n1 if n1 > n2 else n2))