N = int(input())
print(" " * (N - 1) + "*")

if (N > 1):
    for x in range(N - 2):
        print(" " * (N - 2 - x) + "*" + " " * (x * 2 + 1) + "*")
    print("*" * (N * 2 - 1))