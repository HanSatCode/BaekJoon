import sys

def backTracking(list, depth): # list : [] , depth : 1
    if depth == M:
        for x in range(1, N+1):
            if x not in list:
                list.append(x)
                if len(list) == M:
                    print(' '.join(map(str, list)))
                list.pop()
                
    else:
        for x in range(1, N+1):
            if x not in list:
                list.append(x)
                backTracking(list, depth + 1)
                list.pop()
    return list


N, M = map(int, sys.stdin.readline().split(' '))

backTracking([], 1)