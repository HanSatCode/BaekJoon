import sys

N = int(sys.stdin.readline().strip())
L = [] # 줄
D = [] # 대기공간

for _ in range(N):
    line = list(sys.stdin.readline().strip().split())
    for element in line:
        temp = element.split('-')
        L.append([temp[0], int(temp[1])])

S = sorted(L, key=lambda x: (x[0], x[1]))

while len(L) > 0 and len(S) > 0:
    first = S[0]
    if first == L[0]: # 들어갈 차례이면
        L.pop(0)
        S.pop(0)
    else:
        if len(D) > 0 and first == D[-1]: # 대기공간에서 들어갈 차례이면
            D.pop(-1)
            S.pop(0)
        elif first == L[0]: # 줄에서 들어갈 차례이면
            L.pop(0)
            S.pop(0)
        else: # 대기공간에 넣기
            D.append(L.pop(0))
else: # 둘 중에 하나가 비었을 때
    if len(D) != 0:
        for _ in range(len(D)): # 줄이 먼저 비었을 때
            if D[-1] == S[0]:
                S.pop(0)
                D.pop(-1)
            else:
                print("BAD")
                sys.exit(0)
    if len(L) != 0:
        for _ in range(len(L)): # 대기공간이 먼저 비었을 때
            if L[-1] == S[0]:
                S.pop(0)
                L.pop(-1)
            else:
                print("BAD")
                sys.exit(0)
    print("GOOD")