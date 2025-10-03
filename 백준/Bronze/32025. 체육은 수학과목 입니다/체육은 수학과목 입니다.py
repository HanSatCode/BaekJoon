import sys
H = int(sys.stdin.readline().rstrip())
W = int(sys.stdin.readline().rstrip())
print(int(min(H, W) / 2 * 100))