import sys

N = int(sys.stdin.readline().rstrip())

for x in range(N + 1, 10000):
    if (int(str(x)[:2]) + int(str(x)[2:])) ** 2 == x:
        print(x)
        break
else:
    print(-1)