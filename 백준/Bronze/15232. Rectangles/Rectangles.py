import sys

R = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())

for x in range(R):
    for y in range(C):
        print('*', end='')
    print()