import sys

a = list(set(map(int, sys.stdin.readline().rstrip().split(' '))))
for x in a:
    if x != 0 and x != 1:
        print('F')
        break
else:
    print('S')