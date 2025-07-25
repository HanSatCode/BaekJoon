import sys
import math

N, M = map(int, sys.stdin.readline().split())

V = abs(math.ceil(N / 4) - math.ceil(M / 4))
H = abs((N % 4 if N % 4 != 0 else 4) - (M % 4 if M % 4 != 0 else 4))
print(V + H)