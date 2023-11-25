import sys

N = int(sys.stdin.readline().rstrip())
R = 0
if N <= 9:
    print(N)
else:
    for x in range(1, len(str(N))):
        R += x * int(str(9) + str(str(0) * (x-1)))
    R += len(str(N)) * (N - int(str(9) * (len(str(N)) - 1)))
    print(R % 1234567)