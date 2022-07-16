x, y, w, h = map(int, input().split())
checkW, checkH = w/2, h/2
tempX = 0
tempY = 0
result = 0

if checkW <= x :
    tempX = w-x
else :
    tempX = x

if checkH <= y :
    tempY = h-y
else :
    tempY = y

if tempX < tempY :
    result = tempX
else :
    result = tempY

print(result)