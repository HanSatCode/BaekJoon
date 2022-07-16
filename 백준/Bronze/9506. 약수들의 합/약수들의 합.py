num = []
yac = []
check = []

while True :
    a = int(input())
    num.append(a)
    if a == -1 :
        break

for x in range(0, len(num)-1) :
    temp = []
    for y in range(1, num[x]) :
        if num[x]%y == 0 :
            temp.append(y)
    yac.append(temp)

for x in range(0, len(num)-1) :
    tempYac = 0
    for y in range(0, len(yac[x])) :
        tempYac += yac[x][y]
    check.append(tempYac)

for x in range(0, len(num)-1) :
    if check[x] == num[x] :
        print(f'{num[x]} =', ' + '.join(str(_) for _ in yac[x]))
    else :
        print(f'{num[x]} is NOT perfect.')