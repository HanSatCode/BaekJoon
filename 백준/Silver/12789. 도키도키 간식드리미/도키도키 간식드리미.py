# 되게 복잡하게 설계했다 - 좀 더 깔끔하게 구현하기

import sys

N = int(sys.stdin.readline().strip('\n'))
R = [ x for x in range(1, N + 1) ]
Line = list(map(int, sys.stdin.readline().strip('\n').split()))
P = []
Sub = []
M = len(Line) + 1
Check = 1

while P != R :
    if len(Sub) == 0 or len(P) == 0 : # Sub 원소 X
        if Line[0] == Check :
            P.append(Line[0])
            Line.pop(0)
            Check += 1
        else :
            Sub.append(Line[0])
            Line.pop(0)
    else : # Sub 원소 O
        if len(Line) == 0 :
            if P[-1]+1 == Sub[-1] :
                P.append(Sub[-1])
                Sub.pop(-1)
            else :
                print('Sad')
                break
        elif len(Sub) == 0 :
            if P[-1] + 1 == Line[0] :
                P.append(Line[0])
                Line.pop(0)
            else :
                print('Sad')
                break
        else :
            if P[-1] + 1 == Sub[-1] :
                P.append(Sub[-1])
                Sub.pop(-1)
            elif P[-1]+ 1 == Line[0] :
                P.append(Line[0])
                Line.pop(0)
            else :
                Sub.append(Line[0])
                Line.pop(0)
        #print(f'{Line}//{Sub}//{P}')
else :
    print('Nice')