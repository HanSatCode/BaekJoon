import sys

N, M = map(int, sys.stdin.readline().split())
array = []
segTree = [[10**9 + 1, 0]] * (N * 4)
for _ in range(N):
    array.append(int(sys.stdin.readline().strip())) # 숫자 넣기

def init(start, end, node):
    if start == end:
        segTree[node] = [array[start], array[start]]
        return segTree[node]
    mid = (start + end) // 2
    temp = [ init(start, mid, node * 2), init(mid + 1, end, node * 2 + 1)]
    segTree[node] = [ temp[0][0] if temp[0][0] < temp[1][0] else temp[1][0],
                     temp[0][1] if temp[0][1] > temp[1][1] else temp[1][1] ]
    return segTree[node]

init(0, N - 1, 1)

def solve(start, end, node, left, right):
    if left > end or right < start: return [10**9 + 1, 0]
    if left <= start and end <= right: return segTree[node]
    mid = (start + end) // 2
    temp = [solve(start, mid, node * 2, left, right), solve(mid + 1, end, node * 2 + 1, left, right)]
    return  [ temp[0][0] if temp[0][0] < temp[1][0] else temp[1][0],
            temp[0][1] if temp[0][1] > temp[1][1] else temp[1][1] ]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split(' '))
    print(' '.join(map(str, solve(0, N - 1, 1, a - 1, b - 1))))