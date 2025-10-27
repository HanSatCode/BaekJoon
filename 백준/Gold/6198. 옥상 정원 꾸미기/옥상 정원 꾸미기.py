import sys

N = int(sys.stdin.readline().strip())
T = []
S = []
R = 0

for _ in range(N):
    T.append(int(sys.stdin.readline().strip()))

for element in T: # N-1번 반복
    if S and element < S[-1]:
        S.append(element)
        R += len(S) - 1
    else:
        while S and S[-1] <= element:
            S.pop()
        S.append(element)
        R += len(S) - 1
print(R)