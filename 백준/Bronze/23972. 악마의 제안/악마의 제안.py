import sys

K, N = map(int, sys.stdin.readline().split())

if N == 1 : # 무조건 손해
    print(-1)
else :
    temp = (K * N) // (N - 1)
    if (K * N) % (N - 1) != 0 :
        temp += 1
    print(temp)