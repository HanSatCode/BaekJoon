import sys

N = int(sys.stdin.readline().strip())

if N % 2 == 0:
    print("I LOVE CBNU")
else:
    print("*" * N + "\n" + " " * (N // 2) + "*")
    for x in range(N // 2 - 1, -1, -1):
        print(" " * x + "*" + " " * (N - 2 * x - 2) + "*" if N - 2 * x - 2 >= 0 else " " * x + "*")