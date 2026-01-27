import sys

N = int(sys.stdin.readline().strip())

A = list(sys.stdin.readline().strip())
B = list(sys.stdin.readline().strip())

nA = ""
NB = ""
cntA = {}
cntB = {}
if (A[0] == B[0]) and (A[-1] == B[-1]):
    for idx in range(N):
        cntA[A[idx]] = cntA.get(A[idx], 0) + 1
        cntB[B[idx]] = cntB.get(B[idx], 0) + 1
        if not A[idx] in ["a", "e", "i", "o", "u"]: nA += A[idx]
        if not B[idx] in ["a", "e", "i", "o", "u"]: NB += B[idx]
    if cntA == cntB and nA == NB: print("YES")
    else: print("NO")
else:
    print("NO")