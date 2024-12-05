import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    case = sys.stdin.readline().rstrip()
    length = int(len(case) ** (1/2))
    for jump in range(length, 0, -1) :
        for y in range(jump-1, len(case), length):
            print(case[y], end='')
    print()