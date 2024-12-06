import sys

def backTracking(list, depth):
    if depth == M:
        for x in range(1, N+1):
            list.append(x)
            if len(list) >= M:
                print(' '.join(map(str, list)))
            list.pop()
    else:
        for x in range(1, N+1):
            list.append(x)
            if len(list) >= M:
                print(' '.join(map(str, list)))
            else:
                backTracking(list, depth + 1)
            list.pop()

# 1부터 N까지 자연수 중에서 M개를 고른 수열
N, M = map(int, sys.stdin.readline().rstrip().split(' '))

backTracking([], 1)

