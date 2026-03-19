import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    S = int(sys.stdin.readline().strip())
    N = int(sys.stdin.readline().strip())
    for x in range(N):
        A, B = map(int, sys.stdin.readline().strip().split(' '))
        S += A * B
    print(S)