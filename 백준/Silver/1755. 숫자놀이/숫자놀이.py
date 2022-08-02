import sys

alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

num = {}
M, N = map(int, sys.stdin.readline().strip('\n').split())

for x in range(M, N+1) :
    temp = ''
    for y in range(len(str(x))) :
        temp += alpha[int(str(x)[y])]
    else :
        num[temp] = x

num = sorted(num.items())

cnt = 0
for z in range(len(num)) :
    print(num[z][1], end=' ')
    cnt += 1
    if cnt == 10 :
        print()
        cnt = 0