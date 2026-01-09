import sys

N, M, K = map(int, sys.stdin.readline().strip().split(' ')) # 수 갯수, 변경 횟수, 구간 곱 구하기 횟수

A = [] # 처음 입력
segTree = [1] * N * 4 # 세그먼트 트리
MOD = 1000000007


for _ in range(N): A.append(int(sys.stdin.readline().strip()))

def init(start, end, node):
    if start == end: 
        segTree[node] = A[start]
        return segTree[node]
    mid = (start + end) // 2
    segTree[node] = (init(start, mid, node * 2) * init(mid + 1, end, node * 2 + 1)) % MOD
    return segTree[node]

init(0, N - 1, 1) # 초기화

def update(start, end, node, index, newValue):
    if index < start or end < index: return segTree[node]

    if start == end: 
        segTree[node] = newValue # 리프노드에 도달했을 때
        return segTree[node]

    mid = (start + end) // 2
    segTree[node] = (update(start, mid, node * 2, index, newValue) * update(mid + 1, end, node * 2 + 1, index, newValue)) % MOD
    return segTree[node]

def find(start, end, node, left, right):
    if end < left or right < start : return 1 # 범위 벗어남
    if left <= start and end <= right: return segTree[node]
    mid = (start + end) // 2
    return (find(start, mid, node * 2, left, right) * find(mid + 1, end, node * 2 + 1, left, right)) % MOD

for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().strip().split(' '))
    if a == 1: # 수 변경
        update(0, N - 1, 1, b - 1, c)
        A[b - 1] = c
    else: # b - c 구간 곱
        print(find(0, N - 1, 1, b - 1, c - 1))
    #print(segTree)