import sys

N = int(sys.stdin.readline().strip())
W = int(sys.stdin.readline().strip())
R = N * 10

if N >= 3: R += 20
if N >= 5: R += 50
if W > 1000: R = R - 15
print(R if R > 0 else 0)