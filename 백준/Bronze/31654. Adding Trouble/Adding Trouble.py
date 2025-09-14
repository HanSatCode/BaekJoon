import sys
A, B, C = map(int, sys.stdin.readline().strip().split())
print("correct!" if A + B == C else "wrong!")