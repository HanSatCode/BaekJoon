import sys

T = int(sys.stdin.readline().rstrip())
N = []

for _ in range(T):
    N.append(int(sys.stdin.readline().rstrip()))
M = 318138

case = [ x for x in range(0, M+1) ]

for x in range(2, M + 1):
    if case[x] == 0:
        continue
    for y in range(2*x, M + 1, x):
        case[y] = 0
case = sorted(list(set(case)))[2:]

for x in range(2, len(case)):
    if case[x-1] == 0:
        continue
    for y in range(2*x, len(case), x):
        case[y-1] = 0
case = sorted(list(set(case)))[2:]

for x in N:
    print(case[x-1])