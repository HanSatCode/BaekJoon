import sys

n = 0
for _ in range(3) :
    temp = list(map(int, sys.stdin.readline().split()))
    result = temp.count(0)
    if result == 0:
        print('E')
    else:
        print(chr(result + 64))