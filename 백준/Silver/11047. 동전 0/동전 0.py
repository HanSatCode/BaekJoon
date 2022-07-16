import sys

N, K = map(int, sys.stdin.readline().split())
li = []
cnt = 0

for x in range(N) :
    li.append(int(sys.stdin.readline()))

while K != 0 :
    for y in range(N-1, -1,-1) :
        if K >= li[y] :
            #print(f'{K} % {li[y]} = {K//li[y]} ... {K%li[y]}')
            cnt += K//li[y]
            K = K%li[y]
            break
else :
    print(cnt)