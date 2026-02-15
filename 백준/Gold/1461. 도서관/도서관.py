import sys

N, M = map(int, sys.stdin.readline().split())
T = list(map(int, sys.stdin.readline().split()))

R = sorted([ x for x in T if x > 0 ], key=lambda x: (x))
L = sorted([ x for x in T if x < 0 ], key=lambda x: (x))

result = 0

if R and (not L): # 오른쪽만 있을 때
    for x in range(len(R) - M - 1, -1, -M): result += R[x] * 2
    result += R[-1]
elif L and (not R): # 왼쪽만 있을 때
    for x in range(M, len(L), M): result += -L[x] * 2
    result += -L[0]
else:
    if R[-1] < -L[0]: # 왼쪽이 더 큼
        for x in range(M, len(L), M): result += -L[x] * 2
        for x in range(len(R) - 1, -1, -M): result += R[x] * 2
        result += -L[0]
    else: # 오른쪽이 더 큼
        for i in range(0, len(L), M): result += -L[i] * 2
        for i in range(len(R) - M - 1, -1, -M): result += R[i] * 2
        result += R[-1]
print(result)