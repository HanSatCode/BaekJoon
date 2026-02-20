import sys
from collections import deque

Q = int(sys.stdin.readline())
D = deque()

status = ["-90", "0", "90", "180"] # 반시계 90도, 0도, 시계 90도, 180도

curStatus = 1 # 초기 상태는 0도
BC = 0 # 볼 개수
WC = 0 # 가림막 개수

for _ in range(Q):
    #print(curStatus, D, BC, WC)
    order = sys.stdin.readline().strip()
    if order == "push b": 
        if status[curStatus] == "0" or status[curStatus] == "180":
            D.appendleft("b"); BC += 1
        elif status[curStatus] == "90": # 시계 90도일 때는 볼이 가림막으로 변함
            if WC: D.appendleft("b"); BC += 1
        elif status[curStatus] == "-90": continue
    elif order == "push w": D.appendleft("w"); WC += 1
    elif order == "pop":
        if D: 
            temp = D.pop()
            if temp == "b": BC -= 1
            else: WC -= 1
        if status[curStatus] == "90": # 시계 90도일 때는 볼이 가림막으로 변함
            while D and D[-1] == "b": D.pop(); BC -= 1
        elif status[curStatus] == "-90": # 180도일 때는 볼이 사라짐
            while D and D[0] == "b": D.popleft(); BC -= 1
    elif order == "rotate l": 
        curStatus = (curStatus - 1) % 4
        if status[curStatus] == "90": # 시계 90도일 때는 볼이 가림막으로 변함
            while D and D[-1] == "b": D.pop(); BC -= 1
        elif status[curStatus] == "-90": # 180도일 때는 볼이 사라짐
            while D and D[0] == "b": D.popleft(); BC -= 1
    elif order == "rotate r": 
        curStatus = (curStatus + 1) % 4
        if status[curStatus] == "90": # 시계 90도일 때는 볼이 가림막으로 변함
            while D and D[-1] == "b": D.pop(); BC -= 1
        elif status[curStatus] == "-90": # 180도일 때는 볼이 사라짐
            while D and D[0] == "b": D.popleft(); BC -= 1
    elif order == "count b": print(BC)
    else: print(WC) # count w