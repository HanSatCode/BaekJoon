import sys

K = int(sys.stdin.readline().rstrip())

for x in range(K):
    P, M = map(int, sys.stdin.readline().rstrip().split(' '))
    cnt = 0
    L = [ False for _ in range(M + 1) ]
    for y in range(P):
        try:
            temp = int(sys.stdin.readline().rstrip())
            if not L[temp]:
                L[temp] = True
            else:
                cnt += 1
        except IndexError:
            cnt += 1
    else:
        print(cnt)