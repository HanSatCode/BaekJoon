import sys

A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

print("Hanyang Univ." if A + C < B + D else ("Yongdap" if A + C > B + D else "Either"))