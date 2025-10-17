import sys

N = sys.stdin.readline().strip()
print(str(bin(int(N, 8)))[2:])