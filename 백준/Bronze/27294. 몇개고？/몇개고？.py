import sys
T, S = map(int, sys.stdin.readline().strip().split())
print(320 if (T >= 12 and T <= 16) and S == 0 else 280)