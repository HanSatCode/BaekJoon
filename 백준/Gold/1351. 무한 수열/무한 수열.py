import sys

mem = {0: 1}

def dp(n):
    if n in mem.keys():
        return mem[n]
    else:
        mem[n] = dp(int(n/P)) + dp(int(n/Q))
        return mem[n]

N, P, Q = map(int, sys.stdin.readline().rstrip().split(' '))

print(dp(N))