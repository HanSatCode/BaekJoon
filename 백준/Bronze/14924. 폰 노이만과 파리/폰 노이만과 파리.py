import sys

S, T, D = map(int, sys.stdin.readline().strip().split())
print(T*(D//(S*2)))