import sys

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    Y, K = 0, 0
    for i in range(9):
        tY, tK = map(int, sys.stdin.readline().rstrip().split())
        Y += tY
        K += tK
    if Y > K:
        print("Yonsei")
    elif Y < K:
        print("Korea")
    else:
        print("Draw")