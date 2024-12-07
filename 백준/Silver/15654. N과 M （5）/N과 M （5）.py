import sys

#갯수 / 길이
N, M = map(int, sys.stdin.readline().rstrip().split(" "))
L = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))

def backTracking(list, depth):
    if depth == M:
        for element in L:
            if element in list:
                continue
            list.append(element)
            if len(list) == M:
                print(' '.join(map(str, list)))
            list.pop()
    else:
        for element in L:
            if element in list:
                continue
            list.append(element)
            if len(list) == M:
                print(' '.join(map(str, list)))
            else:
                backTracking(list, depth + 1)
            list.pop()

backTracking([], 0);