import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
MAX = M
for _ in range(N):
    i, o = map(int, sys.stdin.readline().strip().split())
    M = M + i - o
    if M > MAX: MAX = M
    if M < 0: 
        print(0)
        sys.exit()
print(MAX)