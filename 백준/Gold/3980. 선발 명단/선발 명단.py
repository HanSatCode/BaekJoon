# 능력치가 0인 포지션에 배치될 수 없다를 안읽고있었음..
import sys

def backTracking(list, used):
    global M
    if len(list) == 11:
        temp = sum(list)
        if temp > M:
            M = temp
        return
    else:
        for y in range(len(list), 11):
            for x in range(11): # ~ 11
                if x in used or player[y][x] == 0:
                    continue
                list.append(player[y][x])
                used.append(x) # x번째의 인덱스를 사용했음을 알림
                #print(list, used, M)
                backTracking(list, used)
                list.pop()
                used.pop()
            else:
                return

C = int(sys.stdin.readline().rstrip())

for _ in range(C):
    M = 0
    player = []
    m = []
    for x in range(11):
        player.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
        m.append(max(player[x]))
    else:
        backTracking([], [])
        print(M)