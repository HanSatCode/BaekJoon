import sys

n = int(sys.stdin.readline())
m = set(map(int, sys.stdin.readline().split()))
m = sorted(list(m))
for x in range(len(m)) :
    if x == len(m)-1 :
        print(m[x])
    else :
        print(m[x], end=' ')