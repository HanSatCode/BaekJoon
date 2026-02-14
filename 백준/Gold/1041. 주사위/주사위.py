import sys

N = int(sys.stdin.readline().strip())
dice = list(map(int, sys.stdin.readline().strip().split()))
m2 = sum(sorted([min(dice[i], dice[5 - i]) for i in range(3)])[:2])
m3 = sum(sorted([min(dice[i], dice[5 - i]) for i in range(3)]))

print((m3 * 4 + (m2 * (N - 1) * 4) + (m2 * (N - 2) * 4) 
       + (min(dice) * (N - 2) * (N - 1) * 4))
       + (min(dice) * (N - 2) * (N - 2))
       if N != 1 else sum(sorted(dice)[:5]))