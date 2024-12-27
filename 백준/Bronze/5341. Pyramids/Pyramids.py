import sys

while True:
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        break
    temp = 0
    for x in range(1, N + 1):
        temp += x
    else:
        print(temp)