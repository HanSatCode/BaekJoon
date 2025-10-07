import sys

A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline().strip())

print((A + B) - (C * 2) if (A + B) >= (C * 2) else (A + B))