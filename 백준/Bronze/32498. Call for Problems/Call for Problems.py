import sys

N = int(sys.stdin.readline().rstrip())
R = 0
for _ in range(N):
    temp = int(sys.stdin.readline().rstrip())
    R += 1 if temp % 2 else 0
else:
    print(R)