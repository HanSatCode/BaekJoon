dap = []
count = int(input())
x = 0
y = 0
temp = ""
plus = 0
point = []
pointTemp = 0

for x in range (x, count) :
    temp = input()
    dap.append(str(temp))

for x in range (0, count) :
    for y in range (0, len(dap[x])) :
        if dap[x][y] == "O":
            plus += 1
        else :
            plus = 0
        pointTemp += plus
    point.append(pointTemp)
    plus = 0
    pointTemp = 0
    print(point[x])