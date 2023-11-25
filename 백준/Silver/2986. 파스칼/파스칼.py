import sys

N = int(sys.stdin.readline().rstrip())
cnt = 0

# 약수[-2] stop

if N <= 2:
    print(0)
else:
    r = []
    for x in range(1, int(N**(1/2)) + 1):
        if N % x == 0:
            r.append(x)
            r.append(N // x)
    else:
        target = sorted(list(set(r)))[-2]
        cnt = (N - 1) - target + 1
        print(cnt)