import sys
import math

def gcd(a, b):
    while b: a, b = b, a % b
    return a

N = int(sys.stdin.readline().strip())
L1 = []
for _ in range(N): L1.append(int(sys.stdin.readline().strip()))
L1.sort()
L2 = sorted([ L1[x] - L1[x - 1] for x in range(1, len(L1)) ])

G = L2[0] # 최대공약수
for i in range(1, len(L2)): G = gcd(G, L2[i])

R = []
for x in range(1, int(math.sqrt(G)) + 1):
    if G % x == 0: 
        R.append(x)
        if x != G // x: R.append(G // x)

R.sort()
print(' '.join(map(str, R[1:])))