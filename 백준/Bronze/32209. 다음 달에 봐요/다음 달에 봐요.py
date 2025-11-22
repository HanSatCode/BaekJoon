import sys

Q = int(sys.stdin.readline().strip())
E = 0
T = True
for _ in range(Q):
    N, K = map(int, sys.stdin.readline().strip().split())
    match(N) :
        case 1: # 추가
            E += K
        case 2: # 제거
            E -= K
            if E < 0:
                T = False
                E = 0
else :
    if T:
        print("See you next month")
    else:
        print("Adios")