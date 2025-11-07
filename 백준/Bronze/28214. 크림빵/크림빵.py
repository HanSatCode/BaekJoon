import sys

N, K, P = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
R = 0

for x in range(0, N*K, K):
    s = sum(A[x:x+K])
    if K-s < P:
        R += 1

print(R)