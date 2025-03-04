import sys

N = int(sys.stdin.readline().rstrip())
M = list(map(int, sys.stdin.readline().rstrip().split(' ')))
R = 0

for x in range(len(M)):
    now = M[x]
    temp = 0
    for x in range(x + 1, len(M)):
        if now > M[x]:
            temp += 1
        else:
            break
    if temp > R:
        R = temp
else:
    print(R)