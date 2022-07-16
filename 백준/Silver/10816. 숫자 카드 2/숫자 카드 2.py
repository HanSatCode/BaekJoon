import sys

n = int(input())
nL = list(map(int, sys.stdin.readline().split()))
m = int(input())
mL = list(map(int, sys.stdin.readline().split()))

r = {}

for x in nL :
    r[x] = r.get(x, 0) + 1

for y in mL :
    if y in r :
        print(r[y], end= ' ')
    else :
        print('0', end= ' ')