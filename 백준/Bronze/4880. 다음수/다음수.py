import sys

while True:
    A, B, C = map(int, sys.stdin.readline().split())
    if A == 0 and B == 0 and C == 0:
        break
    if abs(B - A) == abs(C - B):
        print("AP", C + (B - A))
    else:
        print("GP", C * (B // A))