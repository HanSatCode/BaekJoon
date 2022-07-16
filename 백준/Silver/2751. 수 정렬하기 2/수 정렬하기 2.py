import sys
a = int(sys.stdin.readline())
number = []
for x in range (0, a) :
    number.append(int(sys.stdin.readline()))
number.sort()

for x in range (0, a) :
    print(number[x])

''' 기존에 생각했던 알고리즘 (버블정렬). 시간초과됨
import sys
a = int(input())
number = []
y = 0
temp = 0
clear = 0
for x in range (0, a) :
    number.append(int(sys.stdin.readline()))

while True :
    if number[y] >= number[y+1] :
        temp = number[y]
        number[y] = number[y+1]
        number[y+1] = temp
    else :
        clear += 1

        if clear == a-1 :
            break

    y += 1

    if y == a-1 :
        y = 0

for x in range (0, a) :
    print(number[x])'''