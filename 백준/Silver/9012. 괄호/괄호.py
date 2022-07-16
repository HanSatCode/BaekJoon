import sys

T = int(sys.stdin.readline().strip('\n'))

for _ in range(T) :
    temp = sys.stdin.readline().strip('\n')
    r = 0
    for x in temp :
        if x == '(' :
            r += 1
        else :
            r -= 1
        if r < 0 :
            print('NO')
            break
    else :
        if r != 0 :
            print('NO')
        else :
            print('YES')