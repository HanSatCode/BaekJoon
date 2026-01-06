import sys 

N = int(sys.stdin.readline().strip())
for _ in range(N):
    d = int(sys.stdin.readline().strip())
    t = 0
    while(t*(t + 1) <= d):
        t += 1
    print(t - 1)