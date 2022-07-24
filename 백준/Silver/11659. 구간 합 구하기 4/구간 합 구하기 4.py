from itertools import accumulate
import sys

N, M = map(int, sys.stdin.readline().strip('\n').split())
li = list(map(int, sys.stdin.readline().strip('\n').split()))
pre_li = list(accumulate(li))
for _ in range(M) :
    start, end = map(int, sys.stdin.readline().strip('\n').split())
    if start == end : 
        print(li[start-1])
    else :
        rEnd = end - 1
        if start - 2 < 0 :
            print(pre_li[rEnd])
        else :
            rStart = start - 2
            print(pre_li[rEnd] - pre_li[rStart])