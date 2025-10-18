import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
V = 0

for a in A:
    x = 1 - (V / 100)
    y = 1 - (a / 100)
    V = (1 - (x * y))*100
    print(f"{V:.06f}")