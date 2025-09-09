import sys

def solve(left, right):
    if left > right:
        return right
    mid = (left + right) // 2
    temp = 0
    for tree in A:
        temp += tree - mid if tree > mid else 0
    if temp < M:
        return solve(left, mid - 1)
    else:
        return solve(mid + 1, right)

N, M = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))

print(solve(0, max(A)))