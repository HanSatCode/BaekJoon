import sys

N = int(sys.stdin.readline().strip())
X = int(sys.stdin.readline().strip())
print(f"{(N / (N * (1 - X / 100)) - 1) * 100:.6f}")