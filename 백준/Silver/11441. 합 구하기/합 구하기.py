from itertools import accumulate
import sys

N = int(sys.stdin.readline().strip('\n'))
li = list(map(int, sys.stdin.readline().strip('\n').split()))
pre_li = list(accumulate(li))

M = int(sys.stdin.readline().strip('\n'))

for _ in range(M) :
    start, end = map(int, sys.stdin.readline().strip('\n').split())

    rEnd = end - 1

    if start == end :
        print(li[start-1])
    else :
        if start - 2 < 0 :
            print(pre_li[rEnd])
        else :
            rStart = start - 2
            print(pre_li[rEnd] - pre_li[rStart])