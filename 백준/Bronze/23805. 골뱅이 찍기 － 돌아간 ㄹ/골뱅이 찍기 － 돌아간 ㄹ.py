import sys

N = int(sys.stdin.readline().rstrip())

for x in range(N):
    print("@" * N * 3 + " " * N + "@" * N)
for y in range(N * 3):
    print("@" * N + " " * N + "@" * N + " " * N + "@" * N)
for z in range(N):
    print("@" * N + " " * N + "@" * N * 3)