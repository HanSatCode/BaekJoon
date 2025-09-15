import sys

N = int(sys.stdin.readline().strip())
S = [str(x) for x in range(1, N + 1)]
print(''.join(S).find(str(N)) + 1)