import sys
sys.setrecursionlimit(10**6)


inputArray = [int(sys.stdin.readline().strip())]
for x in range(inputArray[0]):
    inputArray.append(int(sys.stdin.readline().strip()))
N = inputArray[0]

size = 1 # 세그먼트 트리 크기
while size < N: size *= 2 # 세그먼트 트리 크기 계산

inputArray = inputArray + [10**9 + 1] # 인덱스 1부터 시작, 마지막에 큰 값 추가
lastIdx = N + 1 # 마지막 인덱스 (큰 값 위치)
tree = [0] * (size * 2) # 세그먼트 트리 크기 할당

def recursive(node, start, end): # 세그먼트 트리 생성 (베이스 인덱스 1)
    if start == end: # 리프 노드일 경우?
        tree[node] = start if start <= N else lastIdx
        return tree[node]
    mid = (start + end) // 2 # 중간
    leftChild = recursive(node * 2, start, mid)
    rightChild = recursive(node * 2 + 1, mid + 1, end)
    if(inputArray[leftChild] < inputArray[rightChild]): tree[node] = leftChild # 람다 -> if-else로 대체하기
    else: tree[node] = rightChild
    return tree[node]

def query(left, right): # 포인터임. 왼쪽 자식, 오른쪽 자식 아님!
    shortestLengthIndex = lastIdx
    left += (size - 1) # 리프 노드 인덱스 (처음)
    right += (size - 1) # 리프 노드 인덱스 (끝)
    while left <= right:
        if left % 2 == 1: # 오른쪽 자식
            if inputArray[tree[left]] < inputArray[shortestLengthIndex]:
                shortestLengthIndex = tree[left]
            left += 1
        if right % 2 == 0: # 왼쪽 자식
            if inputArray[tree[right]] < inputArray[shortestLengthIndex]:
                shortestLengthIndex = tree[right]
            right -= 1

        left //= 2 # 굳이 형제 노드를 보지 않는 이유? = 부모에 이미 내 형제와 비교한 최솟값이 저장되어 있기 때문
        right //= 2
    return shortestLengthIndex

def solve(start, end): # 최대 직사각형 넓이 계산
    if start > end: return 0
    index = query(start, end) # 구간 최솟값 인덱스
    area = inputArray[index] * (end - start + 1) # 현 구간 전체를 덮는 직사각형 넓이
    if start <= index - 1: area = max(area, solve(start, index - 1)) # 왼쪽 구간을 구할 수 있으면?
    if index + 1 <= end: area = max(area, solve(index + 1, end)) # 오른쪽 구간을 구할 수 있으면?
    return area

recursive(1, 1, size) # 세그먼트 트리 생성 (베이스 인덱스 1)
print(solve(1, N))