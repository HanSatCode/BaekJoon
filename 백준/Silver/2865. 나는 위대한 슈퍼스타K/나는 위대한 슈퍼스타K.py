import sys
import math

N, M, K = map(int, sys.stdin.readline().rstrip().split(' '))

member = {}
result = []

for line in range(M) :
    temp = sys.stdin.readline().rstrip().split(' ')
    for x in range(0, len(temp), 2) :
        member[temp[x]] = member.get(temp[x], []) + [temp[x+1]]
else:
    for x in range(1, N+1) :
        result.append(max(map(float, member.get(str(x)))))
    else:
        temp = sum(sorted(result, reverse=True)[:K])
        print(f"{temp:.1f}")