import sys

N = int(sys.stdin.readline().strip())
A = list(sys.stdin.readline().strip().split(' '))
B = list(sys.stdin.readline().strip().split(' '))
for x in A:
    if not x in B:
        print(x)