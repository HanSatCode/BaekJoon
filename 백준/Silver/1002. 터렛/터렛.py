import sys
import math

case = int(sys.stdin.readline().strip('\n'))

for _ in range(case) :
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().strip('\n').split())
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if r1 == r2 and d == 0 :
        print('-1')
    else :
        if r1 > r2 :
            temp = r1
            r1 = r2
            r2 = temp
        if r2 - r1 < d and d < r2 + r1 :
            print('2')
        elif r1 + r2 == d or r2 - r1 == d :
            print('1')
        else :
            print('0')