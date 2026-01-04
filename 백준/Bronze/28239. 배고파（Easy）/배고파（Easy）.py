import sys

N = int(sys.stdin.readline().strip())
for _ in range(N):
    m = str(bin(int(sys.stdin.readline().strip())))[2:]
    x = len(m) - m.rindex('1') - 1
    y = len(m) - m.index('1') - 1
    if x == y: print(x - 1, y - 1)
    else: print(x, y)