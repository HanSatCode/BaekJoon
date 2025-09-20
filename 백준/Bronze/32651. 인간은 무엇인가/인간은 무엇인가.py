import sys
N = int(sys.stdin.readline().strip())
print("Yes" if N % 2024 == 0 and N <= 100000 else "No")