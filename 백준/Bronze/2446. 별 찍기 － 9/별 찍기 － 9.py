N = int(input())

for x in range(N):
    print(" " * x + "*" * ((N - x) * 2 - 1))
for x in range(N - 2, -1, -1):
    print(" " * x + "*" * ((N - x) * 2 - 1))