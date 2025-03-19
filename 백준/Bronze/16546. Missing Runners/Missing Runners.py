import sys

N = int(sys.stdin.readline().rstrip())
P = [ False for x in range(N + 1)]
temp = list(map(int, sys.stdin.readline().rstrip().split(' ')))

for x in range(N-1):
    P[temp[x]] = True

for x in range(1, N+1):
    if not P[x]:
        print(x)
        break