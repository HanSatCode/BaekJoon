import sys
import math

T = int(sys.stdin.readline().strip())
A = [9.23076, 1.84523, 56.0211, 4.99087, 0.188807, 15.9803, 0.11193]
B = [26.7, 75, 1.5, 42.5, 210, 3.8, 254]
C = [1.835, 1.348, 1.05, 1.81, 1.41, 1.04, 1.88]
D = [0, 1, 1, 0, 1, 1, 0]


for _ in range(T):
    R = 0
    P = list(map(int, sys.stdin.readline().strip().split(' ')))
    for x in range(7):
        if not D[x]: # 트랙
            R += math.floor(A[x] * (math.pow(B[x] - P[x], C[x])))
        else: # 필드
            R += math.floor(A[x] * (math.pow(P[x] - B[x], C[x])))
    print(R)