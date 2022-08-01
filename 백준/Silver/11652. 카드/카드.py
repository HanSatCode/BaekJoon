import sys

N = int(sys.stdin.readline().strip('\n'))
num = {}

for _ in range(N) :
    temp = int(sys.stdin.readline().strip('\n'))
    num[temp] = num.get(temp, 0) + 1

print(sorted(num.items(), key = lambda x : (-x[1], x[0]))[0][0])