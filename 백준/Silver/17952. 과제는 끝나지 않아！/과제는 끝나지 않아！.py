import sys

minute = int(sys.stdin.readline().strip('\n'))
Stack = []
score = 0

for x in range(1, minute+1) :
    temp = list(map(int, sys.stdin.readline().strip('\n').split()))
    if (Stack == [] and temp != [0]) or (Stack != []) :
        if x >= 2 : # 2분째 경과
            if temp != [0] :
                Stack.append(temp) 
        else :
            Stack.append(temp)
        Stack[-1][2] -= 1

        if Stack[-1][2] == 0 : # 처리 완료
            score += Stack[-1][1]
            Stack.pop()
else :
    print(score)