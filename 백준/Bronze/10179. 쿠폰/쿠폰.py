import sys

N = int(sys.stdin.readline().strip())
for _ in range(N):
    num = float(sys.stdin.readline().strip())
    print(f"${num*0.8:.2f}")