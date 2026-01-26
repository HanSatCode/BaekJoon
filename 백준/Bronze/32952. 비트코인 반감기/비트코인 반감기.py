import sys

R, K, M = map(int, sys.stdin.readline().split())
T = 2 ** (M // K) if M >= K else 1
print(int(R / T) if R / T >= 1 else 0)