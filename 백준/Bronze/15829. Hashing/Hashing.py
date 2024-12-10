import sys

hash = 0;

N = int(sys.stdin.readline().rstrip())
L = list(sys.stdin.readline().rstrip())

for x in range(N):
    C = ord(L[x]) - 96
    hash += C * (31 ** x)
else:
    print(hash % 1234567891)