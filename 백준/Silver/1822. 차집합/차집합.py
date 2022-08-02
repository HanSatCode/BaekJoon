import sys

An, Bn = map(int, sys.stdin.readline().strip('\n').split())
A = set(map(int, sys.stdin.readline().strip('\n').split()))
B = set(map(int, sys.stdin.readline().strip('\n').split()))

R = sorted(A - B)

print(len(R))
if R :
    print(*R)