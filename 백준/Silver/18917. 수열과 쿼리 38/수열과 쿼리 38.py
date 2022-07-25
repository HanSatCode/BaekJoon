import sys

M = int(sys.stdin.readline().strip('\n'))
S = 0
XOR = 0

for _ in range(M) :
    check = list(map(int, sys.stdin.readline().strip('\n').split()))
    if check[0] == 1 :
        S += check[1]
        XOR ^= check[1]
    elif check[0] == 2 :
        S -= check[1]
        XOR ^= check[1]
    elif check[0] == 3 :
        print(S)
    else : # 4
        print(XOR)