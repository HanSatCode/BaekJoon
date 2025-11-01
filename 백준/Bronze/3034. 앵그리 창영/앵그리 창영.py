import sys

N, W, H = map(int, sys.stdin.readline().split())
max_distance = (W**2 + H**2)**0.5

for _ in range(N):
    line = int(sys.stdin.readline().strip())
    if line <= max_distance:
        print("DA")
    else:
        print("NE")