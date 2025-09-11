import sys

N = int(sys.stdin.readline().strip())
C = 0

for _ in range(N):
    C += int(sys.stdin.readline().strip())
print(C - (N - 1))