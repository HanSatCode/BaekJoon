import sys

while True:
    inputArray = list(map(int, sys.stdin.readline().strip().split())) # 처음은 크기, 나머지는 높이
    N = inputArray[0]
    if N == 0: break

    size = 1 # 세그먼트 트리 크기
    while size < N: size *= 2 # 세그먼트 트리 크기 계산

    inputArray.append(10**9+1) # 인덱스 1부터 시작, 마지막에 큰 값 추가
    lastIdx = N + 1 # 마지막 인덱스 (큰 값 위치)
    tree = [lastIdx] * (size * 2) # 세그먼트 트리 크기 할당

    for i in range(1, N + 1): # 리프 노드에 인덱스 저장
        tree[size + i - 1] = i

    for x in range(size - 1, 0, -1): # 리프 노드 외의 노드 채우기
        leftChild = tree[x * 2]
        rightChild = tree[x * 2 + 1]

        if leftChild == 0: tree[x] = rightChild # 왼쪽 자식이 비어있으면 오른쪽 자식으로
        elif rightChild == 0: tree[x] = leftChild # 오른쪽 자식이 비어있으면 왼쪽 자식으로
        else:
            if inputArray[leftChild] < inputArray[rightChild]: tree[x] = leftChild
            else: tree[x] = rightChild

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
    
    maxArea = 0
    stack = [(1, N)] # 탐색 구간 스택
    while stack:
        start, end = stack.pop()
        if start > end: continue
        minIndex = query(start, end)
        area = (end - start + 1) * inputArray[minIndex]
        if area > maxArea:
            maxArea = area
        stack.append((start, minIndex - 1))
        stack.append((minIndex + 1, end))

    print(maxArea) # 재귀를 아예 안쓰는 방향으로...