import sys

L = list(map(int, sys.stdin.readline().strip().split(' ')))
R = 0
for x in L:
    if x > 0: R += 1
print(R)