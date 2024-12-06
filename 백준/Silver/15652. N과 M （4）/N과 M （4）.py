import sys

# N과 M 시리즈
# 비내림차순이어야 하니까 마지막에 sorted 적용 -> 역시 시간초과..
# 미리 걸러내면 괜찮으려나

def backTracking(list, depth):
    if depth == M:
        for x in range(1, N+1):
            if len(list) > 0:
                if list[-1] > x:
                    continue
            list.append(x)
            if len(list) >= M:
                print(' '.join(map(str, list)))
            list.pop()
    else:
        for x in range(1, N+1):
            if len(list) > 0:
                if list[-1] > x:
                    continue
            list.append(x)
            if len(list) >= M:
                print(' '.join(map(str, list)))
            else:
                backTracking(list, depth + 1)
            list.pop()

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

backTracking([], 1)