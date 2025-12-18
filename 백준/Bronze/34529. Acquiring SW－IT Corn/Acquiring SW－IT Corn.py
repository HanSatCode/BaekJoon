import sys

X, Y, Z = map(int, sys.stdin.readline().split())
U, V, W = map(int, sys.stdin.readline().split())
print(int((U/100) * X) + int((V/50) * Y) + int((W / 20) * Z))