import sys

n = int(sys.stdin.readline().strip('\n'))
left = {}
for _ in range(n) :
    a, b = sys.stdin.readline().strip('\n').split()
    left[a] = left.get(a, 0) + 1
else :
    leftR = [ key for key, value in left.items() if value % 2 != 0 ]
    leftR = sorted(leftR, reverse=True)
    for x in leftR :
        print(x)