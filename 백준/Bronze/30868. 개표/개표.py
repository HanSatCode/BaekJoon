import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    while n >= 5:
        print("++++", end=" ")
        n -= 5
    else:
        for _ in range(n):
            print("|", end="")
    print()
        