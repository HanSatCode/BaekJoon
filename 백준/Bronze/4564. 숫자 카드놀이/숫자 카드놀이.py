import sys

while True:
    N = sys.stdin.readline().strip()
    if N == "0":
        break
    print(N, end = " ")
    while len(N) > 1:
        temp = 1
        for x in N:
            temp *= int(x)
        print(temp, end = " ")
        N = str(temp)
    print()