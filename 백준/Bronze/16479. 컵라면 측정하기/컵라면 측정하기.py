import sys

K = int(sys.stdin.readline())
N, M = map(int, sys.stdin.readline().split())
L = (max(N, M) - min(N, M)) / 2
M = K ** 2 - L ** 2 # 피타고라스 정리 활용
if(M == int(M)):
    print(int(M))
else:
    print(M)