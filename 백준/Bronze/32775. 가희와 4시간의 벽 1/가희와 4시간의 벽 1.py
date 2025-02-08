import sys

S = int(sys.stdin.readline().rstrip())
F = int(sys.stdin.readline().rstrip())
print("flight" if F < S else "high speed rail")