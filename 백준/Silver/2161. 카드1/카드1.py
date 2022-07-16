import sys

n = int(sys.stdin.readline().strip('\n'))
num = [ x for x in range(1, n+1) ]

while len(num) != 1 :
    temp = num[1]
    print(num[0], end=' ')
    del num[0:2]
    num.insert(len(num), temp)
else :
    print(num[0])