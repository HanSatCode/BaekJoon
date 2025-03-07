import sys

for x in range(2):
    T, F, S, P, C = map(int, sys.stdin.readline().rstrip().split(' '))
    print((T*6) + (F * 3) + (S * 2) + P + (C * 2), end = " ")