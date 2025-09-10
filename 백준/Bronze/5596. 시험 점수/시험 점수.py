import sys

G = []

for _ in range(2):
    G += list(map(int, sys.stdin.readline().strip().split()))
else:
    print(sum(G[0:4]) if sum(G[0:4]) > sum(G[4:8]) else sum(G[4:8]))
