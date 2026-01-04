import sys

N, M, K = map(int, sys.stdin.readline().split()) # 수 갯수, 수 변경 횟수, 구간합 구하는 횟수
segTree = [0] * (N * 4)
inputArray = []
for _ in range(N):
    inputArray.append(int(sys.stdin.readline()))

def init(start, end, node):
    if start == end:
        segTree[node] = inputArray[start]
        return segTree[node]
    mid = (start + end) // 2
    segTree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return segTree[node]

def update(start, end, node, index, diff):
    if index < start or index > end: return
    segTree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(start, mid, node * 2, index, diff)
        update(mid + 1, end, node * 2 + 1, index, diff)

def sumArea(start, end, node, left, right):
    if left > end or right < start: return 0
    if left <= start and end <= right: return segTree[node]
    mid = (start + end) // 2
    return sumArea(start, mid, node * 2, left, right) + sumArea(mid + 1, end, node * 2 + 1, left, right)

init(0, N - 1, 1)
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split()) # 명령, 위치, 값 / 명령, 위치1, 위치2
    if a == 1: # 수 변경하기
        diff = inputArray[b - 1] - c
        update(0, N - 1, 1, b - 1, -diff)
        inputArray[b - 1] = c # 값 갱신
    else: # 구간 합 구하기
        print(sumArea(0, N - 1, 1, b - 1, c - 1)) # based 0