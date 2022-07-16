import sys
count = int(sys.stdin.readline())

position = []

for x in range(count) :
    position.append(list(map(int, sys.stdin.readline().split())))

position.sort(key = lambda x: (x[1], x[0]))

for x in position :
    print(x[0], x[1])