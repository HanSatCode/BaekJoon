import sys

n = int(sys.stdin.readline().strip())
for x in range(n):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    print(f"Case {x + 1}: {temp[0] + temp[1]}")