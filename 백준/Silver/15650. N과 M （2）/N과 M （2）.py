import sys
import copy 

result = []

def backTracking(list, depth): # list : [] , depth : 1
    global result
    if depth == M:
        for x in range(1, N+1):
            if x not in list:
                list.append(x)
                temp = copy.deepcopy(sorted(list))
                if temp not in result:
                    result += [temp]
                list.pop()
                
    else:
        for x in range(1, N+1):
            if x not in list:
                list.append(x)
                backTracking(list, depth + 1)
                list.pop()
    return list

N, M = map(int, sys.stdin.readline().split(' '))

if N == M:
    print(' '.join(map(str, [x for x in range(1, N+1)])))
else:
    backTracking([], 1)
    for target in result:
        print(' '.join(map(str, target)))