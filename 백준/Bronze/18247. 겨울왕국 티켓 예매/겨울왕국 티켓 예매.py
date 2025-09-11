import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())
    if M < 4 or N < 12:
        print(-1)
    else:
        print(11 * M + 4)
