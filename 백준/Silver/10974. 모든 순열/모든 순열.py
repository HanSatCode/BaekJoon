import sys

def backTracking(list, depth): # list : [] , depth : 1
    if depth == N:  #최종 깊이일 때
        for x in range(1, N+1):
            if x not in list:
                list.append(x)
                print(' '.join(map(str, list)))
                list.pop()
                
    else: #아직 위에 있을 때
        for x in range(1, N+1):
            if x not in list:
                list.append(x)
                backTracking(list, depth + 1)
                list.pop()
    return list


N = int(sys.stdin.readline().rstrip())

backTracking([], 1)