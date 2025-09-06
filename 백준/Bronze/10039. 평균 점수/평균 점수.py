import sys

n = 0
for _ in range(5) :
    temp = int(sys.stdin.readline().strip())
    n += temp if temp > 40 else 40
else:
    print(n // 5)